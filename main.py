import sys
import os
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from src.generated.MiniRLexer import MiniRLexer
from src.generated.MiniRParser import MiniRParser
from src.seman_visitor import SemanVisitor as SemanticVisitor

# listener para capturar errores sintacticos sin detener el script
class CustomSyntaxErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append({
            "line": line,
            "column": column,
            "message": msg
        })


def run_pipeline(file_path):
    print(f" EJECUTANDO: {file_path}")

    if not os.path.exists(file_path):
        print(f"[!] Error: El archivo '{file_path}' no existe.")
        return False

    with open(file_path, "r", encoding="utf-8") as f:
        codigo_fuente = f.read()

    # analisis lexico y sintactico
    input_stream = InputStream(codigo_fuente)
    lexer = MiniRLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = MiniRParser(tokens)

    syntax_listener = CustomSyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(syntax_listener)

    tree = parser.program()

    # si hay errores sintacticos, los mostramos
    if syntax_listener.errors:
        print("[!] Errores sintacticos detectados:")
        for err in syntax_listener.errors:
            print(f"   - L{err['line']}:C{err['column']} -> {err['message']}")
        return False

    # analisis semantico
    visitor = SemanticVisitor(base_path=".")
    visitor.visit(tree)

    # reporte de resultados
    if visitor.errors:
        print(f"[X] Se encontraron {len(visitor.errors)} error(es) semantico(s):")
        for err in visitor.errors:
            print(f"   - L{err['line']}:C{err['column']} -> {err['message']}")
        return False
    else:
        print("[V] Analisis semantico exitoso! No se detectaron errores.")
        print("    Tabla de simbolos resultante:")
        for id_name, meta in visitor.symbol_table.items():
            print(f"      * {id_name}: {meta}")
        return True


def main():
    if len(sys.argv) > 1:
        # ejecutar archivo especifico indicado como argumento
        filepath = sys.argv[1]
        run_pipeline(filepath)
    else:
        # si no se pasa argumento, ejecutar todos los archivos de la carpeta examples
        examples_dir = "examples"
        if os.path.exists(examples_dir):
            files = sorted([f for f in os.listdir(examples_dir) if f.endswith(".mr") or f.endswith(".txt")])
            if files:
                for filename in files:
                    filepath = os.path.join(examples_dir, filename)
                    run_pipeline(filepath)
            else:
                print(f"[!] No se encontraron archivos de prueba en '{examples_dir}'.")
        else:
            print("Uso: python main.py <ruta_del_archivo.mr>")


if __name__ == "__main__":
    main()