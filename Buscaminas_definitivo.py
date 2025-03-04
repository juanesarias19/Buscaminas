import random
import os #Es una función del módulo os que permite ejecutar comandos del sistema operativo desde Python.
import time


def limpiar_consola():
   #Este comando es basicamente para limpiar la consola cada vez que el usuario realice una acción  
    os.system('cls' if os.name == 'nt' else 'clear')


def generar_tablero(tamano, minas):
    # Crear una matriz de ceros que representan las casillas vacias 
    matriz = [[0] * tamano for _ in range(tamano)]

    # Obtener ubicación aleatoria para colocar las minas usando random.sample
    indices = random.sample(range(tamano * tamano), minas) #Son numeros aleatorios que dterminan las posiciones de las minas 

    # Con este for se colocan las minas en la matriz 
    for idx in indices:
        fila = idx // tamano  # Determinar la fila
        columna = idx % tamano  # Determinar la columna
        matriz[fila][columna] = -1  # -1 representa una mina

    # Se calculan  los números de minas adyacentes para cada casilla
    for fila in range(tamano):
        for columna in range(tamano):
            if matriz[fila][columna] == -1:
                continue  # Si es una mina, no hacemos nada
            # Cuenta las minas adyacentes
            contador = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= fila + i < tamano and 0 <= columna + j < tamano:
                        if matriz[fila + i][columna + j] == -1:
                            contador += 1
            matriz[fila][columna] = contador

    return matriz

#Esta funcion se encarga de toda la parte grafica del juego
def mostrar_tablero(tablero, visible, marcadas, mostrar_minas=False):
    # Mostrar la fila de letras 
    print("   ", end="")
    for i in range(len(tablero)): 
        print(chr(65 + i), end=" ") #se usa el codigo ASCII para esto
    print()

    # Mostrar el tablero con las casillas visibles y marcadas
    for fila in range(len(tablero)):
        print(f"{fila + 1:<2}", end=" ")
        for columna in range(len(tablero[fila])):
            if marcadas[fila][columna]:
                print("🪦", end=" ")  # ESte emoji es para marcar una mina 
            elif visible[fila][columna] or (mostrar_minas and tablero[fila][columna] == -1):
                if tablero[fila][columna] == -1:
                    print("X", end=" ") #si es -1 imprime una X que signiifica una mina 
                elif tablero[fila][columna] == 0:
                    print(" ", end=" ")  # Si es 0 imprime un espacio ya que es 0 significa que no hay mina 
                else:
                    print(tablero[fila][columna], end=" ")# Muestra el número de minas cercanas
            else:
                print("·", end=" ") #imprime puntos 
        print()


def despejar_casilla(tablero, visible, fila, columna):
    #  si la casilla está dentro de los límites del tablero se puede continuar 
    if fila < 0 or fila >= len(tablero) or columna < 0 or columna >= len(tablero[0]):
        return

    # Si la casilla ya está visible, no hacemos nada
    if visible[fila][columna]:
        return
    # Se marca la casilla como visible
    visible[fila][columna] = True

    # Si la casilla es un 0, despejamos las casillas adyacentes
    if tablero[fila][columna] == 0:
        for i in range(-1, 2): #Se recorren las casillas al rededor 
            for j in range(-1, 2):
                # No llamamos a la función para la misma casilla
                if i == 0 and j == 0:
                    continue #Se usa la funcion de una manera recursiva para despejar las otras 
                despejar_casilla(tablero, visible, fila + i, columna + j)


