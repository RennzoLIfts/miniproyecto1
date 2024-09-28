
from gpiozero import LED, Button, Buzzer
import time
import random


def apagar_luces():
    for led in leds:
        led['azul'].off()
        led['rojo'].off()


def encender_patron(posicion_azul):

    apagar_luces()

    for i, led in enumerate(leds):
        if i == posicion_azul:
            led['azul'].on()
        else:
            led['rojo'].on()


def encender_luces_aleatorias():

    inicio_aleatorio = time.time()
    duracion_aleatoria = 3

    while time.time() - inicio_aleatorio < duracion_aleatoria:

        apagar_luces()

        led_random = random.choice(leds)
        if random.choice([True, False]):
            led_random['azul'].on()
        else:
            led_random['rojo'].on()

        end_time = time.time() + 0.5
        while time.time() < end_time:
            pass

    apagar_luces()


def validacion(minimo, maximo, text):
    x = int(input(f'{text}'))
    while x < minimo or x > maximo:
        print('Valor fuera del rango dado, Intente nuevamente')
        x = int(input(f'{text}'))
    return x


def juego():
    encender_luces_aleatorias()  
    print('Bienvenido al juego, seleccionar número de rondas!')

    rondas = validacion(2, 10, 'Ingrese cantidad de rondas a jugar: ')

    print('Bien! Ahora ingrese cuantos jugadores hay: ')

    jugadores = validacion(1, float('inf'), 'Ingrese cantidad de jugadores: ')

    puntajes = {f'Jugador {i+1}': 10 for i in range(jugadores)}

    for ronda in range(rondas):
        print(f'----- Ronda {ronda+1} -----')

        for turno in range(jugadores):
            inicio_turno = time.time()
            duracion_turno = 10  

            posicion_azul = 0  

            while time.time() - inicio_turno < duracion_turno:
                
                encender_patron(posicion_azul)

                
                for i, boton in enumerate(botones):
                    if boton.is_pressed:  
                        if leds[i]['azul'].is_lit:  
                            print(
                                f"Jugador {turno + 1} acertó con el LED {i + 1}!")
                            puntajes[f'Jugador {turno + 1}'] += 1
                            
                            buzzer.beep(on_time=0.1, n=1)
                        else:  
                            print(
                                f"Jugador {turno + 1} falló con el LED {i + 1}!")
                            puntajes[f'Jugador {turno + 1}'] -= 1
                            
                            buzzer.beep(on_time=0.3, n=1)

                
                time.sleep(0.5)

                
                posicion_azul = (posicion_azul + 1) % len(leds)

            else:
                
                print(
                    f"Jugador {turno + 1} no presionó a tiempo, pierde un punto!")
                puntajes[f'Jugador {turno + 1}'] -= 1

        apagar_luces()  

    
    print("\n--- Fin del juego ---")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje} puntos")

    ganador = max(puntajes, key=puntajes.get)
    print(f"El ganador es {ganador} con {puntajes[ganador]} puntos!")
    buzzer.beep(on_time=0.1, n=5)  


leds = [
    {'azul': LED(20), 'rojo': LED(21)},
    {'azul': LED(26), 'rojo': LED(19)},
    {'azul': LED(16), 'rojo': LED(13)},
    {'azul': LED(6),  'rojo': LED(12)},
    {'azul': LED(22), 'rojo': LED(23)}]


botones = [
    Button(24),
    Button(27),
    Button(17),
    Button(18),
    Button(4)]

buzzer = Buzzer(5)

juego()
