# Mini-R: Compilador para Análisis y Transformación Declarativa de Datos

**Mini-R** es un lenguaje de programación de dominio específico (DSL) diseñado para simplificar el análisis y visualización de datos. Transforma convenciones complejas de R en un modelo declarativo, claro e intuitivo basado en pipelines (`|`).

El proyecto está desarrollado utilizando **ANTLR4** para el front-end y **Python** para el driver y análisis semántico, con miras a generación de código para entornos de análisis de datos.

---

## Estructura del Proyecto

```text
compilador/
├── .agents/skills/compiler-assistant/   # Skill y reglas de diseño del compilador
├── grammar/                             # Especificación léxica y sintáctica (.g4)
│   └── MiniR.g4
├── src/                                 # Código fuente del compilador en Python
│   ├── driver.py                        # Driver principal CLI
│   └── semantic_visitor.py              # Analizador semántico
├── examples/                            # Programas de prueba (.mr)
├── docs/                                # Documentación formal e informes
└── README.md
```

---

## Requisitos de Entorno

- **Python 3.10+**
- **Java JRE/JDK 11+** (para el generador de código de ANTLR4)
- **antlr4-python3-runtime** (`pip install antlr4-python3-runtime`)

---

## Hitos de Desarrollo

- [x] **Configuración Inicial:** Repositorio y especificación base.
- [ ] **Hito 1 (Semana 7):** Front-end inicial (Diseño léxico, gramática ANTLR4, derivaciones por la izquierda, semántica base de 2 errores y driver simple).
- [ ] **Hito 2 (Semana 12):** Expansión del compilador y manejo de al menos 6 errores semánticos.
- [ ] **Hito 3 (Semana 15):** Back-end, generación de código e integración end-to-end.