def jugar():
# ESta es una de las funciones mas importantes ya que gestiona la lógica del juego

    # Este bucle permite que el tamaño del buscaminas no sea excedido por el usuario
    while True: # Establece que minimo tiene que ser de 5 y maximo de 20, si no se cumple esto vuelve a pedir la variable
        tamano = int(input("Tamaño del tablero (5- 20): "))
        if tamano <= 20 and tamano >=5:
            break
        else:
            print("El tamaño del tablero debe ser un número entre 5 y 20. Inténtalo de nuevo.")

    cant_minas = (tamano**2) - 5
    while True: #Este bucle hace el filtro para que la cantidad de minas se cumpla dependiendo de las condiciones del juego
        minas = int(input(f"Cantidad de minas (no puede exceder las {cant_minas}): "))
        if minas <= cant_minas and minas > 0:
            break
        else:
            print("Cantidad de minas excedida. Inténtalo de nuevo.")

    # LLamamos la funcion que genera el tablero 
    tablero = generar_tablero(tamano, minas)
    visible = [[False] * tamano for _ in range(tamano)]  # Una matriz del mismo tamaño que el tablero, donde True indica que una casilla es visible para el jugador y False indica que está oculta.
    marcadas = [[False] * tamano for _ in range(tamano)]  # Una matriz del mismo tamaño que el tablero, donde True indica que una casilla está marcada con una bandera (🪦) y False indica que no está marcada.

    # Variable que cuenta el tiempo
    inicio_tiempo = time.time()
    puntuacion = 1000 * minas  # Puntuación inicial basada en el número de minas
    minas_restantes = minas  # Contador de minas restantes

    # Bucle principal del juego
    while True:
        limpiar_consola()  # Esta funcion limpia la consola en cada iteración

        # Mostrar información del juego
        tiempo_transcurrido = int(time.time() - inicio_tiempo)
        print("Tiempo transcurrido:",tiempo_transcurrido, "segundos")
        print("Puntuación: ",max(0, puntuacion - tiempo_transcurrido * 10))  # Puntuación disminuye con el tiempo
        print("Minas restantes:",minas_restantes)
        #Esta funcion es la parte grafica del juego que muestra el tablero 
        mostrar_tablero(tablero, visible, marcadas)

        # Se le pide al usuario que seleccione una casilla o marque una mina
        entrada = input("Selecciona una casilla (ej. A1) o marca una mina (ej. M A1): ").upper().split()
        #En caso de que la entrada sea invalida
        if len(entrada) < 1:
            print("Entrada inválida. Usa el formato LetraNúmero (ej. A1) o M LetraNúmero (ej. M A1).")
            continue
        #Este if verifica que si M esta en la posicion 0 del string, es decir lo primero sera un comando para marcar una mina 
        if entrada[0] == "M" and len(entrada) == 2:  # Marcar/desmarcar una mina
            # Obtener la casilla a marcar
            try: #
                columna = ord(entrada[1][0]) - 65 #Convierte la letra de la columna en un índice numérico 
                fila = int(entrada[1][1:]) - 1  #Convierte el número de la fila en un índice numérico 
            except (ValueError, IndexError):
                print("Formato inválido. Usa M LetraNúmero (ej. M A1).")
                continue

            # Se verifica si la casilla es válida
            if fila < 0 or fila >= tamano or columna < 0 or columna >= tamano:
                print("Casilla fuera de los límites del tablero.")
                continue

            # Alterna la marca en la casilla
            marcadas[fila][columna] = not marcadas[fila][columna]

            # Actualiza el contador de minas restantes
            if marcadas[fila][columna]:
                minas_restantes -= 1
            else:
                minas_restantes += 1 

        else:  # Despejar una casilla
            if len(entrada) < 1:
                print("Entrada inválida. Usa el formato LetraNúmero (ej. A1) o M LetraNúmero (ej. M A1).")
                continue

            # Aqui es para ubicar las posicion es dependiendo de las coordenadas que ingrese el usuario
            try:
                columna = ord(entrada[0][0]) - 65 #Convierte las letras a numero
                fila = int(entrada[0][1:]) - 1    # Aqui acomoda para que los indicies sean correspondientes 
            except (ValueError, IndexError):
                print("Formato inválido. Usa LetraNúmero (ej. A1).")
                continue

            # Aqui es un control para el tamaño del tablero
            if fila < 0 or fila >= tamano or columna < 0 or columna >= tamano:
                print("Casilla fuera de los límites del tablero.")
                continue

            # Esto es en caso de que la casilla este marcada 
            if marcadas[fila][columna]:
                print("No puedes despejar una casilla marcada. Desmárcala primero.")
                continue

            # Si es -1 quiere decir que piso una mina, con lo que el jugador pierde 
            if tablero[fila][columna] == -1:

                print("                                          ")
                print("  ┌────────────────────────────────────┐  ")
                print("  │          PISASTE UNA MINA          │  ")
                print("  │           FIN DEL JUEGO            │  ")
                print("  └────────────────────────────────────┘  ")
                print("                                          ")
                mostrar_tablero(tablero, visible, marcadas, mostrar_minas=True)
                input("Presiona Enter para volver al menú...")
                return

            # Se llama la funcion para despejar casillas 
            despejar_casilla(tablero, visible, fila, columna)

        # Si ha ganado hace lo siguiente 
        ganado = True
        for fila in range(tamano):
            for columna in range(tamano): #Recorre el tablero 
                #Despues del not visible Verifica si la casilla actual no está visible (es decir, está oculta).
                 #Si se encuentra una casilla que no es una mina y está oculta, significa que el jugador no ha ganado todaví.
                if tablero[fila][columna] != -1 and not visible[fila][columna]: #Verifica si la casilla actual no es una mina.
                    ganado = False
                    break
            if not ganado:
                break
        #Si el jugador ha ganado muestra esta interfaz, ademas de colocar la opcion para regresar al menú
        if ganado:
            print("                                          ")
            print("  ┌────────────────────────────────────┐  ")
            print("  │      ¡FELICIADES! HAS GANADO       │  ")
            print("  └────────────────────────────────────┘  ")
            print("                                          ")

            input("Presiona Enter para volver al menú...")
            return

