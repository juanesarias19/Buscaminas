# Buscaminas
# Proyecto de programación sobre el desarrollo de un Buscaminas 
El grupo stravanzza presenta el primer avance de su proyecto, el desarrollo de un Buscaminas en python.
### ¿Como se abordo la solucion de crear un buscaminas en python?
Para empezar el funcionamiento de un buscaminas se relaciona con el tema de las matrices en python, para jugar un buscaminas es necesario tener una interfaz con forma de bloque que contenga filas y columnas, en estas se encuentran unas minas. El sentido del juego es que el jugador no sabe las posciones de las minas, asi que tiene que ir ingresando posiciones para ir descubriendo las minas, a medida que avanza si se situa en una mina, el jugador pierde, si se situa en un lugar donde no hay minas se deben descubrir la cercania de las otras minas, es decir, en la cuadricula deben aparecer al rededor de la mina unos numeros que indican la cercania de la misma, si es un 1 quiere decir que esta muy cerca por lo que el jugador deberia evitar posicionarse cerca de ese 1, si es un 2 esta un poco lejos y si es 3 aun mas lejos.

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2uE_vmb6-A35XfltEbnAQyrvBcCbxBP3Y4A&amp;s" class="sFlh5c ag2Pqd FyHeAf" alt="Matriz (matemática) - Wikipedia, la enciclopedia libre" jsname="JuXqh" style="max-width: 289px; height: 121px; margin: 0px; width: 294px;" data-ilt="1737912611237">

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjOfzBotH4-IRrdFuVo6b26aQkILLBjE4V2azlz3-Q-yVGHJioO8rgRfn9KgsdN-w9CLOPtgLFRGBc-IoX2T3sPkSTdfRZNUu7kSSG_vyxnylWcznWbMcZPY6s83WUT-KZS-vo5/s0/buscaminas.png" jsaction="" class="sFlh5c FyHeAf iPVvYb" style="max-width: 161px; height: 202px; margin: 0px; width: 159px;" alt="Vagabundia: Buscaminas" jsname="kn3ccd" aria-hidden="false">
