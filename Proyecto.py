import json
from datetime import datetime

experimentos = []


def agregar_experimento():
    print("Agregar un nuevo experimento")
    nombre = input("Ingrese el nombre: ")
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    tipo = input("Ingrese el tipo (Química, Biología, Física): ")
    resultados = input("Ingrese los resultados separados por comas: ")

    try:
        fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%d/%m/%Y")
        resultados_lista = resultados.split(",")
        resultados_num = []
        for r in resultados_lista:
            resultados_num.append(float(r))

        experimento = {"nombre": nombre, "fecha": fecha,
                       "tipo": tipo, "resultados": resultados_num}
        experimentos.append(experimento)
        print("Experimento agregado.")
    except:
        print("Hubo un error, por favor revise los datos ingresados.")


def ver_experimentos():
    print("Lista de experimentos")
    if len(experimentos) == 0:
        print("No hay experimentos aún.")
        return
    for i, e in enumerate(experimentos):
        print(f"{i+1}. {e['nombre']} - {e['fecha']
                                        } - {e['tipo']} - {e['resultados']}")


def modificar_experimento():
    ver_experimentos()
    try:
        indice = int(input("Número del experimento a modificar: ")) - 1
        if 0 <= indice < len(experimentos):
            nombre = input(
                "Nuevo nombre (dejar vacío para mantener el actual): ") or experimentos[indice]["nombre"]
            fecha = input(
                "Nueva fecha (DD/MM/AAAA, opcional): ") or experimentos[indice]["fecha"]
            tipo = input(
                "Nuevo tipo (opcional): ") or experimentos[indice]["tipo"]
            resultados = input(
                "Nuevos resultados separados por comas (opcional): ")
            if resultados:
                resultados_lista = resultados.split(",")
                resultados_num = [float(r) for r in resultados_lista]
            else:
                resultados_num = experimentos[indice]["resultados"]

            experimentos[indice] = {
                "nombre": nombre, "fecha": fecha, "tipo": tipo, "resultados": resultados_num}
            print("Experimento modificado.")
        else:
            print("Número inválido.")
    except:
        print("Error en la modificación.")


def calcular_estadisticas():
    ver_experimentos()
    try:
        indice = int(input("Número del experimento para análisis: ")) - 1
        if 0 <= indice < len(experimentos):
            datos = experimentos[indice]["resultados"]
            promedio = sum(datos) / len(datos)
            maximo = max(datos)
            minimo = min(datos)
            print(f"Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")
        else:
            print("Número inválido.")
    except:
        print("Error en el análisis.")


def generar_informe():
    try:
        with open("informe.txt", "w") as archivo:
            for e in experimentos:
                archivo.write(f"Nombre: {e['nombre']}\nFecha: {e['fecha']}\nTipo: {
                              e['tipo']}\nResultados: {e['resultados']}\n\n")
        print("Informe generado.")
    except:
        print("Error al generar el informe.")


def menu():
    while True:
        print("\n1. Agregar Experimento\n2. Ver Experimentos\n3. Modificar Experimento\n4. Análisis de Datos\n5. Generar Informe\n6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            ver_experimentos()
        elif opcion == "3":
            modificar_experimento()
        elif opcion == "4":
            calcular_estadisticas()
        elif opcion == "5":
            generar_informe()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, intente de nuevo.")


menu()
