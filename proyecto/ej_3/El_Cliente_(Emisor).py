import serial

# Se conecta al otro extremo del par creado en VSPE
client_ser = serial.Serial('COM1', 9600)

def enviar_comando():
    print("Comandos: play, next, prev, volup, voldown, exit")
    while True:
        cmd = input("Ingrese comando >> ")
        if cmd == "exit":
            break
        client_ser.write(f"{cmd}\n".encode('utf-8'))

enviar_comando()
client_ser.close()