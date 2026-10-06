import sys
from antlr4 import InputStream, CommonTokenStream
from src.generated.MiniRLexer import MiniRLexer
from src.generated.MiniRParser import MiniRParser

codigo1 = """
ventas = read("data/ventas.csv")
igv = 0.18

resumen = ventas:
    dropna()
    filter(categoria == "Tecnologia" and stock > 0)
    add(precio_total = precio_unitario * cantidad)
    groupby(sucursal)
    summarize(total = sum(precio_total))
    sort(total, "desc")

plot boxplot(resumen) {
    x: sucursal,
    y: total,
    title: "Ventas por Sucursal"
}
"""

codigo2 = """
clientes = read("data/clientes.csv")
limite_edad = 18

filtrados = clientes:
    filter(edad >= limite_edad and activo == true)
    select(nombre, edad, consumo)
    sort(consumo, "asc")

plot scatter(filtrados) {
    x: edad,
    y: consumo,
    title: "Consumo por Edad"
}
"""

codigo3 = """
datos = read("data/metricas.csv")

metrik = datos:
    dropna()
    groupby(region)
    summarize(promedio = mean(valor), total_registros = count(id), maximo = max(valor), minimo = min(valor))

plot line(metrik) {
    x: region,
    y: promedio,
    title: "Promedio por Región"
}
"""

codigo4 = """
inventario = read("data/inventario.csv")
descuento_general = 0.05

procesado = inventario:
    add(precio_oferta = precio * (1 - descuento_general))
    filter(precio_oferta < 100)

plot hist(procesado) {
    x: precio_oferta,
    title: "Distribución de Precios en Oferta"
}

plot pie(procesado) {
    x: categoria,
    y: precio_oferta,
    title: "Participación de Precios por Categoría"
}
"""


def probar_codigo(nombre, codigo):
    print("=" * 70)
    print(f" PRUEBA: {nombre}")
    print("=" * 70)
    print("Codigo fuente a evaluar:")
    print(codigo.strip())
    print("-" * 70)

    stream_texto = InputStream(codigo)
    lexer = MiniRLexer(stream_texto)
    tokens = CommonTokenStream(lexer)
    parser = MiniRParser(tokens)

    arbol = parser.program()
    num_errores = parser.getNumberOfSyntaxErrors()

    print(f"1. Errores sintacticos encontrados: {num_errores}")

    if num_errores == 0:
        print("2. EXITO: La gramatica reconoció el código sin errores!")
        print("Arbol sintactico generado:")
        print(arbol.toStringTree(recog=parser))
    else:
        print("2. ERROR: Se encontraron errores de sintaxis en el codigo.")
    print("\n")


def main():
    probar_codigo("Caso 1: Carga, Pipeline Completo y Graficos (Boxplot)", codigo1)
    probar_codigo("Caso 2: Seleccion de Columnas, Ordenamiento y Dispersion (Scatter)", codigo2)
    probar_codigo("Caso 3: Multiples Funciones Estadísticas (mean, count, max, min)", codigo3)
    probar_codigo("Caso 4: Graficos Histograma y Pie Chart con Operaciones Aritmeticas", codigo4)


if __name__ == "__main__":
    main()