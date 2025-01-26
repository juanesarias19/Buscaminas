# Buscaminas
# Proyecto de programación sobre el desarrollo de un Buscaminas 

El grupo Stravanzza presenta el primer avance de su proyecto, el desarrollo de un Buscaminas en python.

---
#### Integrantes del grupo

* Juan Esteban Arias Lozano
C.C 1011095584
juariaslo@unal.edu.co

---

<table cellspacing="1" bgcolor="">
	<tr bgcolor="#252582">
		<th><b>Buscaminas: ¿Qué es?</b></th>
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


### ¿Como se abordo la solucion de crear un buscaminas en python?
Partimos desde el hecho de que el funcionamiento de un buscaminas se relaciona con las matrices en python; para jugar un buscaminas es necesario tener una tablero de bloques que forman filas y columnas, en estas se encuentran las minas. 

<p align="center">
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2uE_vmb6-A35XfltEbnAQyrvBcCbxBP3Y4A&amp;s" height="180">
  <img src="https://play-lh.googleusercontent.com/eX5S3Tv3eSO1aWDMQ7MGRO1AaZM-mF0EvRbNsUM887kJVHj0aKv4GnDNj6ds_qvhpak" height="180">
</p>

El sentido del juego es que el jugador no sabe las posciones de las minas, asi que tiene que ir ingresando posiciones para ir descubriendo las minas, a medida que avanza si se situa en una mina, el jugador pierde, si se situa en un lugar donde no hay minas se deben descubrir la cercania de las otras minas, es decir, en la cuadricula deben aparecer al rededor de la mina unos numeros que indican la cercania de la misma, es decir, si es 1 hay 1 mina al rededor (al rededor comprende la posicion de abajo, arriba, izquierda, derecha y diagonales), asi sucesivamente si aparecen numeros como el 2 o el 3 que corresponden a la cantidad de minas.



