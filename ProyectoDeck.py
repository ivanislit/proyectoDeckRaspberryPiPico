# Importa las librerías necesarias para el proyecto
import time            # Librería para manejar tiempo (retrasos, tiempo actual, etc.)
import board           # Librería específica para Raspberry Pi Pico, maneja los pines de la placa
import digitalio       # Librería para manejar entradas y salidas digitales (como los botones)
import usb_hid         # Librería para la comunicación del dispositivo como un teclado/mouse HID sobre USB
from adafruit_hid.keyboard import Keyboard  # Importa la clase Keyboard para simular presiones de teclado
from adafruit_hid.keycode import Keycode    # Importa Keycode para utilizar códigos de teclas específicas

# Inicializa el teclado (para que el Pico se comporte como un teclado)
keyboard = Keyboard(usb_hid.devices)

# Configuración de los pines para cada botón
# Cambia 'board.GP1', 'board.GP2', etc., por los pines que estés usando en tu Raspberry Pi Pico
btn1 = digitalio.DigitalInOut(board.GP1)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.UP

btn2 = digitalio.DigitalInOut(board.GP2)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.UP

btn3 = digitalio.DigitalInOut(board.GP3)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.UP

btn4 = digitalio.DigitalInOut(board.GP4)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.UP

btn5 = digitalio.DigitalInOut(board.GP5)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.UP

# Tiempo máximo en segundos para considerar dos clics como un doble clic
double_click_timeout = 0.4

# Variables para rastrear el tiempo del último clic para cada botón
last_press_time = [0, 0, 0, 0, 0]

# Variables para indicar si se ha detectado un clic y se está esperando un posible segundo clic
click_detected = [False, False, False, False, False]

def send_key_combination(keys):
    """
    Función para enviar una combinación de teclas.
    :param keys: Una tupla que contiene los códigos de las teclas a presionar.
    """
    keyboard.press(*keys)  # Presiona todas las teclas en la tupla
    time.sleep(0.1)        # Pequeña pausa para asegurar que la combinación se registre
    keyboard.release_all() # Libera todas las teclas

def check_button_press(button):
    """
    Función para comprobar si un botón está siendo presionado.
    :param button: El botón a verificar.
    :return: True si el botón está presionado, False en caso contrario.
    """
    return not button.value  # Retorna True si el botón está presionado

def process_button(button, index, single_click_keys=None, double_click_keys=None, double_click_command=None):
    """
    Función para procesar la lógica de clics simples y dobles para un botón.
    :param button: El botón a procesar.
    :param index: Índice del botón (para usar en las listas de seguimiento).
    :param single_click_keys: Combinación de teclas para un clic simple (opcional).
    :param double_click_keys: Combinación de teclas para un doble clic (opcional).
    :param double_click_command: Comando a ejecutar en un doble clic (opcional).
    """
    current_time = time.monotonic()  # Obtiene el tiempo actual

    if check_button_press(button) and not click_detected[index]:
        click_detected[index] = True
        last_press_time[index] = current_time
        while check_button_press(button):
            pass  # Espera hasta que se suelte el botón

    if click_detected[index] and (current_time - last_press_time[index]) <= double_click_timeout:
        if check_button_press(button):
            if double_click_command:
                subprocess.run(double_click_command, shell=True)
            elif double_click_keys:
                send_key_combination(double_click_keys)
            click_detected[index] = False
            while check_button_press(button):
                pass  # Espera hasta que se suelte el botón
    elif click_detected[index] and (current_time - last_press_time[index]) > double_click_timeout:
        if single_click_keys:
            send_key_combination(single_click_keys)
        click_detected[index] = False

# Bucle principal
while True:
    # Llama a process_button para cada botón con las combinaciones de teclas correspondientes
    # Puedes modificar las combinaciones de teclas en los argumentos o usar None para no asignar ninguna acción
    process_button(btn1, 0, single_click_keys=(Keycode.A,), double_click_keys=(Keycode.B,))
    process_button(btn2, 1, single_click_keys=(Keycode.C,), double_click_keys=(Keycode.D,))
    process_button(btn3, 2, single_click_keys=(Keycode.E,), double_click_keys=(Keycode.F,))
    process_button(btn4, 3, single_click_keys=(Keycode.G,), double_click_keys=(Keycode.H,))
    process_button(btn5, 4, single_click_keys=(Keycode.I,), double_click_keys=(Keycode.J,))

    time.sleep(0.01)  # Pequeño retraso para el bucle
    
# Tiempo máximo en segundos para considerar dos clics como un doble clic
double_click_timeout = 0.4

# Variables para rastrear el tiempo del último clic para cada botón
last_press_time = [0, 0, 0, 0, 0]

# Variables para indicar si se ha detectado un clic y se está esperando un posible segundo clic
click_detected = [False, False, False, False, False]

def send_key_combination(keys):
    """
    Función para enviar una combinación de teclas.
    :param keys: Una tupla que contiene los códigos de las teclas a presionar.
    """
    keyboard.press(*keys)  # Presiona todas las teclas en la tupla
    time.sleep(0.1)        # Pequeña pausa para asegurar que la combinación se registre
    keyboard.release_all() # Libera todas las teclas

def check_button_press(button):
    """
    Función para comprobar si un botón está siendo presionado.
    :param button: El botón a verificar.
    :return: True si el botón está presionado, False en caso contrario.
    """
    return not button.value  # Retorna True si el botón está presionado

def process_button(button, index, single_click_keys=None, double_click_keys=None, double_click_command=None):
    """
    Función para procesar la lógica de clics simples y dobles para un botón.
    :param button: El botón a procesar.
    :param index: Índice del botón (para usar en las listas de seguimiento).
    :param single_click_keys: Combinación de teclas para un clic simple (opcional).
    :param double_click_keys: Combinación de teclas para un doble clic (opcional).
    :param double_click_command: Comando a ejecutar en un doble clic (opcional).
    """
    current_time = time.monotonic()  # Obtiene el tiempo actual

    if check_button_press(button) and not click_detected[index]:
        click_detected[index] = True
        last_press_time[index] = current_time
        while check_button_press(button):
            pass  # Espera hasta que se suelte el botón

    if click_detected[index] and (current_time - last_press_time[index]) <= double_click_timeout:
        if check_button_press(button):
            if double_click_command:
                subprocess.run(double_click_command, shell=True)
            elif double_click_keys:
                send_key_combination(double_click_keys)
            click_detected[index] = False
            while check_button_press(button):
                pass  # Espera hasta que se suelte el botón
    elif click_detected[index] and (current_time - last_press_time[index]) > double_click_timeout:
        if single_click_keys:
            send_key_combination(single_click_keys)
        click_detected[index] = False

# Bucle principal
while True:
    # Llama a process_button para cada botón con las combinaciones de teclas correspondientes
    # Puedes modificar las combinaciones de teclas en los argumentos o usar None para no asignar ninguna acción
    process_button(btn1, 0, single_click_keys=(Keycode.A,), double_click_keys=(Keycode.B,))
    process_button(btn2, 1, single_click_keys=(Keycode.C,), double_click_keys=(Keycode.D,))
    process_button(btn3, 2, single_click_keys=(Keycode.E,), double_click_keys=(Keycode.F,))
    process_button(btn4, 3, single_click_keys=(Keycode.G,), double_click_keys=(Keycode.H,))
    process_button(btn5, 4, single_click_keys=(Keycode.I,), double_click_keys=(Keycode.J,))

    time.sleep(0.01)  # Pequeño retraso para el bucle
