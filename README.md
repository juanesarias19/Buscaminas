# Buscaminas
# Proyecto de programación sobre el desarrollo de un Buscaminas 

---
#### Integrantes del grupo

* Juan Esteban Arias Lozano

* Miguel Angel Moreno Alvarez

* Santiago Aldemar Aguilar Riveros

# Definición de la Alternativa


## 📌 Objetivo
El proyecto tiene como objetivo el desarrollo de un Buscaminas, este debe consistir de una interfaz simple y facil de entender, debe implemenatar a si mismo una lógica de juego correcta y  desarrollar una versión completamente funcional.

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

## 📌 Diagrama preliminar

Para describir el proceso y facilitar el desarrollo del algoritmo se optó por realizar un diagrama de flujo que resume el funcionamiento básico del juego, desde el inicio, determinar si se gana o pierde, o el resultado de una casilla vacía. 

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

<!--
## 📌 2. Mecánica de Juego

El Buscaminas es un juego de lógica en el que debes descubrir todas las casillas vacías de un tablero sin detonar ninguna mina.


<details><summary>Tablero y casillas: Se presenta una cuadrícula con casillas ocultas, algunas de las cuales contienen minas.</summary><p>

* Creamos el tablero con una matriz, con la posibilidad de modificar el rango del tablero

  ![image](https://github.com/user-attachments/assets/efe6fb7e-a773-489a-bda7-a7cdb0e43129)


* Añadimos Un random para minas aleatorias en la matriz


</p></details><br>
<details><summary>Iniciar partida: primer casilla </summary><p>

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

-->

## 📌¿Como se abordo la solucion de crear un buscaminas en python?

### 1. Análisis del Problema
Primero, se identificaron los requisitos básicos del juego de Buscaminas:

* **Tablero:** Un tablero de tamaño variable con casillas que pueden contener minas o números que indican el numero de minas adyacentes.

* **Minas:** Un número determinado de minas ubicadas de manera aleatoria en el tablero.

* **Interacción del Usuario:** El jugador debe poder seleccionar casillas para despejarlas o marcarlas como minas.

* **Victoria/Derrota:** El jugador gana si despeja todas las casillas sin minas y pierde si selecciona una casilla con mina.

* **Puntuación:** Un sistema de puntuación basado en el tiempo y el número de minas.

---
---

### 2. Diseño de la Solución

<details><summary> Diagrama de flujo del funcionamiento </summary><p>
	
![Flujo del buscaminas 1](https://github.com/user-attachments/assets/c256f3df-bf25-4065-baa7-a4e63e849c5b)

</p></details><br>  

**Estructura del tablero**

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

* Para la ubicación de minas se utilizó el modulo `random`

```
# Obtener ubicación aleatoria para colocar las minas usando random.sample
    indices = random.sample(range(tamano * tamano), minas) #Son numeros aleatorios que dterminan las posiciones de las minas 
```

___

**Interfaz de Usuario**
* Se diseñó una interfaz de texto para la consola.

  ![image](https://github.com/user-attachments/assets/032498c4-eee5-4634-b5b2-602327a3253b)


<details><summary> Codigo</summary><p>
  
```
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
```
</p></details><br>


* Se añadió una opción de instrucciones.

  ![image](https://github.com/user-attachments/assets/8421f34e-261b-4ce7-b40a-92d7beec901a)

<details><summary> Codigo </summary><p>

```
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
```
	
</p></details><br>  


* Se utilizaron coordenadas (letras para columnas y números para filas) para que el usuario seleccione casillas.

  ![image](https://github.com/user-attachments/assets/1d47fefc-b430-45b2-9837-923260ab2abf)

<details><summary> Codigo </summary><p>

Esta funcion `tablerito` imprime la interfaz del juego  para que  se vea acorde a un sistema de coordenadas. 

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
</p></details><br>  

* Se implementó un sistema para marcar casillas como minas usando el formato M A1.

  ![image](https://github.com/user-attachments/assets/d4bcfb5e-6aac-4820-b9b2-70f45324d1cf)

<details><summary> Codigo </summary><p>

```
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
```

</p></details><br>  
 
___

**Lógica del Juego**
* Se implementó una *función recursiva* `despejar_casilla` para despejar casillas vacías y sus adyacentes automáticamente.

<details><summary> Función depejar casilla </summary><p>
	
```
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
                despejar_casilla(tablero, visible, fila + i, columna + j)
```

</p></details><br>  

* Se verificó si el jugador ganó al despejar todas las casillas sin minas.

<details><summary> Codigo </summary><p>
  
```
ganado = True
        for fila in range(tamano):
            for columna in range(tamano):
                if tablero[fila][columna] != -1 and not visible[fila][columna]:
                    ganado = False
                    break
            if not ganado:
                break

        if ganado:
            print("                                          ")
            print("  ┌────────────────────────────────────┐  ")
            print("  │      ¡FELICIADES! HAS GANADO       │  ")
            print("  └────────────────────────────────────┘  ")
            print("                                          ")

            input("Presiona Enter para volver al menú...")
            return
```
</p></details><br>  

* Se manejó la condición de derrota cuando el jugador selecciona una casilla con mina.

<details><summary> Codigo </summary><p
					    
```
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
            despejar_casilla(tablero, visible, fila, columna)
```
</p></details><br>  

---
---

### 3. Implementación
El código se construyó en Python utilizando algunas de las siguientes herramientas y técnicas:

* **Módulos:**

`import random`
<details><summary> Para la generación aleatoria de minas.</summary><p>

Se usa `random.sample` para seleccionar posiciones aleatorias en el tablero donde se colocarán las minas.
```
indices = random.sample(range(tamano * tamano), minas)
```

Aquí, `random.sample` elige minas números únicos de un rango de 0 a tamano * tamano - 1, que representan las posiciones de las minas.

</p></details><br>

`import os` 
<details><summary> Para limpiar la consola y mejorar la experiencia del usuario.</summary><p>

El módulo `os` proporciona funciones para interactuar con el sistema operativo. En este código, se usa principalmente para limpiar la consola y mejorar la experiencia del usuario.

```
os.system('cls' if os.name == 'nt' else 'clear')
```

`os.name` Devuelve el nombre del sistema operativo ('nt' para Windows)

`cls` Comando para limpiar la consola en Windows.
</p></details><br>

`import time` 
<details><summary>Para medir el tiempo transcurrido y calcular la puntuación. </summary><p>

Se usa `time` para trabajar con funciones relacionadas con el tiempo. En este código, se usa para medir el tiempo transcurrido durante el juego y calcular la puntuación.

* Medición del tiempo: En la función `jugar`, se usa `time.time()` para obtener el tiempo actual en segundos.
```
inicio_tiempo = time.time()
```
Luego, se calcula el tiempo transcurrido restando el tiempo inicial del tiempo actual:

```
tiempo_transcurrido = int(time.time() - inicio_tiempo)
```
Este valor se usa para reducir la puntuación del jugador a medida que pasa el tiempo.
</p></details><br>

* **Funciones principales:**

`generar_tablero` Para crear el tablero con minas y números.

`mostrar_tablero` Para mostrar el tablero en la consola.

`despejar_casilla` Para despejar casillas y sus adyacentes.

`menu` Función que permite la navehación del usuario en la interfaz.

`jugar` Función principal que maneja la lógica del juego.


### 5. Resultado Final
El resultado fue un juego de Buscaminas funcional y entretenido, implementado completamente en Python. El juego incluye:

* Tableros personalizables.
* Un sistema de puntuación dinámico.
* Una interfaz de usuario intuitiva.
* Condiciones claras de victoria y derrota.



