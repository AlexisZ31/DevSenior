# PROYECTO DE INVESTIGACIÓN CIENTÍFICA EN PYTHON


# 1. INICIALIZACIÓN DE LA LISTA DE EXPERIMENTOS
experimentos = []

# 2. FUNCIONES DE GESTIÓN DE EXPERIMENTOS

## 2.1 Agregar un nuevo experimento
def agregar_experimento():
    print("\n--- Agregar Experimento ---")
    nombre = input("Ingrese el nombre del experimento: ")
    fecha = input("Ingrese la fecha (ejemplo: 10/05/2025): ")

    tipo_valido = ["Química", "Biología", "Física"]
    tipo = input("Ingrese el tipo de experimento (Química, Biología, Física): ")
    if tipo not in tipo_valido:
        print("Tipo de experimento no válido. Debe ser Química, Biología o Física.")
        return

    resultados = input("Ingrese los resultados separados por comas: ")
    resultados_lista = resultados.split(",")
    resultados_finales = []
    for r in resultados_lista:
        try:
            numero = float(r)
            resultados_finales.append(numero)
        except:
            print("Error: Uno de los resultados no es un número. Experimento no agregado.")
            return

    experimento = [nombre, fecha, tipo, resultados_finales]
    experimentos.append(experimento)
    print("Experimento agregado con éxito.")

## 2.2 Ver la lista de experimentos
def ver_experimentos():
    print("\n--- Lista de Experimentos ---")
    if len(experimentos) == 0:
        print("No hay experimentos registrados.")
    else:
        for i in range(len(experimentos)):
            exp = experimentos[i]
            print(str(i + 1) + ". Nombre:", exp[0], "- Fecha:", exp[1], "- Tipo:", exp[2], "- Resultados:", exp[3])

## 2.3 Modificar un experimento existente
def modificar_experimento():
    print("\n--- Modificar Experimento ---")
    ver_experimentos()
    if len(experimentos) == 0:
        return
    try:
        indice = int(input("Ingrese el número del experimento a modificar: ")) - 1
        if indice < 0 or indice >= len(experimentos):
            print("Número inválido.")
            return
    except:
        print("Entrada inválida.")
        return

    nombre = input("Nuevo nombre (Enter para mantener el actual): ")
    fecha = input("Nueva fecha (Enter para mantener la actual): ")
    tipo = input("Nuevo tipo (Enter para mantener el actual): ")
    resultados = input("Nuevos resultados separados por comas (Enter para mantener los actuales): ")

    if nombre != "":
        experimentos[indice][0] = nombre
    if fecha != "":
        experimentos[indice][1] = fecha
    if tipo != "":
        if tipo in ["Química", "Biología", "Física"]:
            experimentos[indice][2] = tipo
        else:
            print("Tipo inválido. Se mantiene el tipo anterior.")
    if resultados != "":
        lista_resultados = resultados.split(",")
        nuevos_resultados = []
        for r in lista_resultados:
            try:
                nuevos_resultados.append(float(r))
            except:
                print("Uno de los nuevos resultados no es válido. Se mantienen los resultados anteriores.")
                return
        experimentos[indice][3] = nuevos_resultados

    print("Experimento modificado.")

## 2.4 Eliminar un experimento
def eliminar_experimento():
    print("\n--- Eliminar Experimento ---")
    ver_experimentos()
    if len(experimentos) == 0:
        return
    try:
        indice = int(input("Ingrese el número del experimento a eliminar: ")) - 1
        if 0 <= indice < len(experimentos):
            eliminado = experimentos.pop(indice)
            print(f"Experimento '{eliminado[0]}' eliminado.")
        else:
            print("Número inválido.")
    except:
        print("Entrada inválida.")

# 3. FUNCIONES DE ANÁLISIS Y COMPARACIÓN

## 3.1 Calcular estadísticas básicas de un experimento
def calcular_estadisticas():
    print("\n--- Análisis de Datos ---")
    ver_experimentos()
    if len(experimentos) == 0:
        return
    try:
        indice = int(input("Seleccione el número del experimento para analizar: ")) - 1
        if indice < 0 or indice >= len(experimentos):
            print("Número inválido.")
            return
    except:
        print("Entrada inválida.")
        return

    datos = experimentos[indice][3]
    if len(datos) == 0:
        print("Este experimento no tiene resultados.")
        return

    suma = 0
    maximo = datos[0]
    minimo = datos[0]
    for valor in datos:
        suma += valor
        if valor > maximo:
            maximo = valor
        if valor < minimo:
            minimo = valor
    promedio = suma / len(datos)

    print("Promedio:", promedio)
    print("Máximo:", maximo)
    print("Mínimo:", minimo)

## 3.2 Comparar promedios de dos experimentos
def comparar_experimentos():
    print("\n--- Comparar Experimentos ---")
    ver_experimentos()
    if len(experimentos) < 2:
        print("Se necesitan al menos dos experimentos para comparar.")
        return
    try:
        i1 = int(input("Ingrese el número del primer experimento: ")) - 1
        i2 = int(input("Ingrese el número del segundo experimento: ")) - 1
        if 0 <= i1 < len(experimentos) and 0 <= i2 < len(experimentos):
            prom1 = sum(experimentos[i1][3]) / len(experimentos[i1][3])
            prom2 = sum(experimentos[i2][3]) / len(experimentos[i2][3])
            print(f"Promedio de '{experimentos[i1][0]}': {prom1}")
            print(f"Promedio de '{experimentos[i2][0]}': {prom2}")
            if prom1 > prom2:
                print(f"'{experimentos[i1][0]}' tiene mejores resultados que '{experimentos[i2][0]}'.")
            elif prom1 < prom2:
                print(f"'{experimentos[i2][0]}' tiene mejores resultados que '{experimentos[i1][0]}'.")
            else:
                print("Ambos experimentos tienen el mismo promedio.")
        else:
            print("Uno o ambos números son inválidos.")
    except:
        print("Entrada inválida. Intente de nuevo.")

# 4. FUNCIONES DE INFORME

def generar_informe():
    print("\n--- Generar Informe ---")
    try:
        archivo = open("informe.txt", "w")
        mejor_promedio = -1
        mejor_nombre = ""
        for exp in experimentos:
            resultados = exp[3]
            promedio = sum(resultados) / len(resultados) if resultados else 0
            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_nombre = exp[0]
            archivo.write("Nombre: " + exp[0] + "\n")
            archivo.write("Fecha: " + exp[1] + "\n")
            archivo.write("Tipo: " + exp[2] + "\n")
            archivo.write("Resultados: " + str(exp[3]) + "\n")
            archivo.write("Promedio: " + str(promedio) + "\n\n")
        archivo.write("Conclusión: El experimento con mejor promedio fue '" + mejor_nombre + "' con " + str(mejor_promedio) + " de promedio.\n")
        archivo.close()
        print("Informe generado correctamente.")
    except:
        print("Error al generar el informe.")

# 5. MENÚ PRINCIPAL DEL PROGRAMA

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar Experimento")
        print("2. Ver Experimentos")
        print("3. Modificar Experimento")
        print("4. Eliminar Experimento")
        print("5. Análisis de Datos")
        print("6. Comparar Experimentos")
        print("7. Generar Informe")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_experimento()
        elif opcion == "2":
            ver_experimentos()
        elif opcion == "3":
            modificar_experimento()
        elif opcion == "4":
            eliminar_experimento()
        elif opcion == "5":
            calcular_estadisticas()
        elif opcion == "6":
            comparar_experimentos()
        elif opcion == "7":
            generar_informe()
        elif opcion == "8":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# 6. INICIAR EL PROGRAMA
menu()
