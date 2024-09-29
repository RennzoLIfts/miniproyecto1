Este es el codigo utilizado para el item 1 del miniproyecto el cual explicare brevemente

Partiendo por las Funciones Base tenemos a

validacion(m,M,text): Esta función se utiliza para asegurar que, al introducir un valor en una variable con límites definidos, dicho valor se mantenga dentro de los rangos establecidos. De esta manera, se evita cualquier tipo de error durante la ejecución del código.

apagar_luces() : Esta es una de las funciones más importantes, ya que se debe ejecutar al inicio de cada turno, ronda o juego. Su propósito es apagar todos los LEDs encendidos para evitar la mezcla de colores, lo cual podría generar confusión al tener dos canales de colores combinados.

encender_luces_aleatorias() : Esta función se ejecuta al inicio del juego para indicar cuáles son las zonas seguras y las zonas de trampa. Las zonas seguras están representadas por LEDs azules, mientras que las trampas están indicadas por LEDs rojos.

encender_patron(posicion_azul): Esta es la función principal del juego, encargada de establecer un patrón que el jugador debe seguir. El patrón elegido es una secuencia continua de luz azul, que comienza en el LED 1 (de izquierda a derecha). Cada segundo, la luz azul avanza de posición, moviéndose desde el LED 1 hasta el LED 5, en orden sucesivo.

juego(): Esta es la función que contiene la lógica del juego. En ella se implementan los bucles for y while necesarios para su correcta ejecución. El juego inicia con la entrada manual de la cantidad de rondas y jugadores. Al finalizar, se muestra la tabla de puntuaciones y se anuncia al ganador.

https://youtube.com/shorts/Oi-R_xGfQys
https://youtu.be/7WSHcyi-2Mg
