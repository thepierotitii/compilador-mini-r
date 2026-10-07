import os
import csv
from antlr4 import *
from src.generated.MiniRVisitor import MiniRVisitor
from src.generated.MiniRParser import MiniRParser
from src.symbol_table import SymbolTable, Symbol


class SemanVisitor(MiniRVisitor):
    
    def __init__(self, base_path="."):
        super().__init__()
        self.base_path = base_path

        # tabla de simbolos
        self.table = SymbolTable()

        # lista de errores
        self.errors = []

        # transformaciones
        self.current_dataset_name = None
        self.current_columns = None      
        self.current_group_cols = set()   # columnas agrupadas en groupby()

    @property
    def symbol_table(self):
        return self.table.symbols

    # metodos auxiliares

    def add_error(self, node, message: str):
        line = 0
        col = 0
        if hasattr(node, "symbol") and node.symbol:
            line = node.symbol.line
            col = node.symbol.column
        elif hasattr(node, "start") and node.start:
            line = node.start.line
            col = node.start.column

        self.errors.append({
            "line": line,
            "column": col,
            "message": message
        })

    def check_column(self, node, col_name: str) -> bool:
        """Verifica si una columna existe en el dataset activo del pipeline."""
        if self.current_columns is not None and col_name not in self.current_columns:
            self.add_error(
                node,
                f"La columna '{col_name}' no existe en el dataset '{self.current_dataset_name}'."
            )
            return False
        return True

    def extract_identifiers(self, ctx):
        """Recolecta de forma recursiva los identificadores (ID) dentro de una expresión."""
        result = []
        if ctx is None:
            return result

        # si el nodo es llamada a función validamos solo sus argumentos
        if hasattr(ctx, "exprList") and ctx.exprList():
            for sub in ctx.exprList().expr():
                result.extend(self.extract_identifiers(sub))
            return result

        # si contiene un identificador primario
        if hasattr(ctx, "primary") and ctx.primary() and ctx.primary().ID():
            result.append(ctx.primary().ID())
            return result

        # recorrer subarboles
        if hasattr(ctx, "children") and ctx.children:
            for child in ctx.children:
                if isinstance(child, ParserRuleContext):
                    result.extend(self.extract_identifiers(child))

        return result

    def validate_expression(self, expr_ctx, in_dataset: bool = False):
        if expr_ctx is None:
            return

        for id_node in self.extract_identifiers(expr_ctx):
            name = id_node.getText()
            if in_dataset:
                is_col = (self.current_columns is None) or (name in self.current_columns)
                is_scalar = self.table.exists(name) and self.table.lookup(name).is_scalar()

                if not is_col and not is_scalar:
                    self.add_error(
                        id_node,
                        f"La columna o variable '{name}' no existe en el dataset '{self.current_dataset_name}'."
                    )
            else:
                try:
                    self.table.lookup(name)
                except ValueError:
                    self.add_error(
                        id_node,
                        f"La variable '{name}' no ha sido declarada previamente."
                    )

    # reglas del visitador

    def visitProgram(self, ctx: MiniRParser.ProgramContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.errors

    def visitLoadStmt(self, ctx: MiniRParser.LoadStmtContext):
        var_name = ctx.ID().getText()
        raw_path = ctx.STRING().getText()
        file_path = raw_path.strip('"\'')
        full_path = os.path.join(self.base_path, file_path) if not os.path.isabs(file_path) else file_path

        columns = None
        if os.path.exists(full_path):
            try:
                with open(full_path, mode="r", encoding="utf-8") as f:
                    header = next(csv.reader(f), None)
                    if header:
                        columns = {col.strip() for col in header}
            except Exception as e:
                self.add_error(ctx, f"No se pudo leer el archivo '{file_path}': {str(e)}")
                columns = set()

        # registro de los datos
        self.table.declare(
            name=var_name,
            type_="dataset",
            columns=columns,
            source=file_path
        )
        return None

    def visitAssignStmt(self, ctx: MiniRParser.AssignStmtContext):
        var_name = ctx.ID().getText()
        self.validate_expression(ctx.expr(), in_dataset=False)
        self.table.declare(name=var_name, type_="scalar")
        return None

    def visitTransformStmt(self, ctx: MiniRParser.TransformStmtContext):
        target_name = ctx.ID(0).getText()
        source_name = ctx.ID(1).getText()

        # validar dataset en tabla de simbolos
        try:
            source_symbol = self.table.lookup(source_name)
        except ValueError:
            self.add_error(ctx.ID(1), f"El dataset '{source_name}' no ha sido declarado previamente.")
            self.table.declare(name=target_name, type_="dataset", columns=None)
            return None

        if not source_symbol.is_dataset():
            self.add_error(ctx.ID(1), f"'{source_name}' no es un dataset y no puede ser transformado.")
            return None

        # contexto del pipeline
        self.current_dataset_name = source_name
        self.current_columns = set(source_symbol.columns) if source_symbol.columns is not None else None
        self.current_group_cols = set()

        for op in ctx.transformOp():
            self.visit(op)

        # registro del nuevo dataset
        self.table.declare(
            name=target_name,
            type_="dataset",
            columns=set(self.current_columns) if self.current_columns is not None else None
        )

        # limpiar contexto
        self.current_dataset_name = None
        self.current_columns = None
        self.current_group_cols = set()
        return None

    def visitDropnaOp(self, ctx: MiniRParser.DropnaOpContext):
        return None

    def visitSelectOp(self, ctx: MiniRParser.SelectOpContext):
        new_cols = set()
        for id_node in ctx.idList().ID():
            col = id_node.getText()
            self.check_column(id_node, col)
            new_cols.add(col)

        if self.current_columns is not None:
            self.current_columns = new_cols
        return None

    def visitFilterOp(self, ctx: MiniRParser.FilterOpContext):
        self.validate_expression(ctx.expr(), in_dataset=True)
        return None

    def visitAddOp(self, ctx: MiniRParser.AddOpContext):
        new_col = ctx.ID().getText()
        self.validate_expression(ctx.expr(), in_dataset=True)
        if self.current_columns is not None:
            self.current_columns.add(new_col)
        return None

    def visitGroupbyOp(self, ctx: MiniRParser.GroupbyOpContext):
        self.current_group_cols = set()
        for id_node in ctx.idList().ID():
            col = id_node.getText()
            self.check_column(id_node, col)
            self.current_group_cols.add(col)
        return None

    def visitSummarizeOp(self, ctx: MiniRParser.SummarizeOpContext):
        summary_cols = set()
        for item in ctx.summarizeItem():
            new_col = item.ID().getText()
            agg_call = item.aggCall()
            source_col = agg_call.ID().getText()

            self.check_column(agg_call.ID(), source_col)
            summary_cols.add(new_col)

        if self.current_columns is not None:
            self.current_columns = self.current_group_cols | summary_cols
        return None

    def visitSortOp(self, ctx: MiniRParser.SortOpContext):
        self.check_column(ctx.ID(), ctx.ID().getText())
        return None

    def visitPlotStmt(self, ctx: MiniRParser.PlotStmtContext):
        dataset_name = ctx.ID(1).getText()

        # Validar dataset en la tabla de símbolos
        try:
            dataset_symbol = self.table.lookup(dataset_name)
        except ValueError:
            self.add_error(ctx.ID(1), f"El dataset '{dataset_name}' utilizado en plot no ha sido declarado.")
            return None

        if not dataset_symbol.is_dataset():
            self.add_error(ctx.ID(1), f"'{dataset_name}' no es un dataset y no puede ser graficado.")
            return None

        available_cols = dataset_symbol.columns
        if available_cols is None or not ctx.plotPropertyList():
            return None

        # Validar propiedades x e y
        for prop in ctx.plotPropertyList().plotProperty():
            prop_key = prop.ID(0).getText() if prop.ID(0) else ""
            if prop_key in ("x", "y") and prop.getChildCount() >= 3:
                val_node = prop.getChild(2)
                val_text = val_node.getText()

                is_literal = val_text.startswith(('"', "'")) or val_text.replace('.', '', 1).isdigit()
                is_scalar = self.table.exists(val_text) and self.table.lookup(val_text).is_scalar()

                if not is_literal and not is_scalar and val_text not in available_cols:
                    self.add_error(
                        val_node,
                        f"La columna '{val_text}' no existe en el dataset '{dataset_name}'."
                    )
        return None


SemanticVisitor = SemanVisitor