#ESta funcion solo muestra el menu 
def mostrar_menu():
   
    print("                                          ")
    print("  ┌────────────────────────────────────┐  ")
    print("  │BIENVENIDO AL BUSCAMINAS STRAVAGANTE│  ")
    print("  └────────────────────────────────────┘  ")
    print("                                          ")
    print("  ┌────────────────────────────────────┐  ")
    print("  │>1.             Jugar               │  ")
    print("  │>2.          Instrucciones          │  ")
    print("  │>3.             Salir               │  ")
    print("  └────────────────────────────────────┘  ")
#Esta funcion es para traer el catalogo de instrucciones 
def mostrar_instrucciones():
    print("                                          ") 
    print("  ┌────────────────────────────────────┐  ")
    print("  │    INSTRUCCIONES DE BUSCAMINAS     │  ")
    print("  └────────────────────────────────────┘  ")
    print("                                          ")   
    print("──────────────────────────────────────────") 
    print("                                          ")   
    print("  ┌────────────────────────────────────┐  ")
    print("  │            ¿COMO JUGAR?            │  ")
    print("  │1.Coordenadas:                      │  ")  
    print("  │ -Las columnas son letras(A,B,C,..) │  ")  
    print("  │  y las filas son números(1,2,3,..) │  ") 
    print("  │                                    │  ") 
    print("  │2.Despejar casillas:                │  ") 
    print("  │ -Ingresa la coordenada Letra-Número│  ")
    print("  │  para despejar la casilla (ej. A1).│  ")
    print("  │ -Si aparece un número, indica      │  ") 
    print("  │  cuántas minas hay alrededor.      │  ") 
    print("  │ -Si está vacía, se despejarán      │  ") 
    print("  │  automáticamente las casillas      │  ") 
    print("  │  adyacentes.                       │  ") 
    print("  │                                    │  ") 
    print("  │3.Marcar las minas:                 │  ") 
    print("  │ -Si sospechas que hay una mina     │  ")     
    print("  │  márcala con                       │  ") 
    print("  │  M-Letra-Número (ej. M A1)         │  ") 
    print("  │ -Desmarcala con el mismo comando   │  ") 
    print("  │ -Usa los números para deducir      │  ") 
    print("  │  dónde están las minas             │  ") 
    print("  │                                    │  ") 
    print("  │             ¡CUIDADO!              │  ") 
    print("  │Seleccionar una mina acaba el juego │  ") 
    print("  │                                    │  ") 
    print("  │           ¡BUENA SUERTE!           │  ") 
    print("  └────────────────────────────────────┘  ")
   

#Esta es la funcion que permite la navegacion del jugador en la ingterfaz principal del juegp
def menu():
    #Este bucle se repite hasta que el jugador oprima 3
    #Ademas despues de cada partida se vuelve a repetir este bucle 
    while True:
        limpiar_consola() #Siempre tiene que limpiar la consola para que se actualice 
        mostrar_menu() #Se muestra la interfaz del menu dejando al jugador que ingrese una opcion 
        opcion = input("Selecciona una opción: ")
         #Aqui estan las opciones 
         #Si es uno da pie para la funcion jugar que comprende basicamente todo el juego
        if opcion == "1":
            jugar()
        elif opcion == "2":
            #Cuando se inserta el 2 se limpia la consola para que solo quede la interfaz de las instrucciones, ademas se tiene que presionar enter para continuar 
            limpiar_consola()
            mostrar_instrucciones()
            input("\nPresiona Enter para volver al menú...")
            #Si es 3 sale del bucle con 3
        elif opcion == "3":
            print("                                          ")
            print("  ┌────────────────────────────────────┐  ")
            print("  │         ¡GRACIAS POR JUGAR!        │  ")
            print("  └────────────────────────────────────┘  ")
            print("                                          ")
                
            break
        #En caso de que hayan errores 
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")
            input("Presiona Enter para continuar...")


if __name__ == "__main__":
#Todo se resume a una sola funcion
    menu()