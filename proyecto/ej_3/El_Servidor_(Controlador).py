import serial
import win32api
import win32con
import time

# Configuración del puerto serial (ajusta el COM según VSPE)
ser = serial.Serial('COM2', 9600, timeout=1)

def press_key(vk_code):
    # Simula presionar la tecla
    win32api.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.05)
    # Simula soltar la tecla
    win32api.keybd_event(vk_code, 0, win32con.KEYEVENTF_KEYUP, 0)

print("Servidor listo. Esperando comandos...")

# ... (resto del código igual arriba)

try:
    while True:
        if ser.in_waiting > 0:
            comando = ser.readline().decode('utf-8').strip().lower()
            
            if comando == "play":
                # Simula CTRL + SPACE (como tienes en tu captura)
                win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
                win32api.keybd_event(win32con.VK_SPACE, 0, 0, 0)
                time.sleep(0.05)
                win32api.keybd_event(win32con.VK_SPACE, 0, win32con.KEYEVENTF_KEYUP, 0)
                win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)

            elif comando == "next":
                # VK_RIGHT es la flecha derecha (Next en tu AIMP)
                press_key(win32con.VK_RIGHT)

            elif comando == "prev":
                # VK_LEFT es la flecha izquierda (Prev en tu AIMP)
                press_key(win32con.VK_LEFT)

            elif comando == "volup":
                # F12 no escribe texto en la terminal
                press_key(win32con.VK_F12)

            elif comando == "voldown":
                # F10 no escribe texto en la terminal
                press_key(win32con.VK_F10)
            
            elif comando == "stop":
                # VK_DELETE es la tecla suprimir (como tienes en tu captura)
                press_key(win32con.VK_DELETE)
# ...
except KeyboardInterrupt:
    ser.close()