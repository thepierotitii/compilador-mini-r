grammar MiniR;

// reglas del parser

// programa principal
program
    : statement* EOF
    ;

// sentencias soportadas
statement
    : loadStmt
    | transformStmt
    | assignStmt
    | plotStmt
    ;

// carga de datos desde archivo
loadStmt
    : ID ASSIGN READ LPAREN STRING RPAREN SEMI?
    ;

// asignacion de variables y expresiones
assignStmt
    : ID ASSIGN expr SEMI?
    ;

// transformacion secuencial de datasets mediante bloque con dos puntos
transformStmt
    : ID ASSIGN ID COLON transformOp+ SEMI?
    ;

// operaciones disponibles dentro del bloque de transformacion
transformOp
    : dropnaOp
    | filterOp
    | addOp
    | selectOp
    | groupbyOp
    | summarizeOp
    | sortOp
    ;

// eliminar valores nulos
dropnaOp
    : DROPNA LPAREN RPAREN
    ;

// filtrado de filas por condicion logica
filterOp
    : FILTER LPAREN expr RPAREN
    ;

// crear o modificar columnas
addOp
    : ADD LPAREN ID ASSIGN expr RPAREN
    ;

// seleccionar columnas especificas
selectOp
    : SELECT LPAREN idList RPAREN
    ;

// agrupar filas por columnas
groupbyOp
    : GROUPBY LPAREN idList RPAREN
    ;

// resumir columnas mediante funciones estadisticas
summarizeOp
    : SUMMARIZE LPAREN summarizeItem (COMMA summarizeItem)* RPAREN
    ;

summarizeItem
    : ID ASSIGN aggCall
    ;

// invocacion de funcion agregada sobre una columna
aggCall
    : aggFunc LPAREN ID RPAREN
    ;

// funciones estadisticas soportadas
aggFunc
    : SUM
    | MEAN
    | COUNT
    | MAX
    | MIN
    ;

// ordenar dataset por una columna
sortOp
    : SORT LPAREN ID (COMMA sortOrder)? RPAREN
    ;

// sentido del ordenamiento
sortOrder
    : STRING
    | ASC
    | DESC
    ;

// generacion de graficos
plotStmt
    : PLOT ID LPAREN ID RPAREN LBRACE plotPropertyList? RBRACE SEMI?
    ;

plotPropertyList
    : plotProperty (COMMA plotProperty)* COMMA?
    ;

// propiedades del grafico clave valor
plotProperty
    : ID COLON (ID | STRING | INT | FLOAT)
    ;

// lista de identificadores separados por coma
idList
    : ID (COMMA ID)*
    ;

// lista de expresiones separadas por coma
exprList
    : expr (COMMA expr)*
    ;

// jerarquia y precedencia de expresiones
expr
    : NOT expr                                           # NotExpr
    | MINUS expr                                         # UnaryMinusExpr
    | expr (MULT | DIV | MOD) expr                       # MulDivExpr
    | expr (PLUS | MINUS) expr                           # AddSubExpr
    | expr (EQ | NEQ | LT | LTE | GT | GTE) expr         # RelationalExpr
    | expr AND expr                                      # AndExpr
    | expr OR expr                                       # OrExpr
    | ID LPAREN exprList? RPAREN                         # FuncCallExpr
    | LPAREN expr RPAREN                                 # ParenExpr
    | primary                                            # AtomExpr
    ;

// valores basicos atomicos
primary
    : ID
    | INT
    | FLOAT
    | STRING
    | TRUE
    | FALSE
    ;

// reglas del lexer

// palabras clave de operaciones
READ         : 'read' ;
DROPNA       : 'dropna' ;
FILTER       : 'filter' ;
ADD          : 'add' ;
SELECT       : 'select' ;
GROUPBY      : 'groupby' ;
SUMMARIZE    : 'summarize' ;
SORT         : 'sort' ;
PLOT         : 'plot' ;

// funciones estadisticas
SUM          : 'sum' ;
MEAN         : 'mean' ;
COUNT        : 'count' ;
MAX          : 'max' ;
MIN          : 'min' ;

// ordenamiento
ASC          : 'asc' ;
DESC         : 'desc' ;

// literales booleanos
TRUE         : 'true' ;
FALSE        : 'false' ;

// operadores logicos
AND          : 'and' ;
OR           : 'or' ;
NOT          : 'not' ;

// asignacion y delimitadores
ASSIGN       : '=' ;
COLON        : ':' ;
SEMI         : ';' ;
COMMA        : ',' ;
LPAREN       : '(' ;
RPAREN       : ')' ;
LBRACE       : '{' ;
RBRACE       : '}' ;

// operadores aritmeticos
PLUS         : '+' ;
MINUS        : '-' ;
MULT         : '*' ;
DIV          : '/' ;
MOD          : '%' ;

// operadores relacionales
EQ           : '==' ;
NEQ          : '!=' ;
GTE          : '>=' ;
LTE          : '<=' ;
GT           : '>' ;
LT           : '<' ;

// identificadores y literales
ID           : [a-zA-Z_][a-zA-Z0-9_]* ;
INT          : [0-9]+ ;
FLOAT        : [0-9]+ '.' [0-9]+ ;
STRING       : '"' (~["\r\n\\] | '\\' .)* '"' ;

// omision de espacios en blanco y comentarios
WS           : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;
