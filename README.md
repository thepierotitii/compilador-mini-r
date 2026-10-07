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
│   │   └── MiniRVisitor.py
│   └── seman_visitor.py              # Analizador semántico (recorrido del AST y tabla de símbolos)
├── data/                                # Archivos de datos de entrada (.csv)
│   └── ventas.csv
├── examples/                            # Programas de prueba en Mini-R (.mr)
│   ├── 01_bar.mr
│   ├── 02_scatter_line.mr
│   ├── 03_hist_pie.mr
│   ├── 04_error_columna.mr
│   └── 05_error_dataset.mr
├── docs/                                # Documentación formal e informes del proyecto
├── main.py                              # Driver principal CLI del compilador
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
- **Análisis Semántico Robusto:**
  - Tabla de símbolos dinámica con distinción de tipos (`dataset` vs `scalar`).
  - Inspección del esquema de columnas en archivos CSV existentes durante la validación semántica.
  - Propagación y acotación secuencial del conjunto de columnas disponibles a través de operaciones como `select`, `add` y `summarize`.
  - Reporte de errores con posición exacta (línea y columna) para columnas no encontradas, datasets no declarados y variables no válidas.

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

---

## Hitos de Desarrollo

- [x] **Configuración Inicial:** Repositorio y especificación base.
- [x] **Hito 1 (Semana 7):** Front-end inicial (Diseño léxico, gramática ANTLR4, derivaciones por la izquierda, semántica base de 2+ errores y driver simple).
- [ ] **Hito 2 (Semana 12):** Expansión del compilador y manejo de al menos 6 errores semánticos.
- [ ] **Hito 3 (Semana 15):** Back-end, generación de código e integración end-to-end.
