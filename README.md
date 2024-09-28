Este es el codigo utilizado para el item 1 del miniproyecto el cual explicare brevemente


Partiendo por las funciones base tenemos a

validacion(m,M,text): Esta funcion esta hecha para que al introducir algun valor a una variable que requiera limite se asegure que el valor introducido este dentro de esos limites establecidos para asi no tener ningun tipo de error en la ejecucion del codigo

apagar_luces() : esta funcion es de las más importantes debido a que es necesario al momento de iniciar cada turno o cada nueva ronda o cada nuevo juego apagar los leds encendidos para que asi no se mezcle ningun color al tener 2 canales de colores combinados

encender_luces_aleatorias() : esta funcion ejecutada al inicio del juego es para representar cuales son las zonas seguras representadas por el led encendido en azul o las de trampa representadas por los led encendidos de rojo

encender_patron(posicion_azul): esta funcion ya es la funcion principal usada en el juego el cual da un patron a seguir para asi el jugador pueda intentar predecir la siguiente luz y acertar.
En este caso el patron elegido es el azul continuo es decir que al inicio de la ronda la luz azul se encuentra en el led 1 (de izquierda a derecha) y cada segundo que pasa el led avanzara de posicion saltando del led 1 al 2 ... al 5


juego(): este es la funcion del juego en si, donde esta contenido los bucles tanto for como while para la ejecucion correcta del juego, inciando por la entrada manual de la cantidad de rondas, luego la cantidad de jugadores y ya al final del juego mostrando la tabla de puntuaciones
y el ganador

