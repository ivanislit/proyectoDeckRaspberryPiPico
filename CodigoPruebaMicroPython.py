# Código Prueba MicroPython (Configurado para 3 botones)

from machine import Pin
import utime

# Configura los pines GP1, GP2 y GP3 como entradas con pull-up (Ajustar puertos GP a sus necesidades).
button1 = Pin(1, Pin.IN, Pin.PULL_UP) # Se sustituye únicamente el número por el número correspondiente al GP, no al pin.
button2 = Pin(2, Pin.IN, Pin.PULL_UP)
button3 = Pin(3, Pin.IN, Pin.PULL_UP)

prev_value1 = button1.value()
prev_value2 = button2.value()
prev_value3 = button3.value()

while True:
    # Lee los estados actuales de los botones
    value1 = button1.value()
    value2 = button2.value()
    value3 = button3.value()

    # Comprueba si ha habido un cambio en el estado de alguno de los botones
    if value1 != prev_value1:
        if value1 == 0:
            print("Botón 1 presionado")
        else:
            print("Botón 1 liberado")
        prev_value1 = value1

    if value2 != prev_value2:
        if value2 == 0:
            print("Botón 2 presionado")
        else:
            print("Botón 2 liberado")
        prev_value2 = value2

    if value3 != prev_value3:
        if value3 == 0:
            print("Botón 3 presionado")
        else:
            print("Botón 3 liberado")
        prev_value3 = value3
    
    # Espera un poco antes de leer los estados de los botones nuevamente
    utime.sleep(0.1)
