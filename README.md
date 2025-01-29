# Buscaminas
# Proyecto de programación sobre el desarrollo de un Buscaminas 

---
#### Integrantes del grupo

* Juan Esteban Arias Lozano
C.C 1011095584
juariaslo@unal.edu.co
* Miguel Angel Moreno Alvarez
C.C 1072423634
migmorenoal@unal.edu.co
* Santiago Aldemar Aguilar Riveros
C.C 1031651244
saaguilar@unal.edu.co
---
# Definición de la Alternativa


## 📌 Objetivo
El proyecto tiene como objetivo el desarrollo de un Buscaminas, este debe consistir de una interfaz simple y facil de entender, debe implemenatar a si mismo una lógica de juego correcta y  desarrollar una versión completamente funcional.


## 📌 Objetivo del avance
El avance del proyecto tiene como objetivo principal asegurar un desarrollo estructurado y eficiente, comenzando con una planeación detallada que establece los pasos necesarios para alcanzar la meta propuesta. Actualmente, se ha trabajado en la creación de la interfaz y la implementación de las funciones básicas, priorizando un diseño intuitivo y funcional que facilite la experiencia del usuario. Durante el desarrollo, se han identificado diversos obstáculos y dificultades, tales como la integración de ciertos componentes, los cuales requieren un enfoque más profundo para garantizar la funcionalidad del sistema.

---

<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Buscaminas: ¿Qué es un Buscaminas?</b></th>
	</tr>
	<tr bgcolor="#e4e4ed">
		<td style="color:#141414"> 
      Buscaminas es un género de videojuegos de lógica. El videojuego presenta una cuadrícula de casillas en las que se puede hacer clic, donde hay «minas» ocultas esparcidas por todo el tablero. <br>
      El objetivo es limpiar el tablero sin detonar ninguna mina, con la ayuda de pistas sobre el número de minas vecinas en las casillas circundantes..<br><br>
      <p align="center">
        <img src="https://www.ludoteka.com/img/juegos/buscaminas3.png" height="180">
      </p>
    </td>
  </tr>
</table>

## Diagrama preliminar

Para describir el proceso y facilitar el desarrollo del algoritmo se optó por realizar un diagra de flujo que resume el funcionamiento básico del juego, desde el inicio, determinar si se gana o pierde, o el resultado de una casilla vacía. 

<details><summary>Diagrama de flujo </summary><p>

```mermaid
flowchart TD
    n1["Leer Rango"] --> n2["Leer Numero de minas"]
    n2 --> A["Generar Matriz de tablero"]
    A --> B("Colocar minas aleatoriamente")
    B --> n3["Descubir casilla"]
    n3 --> C{"¿Es una mina?"}
    C -- No --> n4["Mostrar numero de minas vecinas"]
    C -- Si --> n5["Perdiste"]
    n6["¿Hay casillas libres?"] -- No --> n10["Ganaste"]
    n11(["Inicio"]) --> n1
    n10 --> n12["¿Volver a jugar?"]
    n5 --> n12
    n6 --> n3
    n4 --> n6
    n12 -- Si --> n1
    n12 -- No --> n13(["Fin"])
    n1@{ shape: lean-r}
    n2@{ shape: lean-r}

```
</p></details><br>


## 📌 2. Mecánica de Juego

El Buscaminas es un juego de lógica en el que debes descubrir todas las casillas vacías de un tablero sin detonar ninguna mina.


<details><summary>Tablero y casillas: Se presenta una cuadrícula con casillas ocultas, algunas de las cuales contienen minas.</summary><p>

