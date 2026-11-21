# Generated from grammar/MiniR.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniRParser import MiniRParser
else:
    from MiniRParser import MiniRParser

# This class defines a complete listener for a parse tree produced by MiniRParser.
class MiniRListener(ParseTreeListener):

    # Enter a parse tree produced by MiniRParser#program.
    def enterProgram(self, ctx:MiniRParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniRParser#program.
    def exitProgram(self, ctx:MiniRParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniRParser#statement.
    def enterStatement(self, ctx:MiniRParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniRParser#statement.
    def exitStatement(self, ctx:MiniRParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniRParser#loadStmt.
    def enterLoadStmt(self, ctx:MiniRParser.LoadStmtContext):
        pass

    # Exit a parse tree produced by MiniRParser#loadStmt.
    def exitLoadStmt(self, ctx:MiniRParser.LoadStmtContext):
        pass


    # Enter a parse tree produced by MiniRParser#assignStmt.
    def enterAssignStmt(self, ctx:MiniRParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by MiniRParser#assignStmt.
    def exitAssignStmt(self, ctx:MiniRParser.AssignStmtContext):
        pass


    # Enter a parse tree produced by MiniRParser#transformStmt.
    def enterTransformStmt(self, ctx:MiniRParser.TransformStmtContext):
        pass

    # Exit a parse tree produced by MiniRParser#transformStmt.
    def exitTransformStmt(self, ctx:MiniRParser.TransformStmtContext):
        pass


    # Enter a parse tree produced by MiniRParser#transformOp.
    def enterTransformOp(self, ctx:MiniRParser.TransformOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#transformOp.
    def exitTransformOp(self, ctx:MiniRParser.TransformOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#dropnaOp.
    def enterDropnaOp(self, ctx:MiniRParser.DropnaOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#dropnaOp.
    def exitDropnaOp(self, ctx:MiniRParser.DropnaOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#filterOp.
    def enterFilterOp(self, ctx:MiniRParser.FilterOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#filterOp.
    def exitFilterOp(self, ctx:MiniRParser.FilterOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#addOp.
    def enterAddOp(self, ctx:MiniRParser.AddOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#addOp.
    def exitAddOp(self, ctx:MiniRParser.AddOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#selectOp.
    def enterSelectOp(self, ctx:MiniRParser.SelectOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#selectOp.
    def exitSelectOp(self, ctx:MiniRParser.SelectOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#groupbyOp.
    def enterGroupbyOp(self, ctx:MiniRParser.GroupbyOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#groupbyOp.
    def exitGroupbyOp(self, ctx:MiniRParser.GroupbyOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#summarizeOp.
    def enterSummarizeOp(self, ctx:MiniRParser.SummarizeOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#summarizeOp.
    def exitSummarizeOp(self, ctx:MiniRParser.SummarizeOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#summarizeItem.
    def enterSummarizeItem(self, ctx:MiniRParser.SummarizeItemContext):
        pass

    # Exit a parse tree produced by MiniRParser#summarizeItem.
    def exitSummarizeItem(self, ctx:MiniRParser.SummarizeItemContext):
        pass


    # Enter a parse tree produced by MiniRParser#aggCall.
    def enterAggCall(self, ctx:MiniRParser.AggCallContext):
        pass

    # Exit a parse tree produced by MiniRParser#aggCall.
    def exitAggCall(self, ctx:MiniRParser.AggCallContext):
        pass


    # Enter a parse tree produced by MiniRParser#aggFunc.
    def enterAggFunc(self, ctx:MiniRParser.AggFuncContext):
        pass

    # Exit a parse tree produced by MiniRParser#aggFunc.
    def exitAggFunc(self, ctx:MiniRParser.AggFuncContext):
        pass


    # Enter a parse tree produced by MiniRParser#sortOp.
    def enterSortOp(self, ctx:MiniRParser.SortOpContext):
        pass

    # Exit a parse tree produced by MiniRParser#sortOp.
    def exitSortOp(self, ctx:MiniRParser.SortOpContext):
        pass


    # Enter a parse tree produced by MiniRParser#sortOrder.
    def enterSortOrder(self, ctx:MiniRParser.SortOrderContext):
        pass

    # Exit a parse tree produced by MiniRParser#sortOrder.
    def exitSortOrder(self, ctx:MiniRParser.SortOrderContext):
        pass


    # Enter a parse tree produced by MiniRParser#plotStmt.
    def enterPlotStmt(self, ctx:MiniRParser.PlotStmtContext):
        pass

    # Exit a parse tree produced by MiniRParser#plotStmt.
    def exitPlotStmt(self, ctx:MiniRParser.PlotStmtContext):
        pass


    # Enter a parse tree produced by MiniRParser#plotPropertyList.
    def enterPlotPropertyList(self, ctx:MiniRParser.PlotPropertyListContext):
        pass

    # Exit a parse tree produced by MiniRParser#plotPropertyList.
    def exitPlotPropertyList(self, ctx:MiniRParser.PlotPropertyListContext):
        pass


    # Enter a parse tree produced by MiniRParser#plotProperty.
    def enterPlotProperty(self, ctx:MiniRParser.PlotPropertyContext):
        pass

    # Exit a parse tree produced by MiniRParser#plotProperty.
    def exitPlotProperty(self, ctx:MiniRParser.PlotPropertyContext):
        pass


    # Enter a parse tree produced by MiniRParser#idList.
    def enterIdList(self, ctx:MiniRParser.IdListContext):
        pass

    # Exit a parse tree produced by MiniRParser#idList.
    def exitIdList(self, ctx:MiniRParser.IdListContext):
        pass


    # Enter a parse tree produced by MiniRParser#exprList.
    def enterExprList(self, ctx:MiniRParser.ExprListContext):
        pass

    # Exit a parse tree produced by MiniRParser#exprList.
    def exitExprList(self, ctx:MiniRParser.ExprListContext):
        pass


    # Enter a parse tree produced by MiniRParser#AndExpr.
    def enterAndExpr(self, ctx:MiniRParser.AndExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#AndExpr.
    def exitAndExpr(self, ctx:MiniRParser.AndExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:MiniRParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:MiniRParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#NotExpr.
    def enterNotExpr(self, ctx:MiniRParser.NotExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#NotExpr.
    def exitNotExpr(self, ctx:MiniRParser.NotExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#RelationalExpr.
    def enterRelationalExpr(self, ctx:MiniRParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#RelationalExpr.
    def exitRelationalExpr(self, ctx:MiniRParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#ParenExpr.
    def enterParenExpr(self, ctx:MiniRParser.ParenExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#ParenExpr.
    def exitParenExpr(self, ctx:MiniRParser.ParenExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#AtomExpr.
    def enterAtomExpr(self, ctx:MiniRParser.AtomExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#AtomExpr.
    def exitAtomExpr(self, ctx:MiniRParser.AtomExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:MiniRParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:MiniRParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#OrExpr.
    def enterOrExpr(self, ctx:MiniRParser.OrExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#OrExpr.
    def exitOrExpr(self, ctx:MiniRParser.OrExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:MiniRParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:MiniRParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#FuncCallExpr.
    def enterFuncCallExpr(self, ctx:MiniRParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by MiniRParser#FuncCallExpr.
    def exitFuncCallExpr(self, ctx:MiniRParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by MiniRParser#primary.
    def enterPrimary(self, ctx:MiniRParser.PrimaryContext):
        pass

    # Exit a parse tree produced by MiniRParser#primary.
    def exitPrimary(self, ctx:MiniRParser.PrimaryContext):
        pass



del MiniRParser