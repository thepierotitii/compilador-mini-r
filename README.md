# Mini-R: Compilador para Análisis y Transformación Declarativa de Datos

**Mini-R** es un lenguaje de programación de dominio específico (DSL) diseñado para simplificar el análisis, transformación y visualización de datos. Transforma operaciones de manipulación de datos en un modelo declarativo, claro e intuitivo basado en bloques de transformación (`:`).

El proyecto está desarrollado utilizando **ANTLR4** para el front-end (análisis léxico y sintáctico) y **Python** para el analizador semántico (Visitor) y el driver principal.

---

## Estructura del Proyecto

```text
compilador-mini-r/
├── grammar/                             # Especificación léxica y sintáctica ANTLR4 (.g4)
│   └── MiniR.g4
├── src/                                 # Código fuente del compilador en Python
│   ├── generated/                       # Lexer, Parser y Visitor generados por ANTLR4
│   │   ├── MiniRLexer.py
│   │   ├── MiniRParser.py
│   │   ├── MiniRVisitor.py
│   │   └── MiniRListener.py
│   ├── seman_visitor.py                 # Analizador semántico (recorrido del AST y chequeo de reglas)
│   └── symbol_table.py                  # Gestión de la Tabla de Símbolos y metadatos de tipos
├── data/                                # Archivos de datos de entrada (.csv)
│   └── ventas.csv
├── examples/                            # Programas de prueba en Mini-R (.mr)
│   ├── 01_bar.mr                        # Caso válido: Carga, agregación y gráfico de barras
│   ├── 02_scatter_line.mr               # Caso válido: Filtros, dispersión y líneas
│   ├── 03_hist_pie.mr                   # Caso válido: Histogramas y pie charts
│   ├── 04_error_columna.mr              # Error semántico: Columna inexistente
│   ├── 05_error_dataset.mr              # Error semántico: Dataset no declarado
│   ├── 06_error_variable_no_declarada.mr # Error semántico: Variable escalar no declarada
│   ├── 07_error_tipo_invalid.mr         # Error semántico: Transformación sobre tipo no dataset
│   ├── 08_error_tipo_grafico.mr         # Error semántico: Tipo de gráfico no soportado
│   ├── 09_error_redefinicion.mr         # Error semántico: Redefinición incompatible de tipos
│   ├── 10_error_propiedad_plot.mr       # Error semántico: Propiedad obligatoria faltante en plot
│   └── 11_error_division_cero.mr        # Error semántico: División estática por cero
├── docs/                                # Documentación formal del proyecto
│   └── arquitectura_compilador.md       # Especificación formal de arquitectura y diseño
├── main.py                              # Driver principal CLI del compilador
├── test_grammar.py                      # Script de pruebas sintácticas independientes
├── requirements.txt                     # Dependencias del proyecto
└── README.md
```

---

## Características del Lenguaje

- **Carga de Datasets:** Asignación declarativa leyendo archivos CSV (`dataset = read("data/ventas.csv")`).
- **Transformaciones en Bloque (`:`):** Soporte para encadenar operaciones como:
  - `dropna()`: Limpieza de valores nulos.
  - `filter(condicion)`: Filtrado por condiciones lógicas y aritméticas.
  - `add(col = expr)`: Creación o derivación de nuevas columnas.
  - `select(col1, col2)`: Selección y acotación del esquema de columnas.
  - `groupby(col1, col2)`: Agrupación de datos por variables.
  - `summarize(nueva_col = func(col))`: Agregaciones estadísticas (`sum`, `mean`, `count`, `max`, `min`).
  - `sort(col, "asc"|"desc")`: Ordenamiento de resultados.
- **Visualización Declarativa:** Sentencia `plot tipo(dataset) { x: col1, y: col2 }` para visualización (`bar`, `scatter`, `line`, `hist`, `pie`).
- **Análisis Semántico Robusto (7+ Errores Verificados):**
  - **Tabla de símbolos modular (`SymbolTable`):** Control estricto de identificadores, tipos (`dataset` vs `scalar`), orígenes y esquemas dimensionales.
  - **Inspección dinámica de esquemas:** Lectura de cabeceras de archivos CSV en disco para validar columnas en tiempo de compilación.
  - **Propagación contextual:** Seguimiento y mutación del conjunto de columnas disponibles a través de pipelines encadenados (`select`, `add`, `summarize`).
  - **Reporte granular con línea y columna:** Detección de:
    1. Acceso a columnas no existentes en el dataset.
    2. Referencia a datasets no declarados.
    3. Uso de variables escalares no declaradas.
    4. Tipo de dato inválido para transformaciones (operador `:` sobre escalares).
    5. Tipo de gráfico no soportado en `plot`.
    6. Redefinición incompatible de tipos (ej. sobreescribir un dataset con un escalar).
    7. Propiedades obligatorias faltantes en gráficos (`x` e `y`).
    8. División estática por cero en expresiones constantes.

---

## Requisitos de Entorno

- **Python 3.10+** (compatible con gestores de entornos como `uv` o `venv`)
- **Java JRE/JDK 11+** (para la generación de parser/lexer con ANTLR4)

---

## Instalación de Dependencias

Con `pip` estándar:

```bash
pip install -r requirements.txt
```

Con `uv` (opcional / recomendado):

```bash
uv venv
uv pip install -r requirements.txt
```

---

## Uso y Ejecución

### 1. Regenerar el Código de ANTLR4 (Opcional)

Si realizas modificaciones en la gramática `grammar/MiniR.g4`, puedes regenerar los lexers, parsers y visitors ejecutando:

```bash
antlr4 -Dlanguage=Python3 -visitor -o src/generated grammar/MiniR.g4
```

### 2. Ejecutar el Driver Principal (`main.py`)

Para ejecutar la suite completa de programas de prueba en `examples/`:

```bash
python main.py
# O utilizando uv:
uv run python main.py
```

Para analizar un archivo específico de Mini-R:

```bash
python main.py examples/01_bar.mr
# O utilizando uv:
uv run python main.py examples/01_bar.mr
```

### 3. Ejecutar Pruebas Sintácticas Independientes (`test_grammar.py`)

Para verificar que la gramática reconozca múltiples construcciones sintácticas y visualizar los árboles de sintaxis concreta (Parse Trees):

```bash
python test_grammar.py
# O utilizando uv:
uv run python test_grammar.py
```

---

## Hitos de Desarrollo

- [x] **Configuración Inicial:** Repositorio y especificación base.
- [x] **Hito 1 (Semana 7):** Front-end inicial (Diseño léxico, gramática ANTLR4, derivaciones por la izquierda, semántica base de 2+ errores y driver simple).
- [x] **Hito 2 (Semana 12):** Expansión del compilador y manejo de al menos 6 errores semánticos.
- [ ] **Hito 3 (Semana 15):** Back-end, generación de código e integración end-to-end.