* Creamos el tablero con una matriz, con la posibilidad de modificar el rango del tablero

  ![image](https://github.com/user-attachments/assets/efe6fb7e-a773-489a-bda7-a7cdb0e43129)


* Añadimos Un random para minas aleatorias en la matriz


</p></details><br>
<details><summary>Clic inicial:</summary><p>

— Para ejecución en consola se tenían dos opciones

  * Inciar en una posición y desplazarnos por el tablero
  * Coordenadas para ubicar las posiciones

![image](https://github.com/user-attachments/assets/6cfb66be-fbab-4bdf-9f7f-1fe65cded9c0)

</p></details><br>

<details><summary>Descubrir casilla: Al hacer clic en una casilla, puede ocurrir una de dos cosas:</summary><p>

* ###  Casilla vacía, indica cuántas minas hay en las casillas adyacentes.

![Captura de pantalla 2025-01-29 103402](https://github.com/user-attachments/assets/ffa89a63-5e62-4d47-aa5c-a035ee9f7f3e)

* ###  Mina, pierdes la partida.

![image](https://github.com/user-attachments/assets/4aecdb59-3e90-4d8f-9a46-704854a35dad)

</p></details><br>

▶ Estrategia y lógica: Usando los números revelados, debes deducir dónde están las minas y marcarlas con banderas.

▶ Victoria: Ganas si descubres todas las casillas sin minas.

## 📌 3. Posibles Desafíos

En la planeación y la realización parcial del proyecto, fueron hallados y pensados algunos obstaculos y desafios, que podrían llegar a requerir más esfuerzo o atención en el futuro, tales como:
* Lógica para la expansión de casillas vacías al hacer clic.
* Gestión de eventos y actualizaciones gráficas en la interfaz.
* Validación de condiciones de victoria y derrota
* Programacion del Temporizador
* Conteo de puntaje

## ¿Como se abordo la solucion de crear un buscaminas en python?
Partimos desde el hecho de que el funcionamiento de un buscaminas se relaciona con las matrices en python; para jugar un buscaminas es necesario tener una tablero de bloques que forman filas y columnas, ahí es donde se encuentran las minas. 

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2uE_vmb6-A35XfltEbnAQyrvBcCbxBP3Y4A&amp;s" height="180">
  <img src="https://github.com/user-attachments/assets/6cfb66be-fbab-4bdf-9f7f-1fe65cded9c0" alt="image" height="180">
  <!-- <img src="https://play-lh.googleusercontent.com/eX5S3Tv3eSO1aWDMQ7MGRO1AaZM-mF0EvRbNsUM887kJVHj0aKv4GnDNj6ds_qvhpak" height="180"> -->
</p>


La base del codigo consiste en crear una matriz base a las minas asignamos el valor 1 y las casillas vacias 0

```
    def generar_tablero(tamano, minas):
    # Se crea una matriz de ceros los cuales son las posiciones seguras 
    matriz = [[0] * tamano for m in range(tamano)]

    # este if es en caso de que las minas sean mayores que el tamaño de la matriz 
    if minas > tamano * tamano:
        return "Error: La cantidad de minas es mayor que el tamaño del tablero."

    # Con esta linea de codigo se generan aleatoriamente las posiciones de los 1 
    indices = np.random.choice(tamano * tamano, minas, replace=False)

    # Colocar las minas en la matriz
    for p in indices:
        fila = p // tamano  # Determinar la fila
        columna = p % tamano  # Determinar la columna
        matriz[fila][columna] = 1

    return matriz  # Devolvemos la matriz con las minas
```

Para la ubicación de minas fue necesario importar una funcion de la biblioteca `NumPy`

```
import numpy as np

# Obtener índices aleatorios para colocar las minas
    indices = np.random.choice(tamano * tamano, minas, replace=False)
```

_`replace=False` indica que no se deben seleccionar índices repetidos. Esto Esto garantiza que solo puede existir una mina por celda._


Esta funcion imprime la interfaz del juego  para que  se vea acorde a un sistema de coordenadas. 

```
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
```

Para contar las minas adyacentes usamos la siguiente función

```
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
```
Para hacer las actualizaciones del tablero se utiliza la siguiente funcion basada en la de la interafz del juego:

```
    def mostrar_tablero_actualizado(matriz, fila, columna):
# Tiene la misma estructura de la funcion tablerito, es para ordenar la matriz 
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

```

Posteriormente se utiliza una función que evalua dato ingresado, verificando si es un digito o no:

```
	def es_numero(valor):
	        for caracter in valor:
	            if caracter < '0' or caracter > '9':
	             return False
	        return True
```

Para hacer el filtro de ingreso de datos y estar seguros de que las coordenadas ingresadas son correctas se usa esta funcion:

```
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

        fila_txt, columna_txt = partes

        # Verificar la fila
        if es_numero(fila_txt) == False:
            print("Fila no es un número válido, intenta nuevamente.")
            continue

        fila = int(fila_txt) - 1
        if fila < 0 or fila >= filas:
            print("Fila fuera de rango, intenta nuevamente.")
            continue

        # Verificar la columna
        if len(columna_txt) != 1 or not ('A' <= columna_txt <= chr(64 + columnas)):
            print("Columna fuera de rango, intenta nuevamente.")
            continue

        columna = ord(columna_txt) - 65  # Convertir la letra a índice de columna

        # Verificar si hay una mina en la posición
        if matriz[fila][columna] == 1:
            print("\n ¡BOOOM! Has encontrado una mina. 🔥☠️")
            return False  # Fin del juego
        else:
            print("\n No hay mina. Puedes seguir jugando. 👀👌")
            mostrar_tablero_actualizado(matriz, fila, columna)
            return True  # Continuar jugando
```

Al final se imprime la interfaz y se llaman las funciones

```
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
```

Este bucle hace que el proceso se repita hasta que el jugador ingrese una mina=

```
# Bucle principal del juego
while True:
    if verificar_coordenada(matriz) == False:
        break  # Fin del juego si se encuentra una mina
```


**Nota:**Esto es solo un avance del proyecto, este se encuentra anexado al principio del repositorio




