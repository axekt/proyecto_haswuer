import wave
import struct
import math

rate = 44100
duracion = 10 # 10 segundos

# --- EJERCICIO 4: Generar onda compleja ---
archivo_4 = wave.open('ejercicio_4_onda_compleja.wav', 'w')
archivo_4.setnchannels(2) # Stereo
archivo_4.setsampwidth(2)
archivo_4.setframerate(rate)

for i in range(rate * duracion):
    # La fórmula exacta del enunciado
    y = int(8000 * math.sin(2 * math.pi * 500.0 / rate * i) + 8000 * math.sin(2 * math.pi * 250.0 / rate * i))
    
    # Stereo: ponemos la misma onda combinada en ambos canales
    data = struct.pack('<hh', y, y)
    archivo_4.writeframesraw(data)
archivo_4.close()
print("Generado: ejercicio_4_onda_compleja.wav")


# --- EJERCICIO 5: Bajar volumen en un 75% ---
# Abrimos el original para leer ('r') y uno nuevo para escribir ('w')
wav_in = wave.open('ejercicio_4_onda_compleja.wav', 'r')
wav_out = wave.open('ejercicio_5_volumen_bajo.wav', 'w')
wav_out.setparams(wav_in.getparams()) # Copiamos los parámetros

num_frames = wav_in.getnframes()

for _ in range(num_frames):
    # Leemos 1 frame (que son 4 bytes en estéreo de 16-bit: 2 bytes L + 2 bytes R)
    frame_bytes = wav_in.readframes(1)
    
    # Desempaquetamos (unpack) los bytes crudos a dos números enteros
    val_L, val_R = struct.unpack('<hh', frame_bytes)
    
    # Bajar volumen 75% significa que nos quedamos con el 25% de la amplitud original
    nuevo_L = int(val_L * 0.25)
    nuevo_R = int(val_R * 0.25)
    
    # Volvemos a empaquetar y escribir
    wav_out.writeframes(struct.pack('<hh', nuevo_L, nuevo_R))

wav_in.close()
wav_out.close()
print("Generado: ejercicio_5_volumen_bajo.wav")


# --- EJERCICIO 6: Limpiar canal izquierdo ---
wav_in2 = wave.open('ejercicio_4_onda_compleja.wav', 'r')
wav_out2 = wave.open('ejercicio_6_limpia_izquierdo.wav', 'w')
wav_out2.setparams(wav_in2.getparams())

for _ in range(num_frames):
    frame_bytes = wav_in2.readframes(1)
    val_L, val_R = struct.unpack('<hh', frame_bytes)
    
    # Limpiamos (muteamos) el canal izquierdo forzando su valor a 0
    nuevo_L = 0 
    
    wav_out2.writeframes(struct.pack('<hh', nuevo_L, val_R))

wav_in2.close()
wav_out2.close()
print("Generado: ejercicio_6_limpia_izquierdo.wav")