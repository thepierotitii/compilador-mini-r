# Generated from grammar/MiniR.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniRParser import MiniRParser
else:
    from MiniRParser import MiniRParser

# This class defines a complete generic visitor for a parse tree produced by MiniRParser.

class MiniRVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniRParser#program.
    def visitProgram(self, ctx:MiniRParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#statement.
    def visitStatement(self, ctx:MiniRParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#loadStmt.
    def visitLoadStmt(self, ctx:MiniRParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#assignStmt.
    def visitAssignStmt(self, ctx:MiniRParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#transformStmt.
    def visitTransformStmt(self, ctx:MiniRParser.TransformStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#transformOp.
    def visitTransformOp(self, ctx:MiniRParser.TransformOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#dropnaOp.
    def visitDropnaOp(self, ctx:MiniRParser.DropnaOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#filterOp.
    def visitFilterOp(self, ctx:MiniRParser.FilterOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#addOp.
    def visitAddOp(self, ctx:MiniRParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#selectOp.
    def visitSelectOp(self, ctx:MiniRParser.SelectOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#groupbyOp.
    def visitGroupbyOp(self, ctx:MiniRParser.GroupbyOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#summarizeOp.
    def visitSummarizeOp(self, ctx:MiniRParser.SummarizeOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#summarizeItem.
    def visitSummarizeItem(self, ctx:MiniRParser.SummarizeItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#aggCall.
    def visitAggCall(self, ctx:MiniRParser.AggCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#aggFunc.
    def visitAggFunc(self, ctx:MiniRParser.AggFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#sortOp.
    def visitSortOp(self, ctx:MiniRParser.SortOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#sortOrder.
    def visitSortOrder(self, ctx:MiniRParser.SortOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#plotStmt.
    def visitPlotStmt(self, ctx:MiniRParser.PlotStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#plotPropertyList.
    def visitPlotPropertyList(self, ctx:MiniRParser.PlotPropertyListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#plotProperty.
    def visitPlotProperty(self, ctx:MiniRParser.PlotPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#idList.
    def visitIdList(self, ctx:MiniRParser.IdListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#exprList.
    def visitExprList(self, ctx:MiniRParser.ExprListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#AndExpr.
    def visitAndExpr(self, ctx:MiniRParser.AndExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:MiniRParser.MulDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#NotExpr.
    def visitNotExpr(self, ctx:MiniRParser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#RelationalExpr.
    def visitRelationalExpr(self, ctx:MiniRParser.RelationalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#ParenExpr.
    def visitParenExpr(self, ctx:MiniRParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#AtomExpr.
    def visitAtomExpr(self, ctx:MiniRParser.AtomExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:MiniRParser.AddSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#OrExpr.
    def visitOrExpr(self, ctx:MiniRParser.OrExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx:MiniRParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:MiniRParser.FuncCallExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniRParser#primary.
    def visitPrimary(self, ctx:MiniRParser.PrimaryContext):
        return self.visitChildren(ctx)



del MiniRParser