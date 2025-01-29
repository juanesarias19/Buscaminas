import numpy as np

def generar_tablero(tamano, minas):
    # Crear una matriz de ceros
    matriz = [[0] * tamano for _ in range(tamano)]

    # Verificar que la cantidad de minas no sea mayor que los espacios disponibles
    if minas > tamano * tamano:
        return "Error: La cantidad de minas es mayor que el tamaño del tablero."

    # Obtener índices aleatorios para colocar las minas
    indices = np.random.choice(tamano * tamano, minas, replace=False)

    # Colocar las minas en la matriz
    for idx in indices:
        fila = idx // tamano  # Determinar la fila
        columna = idx % tamano  # Determinar la columna
        matriz[fila][columna] = 1

    return matriz  # Devolvemos la matriz con las minas

def tablerito(columnas, matriz):
    print("     ", end="")
    for i in range(65, 65 + columnas):  # Cambié 73 por 65 + columnas para que se ajuste al tamaño
        print(chr(i), end=" ")
    print()

    for i in range(1, columnas + 1):
        if i > 9:
            print(i, end="   ")
        else:
            print(i, end="    ")
        for j in range(columnas):
            if matriz[i - 1][j] == 1:
                print("1", end=" ")  # Representa una mina
            else:
                print("□", end=" ")  # Representa un espacio vacío
        print()
    return tablerito

def contar_minas_alrededor(matriz, fila, columna):
    #Cuenta el número de minas alrededor de una posición dada.
    filas = len(matriz)
    columnas = len(matriz[0])
    minas_cerca = 0

    # Recorrer las posiciones vecinas
    for i in range(max(0, fila - 1), min(filas, fila + 2)):
        for j in range(max(0, columna - 1), min(columnas, columna + 2)):
            if (i, j) != (fila, columna) and matriz[i][j] == 1:
                minas_cerca += 1
    return minas_cerca



def mostrar_tablero_actualizado(matriz, fila, columna):

    filas = len(matriz)
    columnas = len(matriz[0])
    print("\n--- Tablero actualizado ---")
    print("     ", end="")
    for i in range(65, 65 + columnas):  # Cambié 73 por 65 + columnas para que se ajuste al tamaño
        print(chr(i), end=" ")
    print()


    
    for x in range(filas):
        if x >= 9:
            print(x + 1, end="   ")
        else:
            print(x + 1 , end="    ")
        for y in range(columnas):
            if x == fila and y == columna:
                minas_cerca = contar_minas_alrededor(matriz, fila, columna)
                print(minas_cerca, end=" ")
            else:
                print("□", end=" ")
        print()


def verificar_coordenada(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    while True:
        # Pedir la coordenada en un solo input
        entrada = input("Ingrese la coordenada (fila 1-" + str(filas) + ", columna A-" + chr(64 + columnas) + "): ").upper()

        # Separar la entrada en fila y columna
        partes = entrada.split()
        if len(partes) != 2:
            print("Formato incorrecto. Debe ser 'fila columna'. Intenta nuevamente.")
            continue

        fila_str, columna_str = partes


def es_numero(valor):
        for caracter in valor:
            if caracter < '0' or caracter > '9':
             return False
        return True



def verificar_coordenada(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    while True:
        # Pedir la coordenada en un solo input
        entrada = input("Ingrese la coordenada (entre 1-" + str(filas) + "y A-" + chr(64 + columnas) + "): ").upper()

        # Separar la entrada en fila y columna
        partes = entrada.split()
        if len(partes) != 2:
            print("Formato incorrecto. Debe ser 'fila columna'. Intenta nuevamente.")
            continue

        fila_str, columna_str = partes

        # Verificar la fila
        if es_numero(fila_str) == False:
            print("Fila no es un número válido, intenta nuevamente.")
            continue

        fila = int(fila_str) - 1
        if fila < 0 or fila >= filas:
            print("Fila fuera de rango, intenta nuevamente.")
            continue

        # Verificar la columna
        if len(columna_str) != 1 or not ('A' <= columna_str <= chr(64 + columnas)):
            print("Columna fuera de rango, intenta nuevamente.")
            continue

        columna = ord(columna_str) - 65  # Convertir la letra a índice de columna

        # Verificar si hay una mina en la posición
        if matriz[fila][columna] == 1:
            print("\n ¡BOOOM! Has encontrado una mina. 🔥☠️")
            return False  # Fin del juego
        else:
            print("\n No hay mina. Puedes seguir jugando. 👀👌")
            mostrar_tablero_actualizado(matriz, fila, columna)
            return True  # Continuar jugando

print("------------------------------------------")
print("--BIENVENIDO AL  BUSCAMINAS STRAVAGANTE--")
print("------------------------------------------")
tamano = int(input("--Tamaño del tablero: "))  # Pedimos al usuario el tamaño y la cantidad de minas
minas = int(input("--Cantidad de minas: "))
print("------------------------------------------")

# Generamos el tablero y mostramos el resultado
matriz = generar_tablero(tamano, minas)
tablerito(tamano, matriz)
print("Las minas colocadas son =", minas)

# Bucle principal del juego
while True:
    if verificar_coordenada(matriz) == False:
        break  # Fin del juego si se encuentra una mina