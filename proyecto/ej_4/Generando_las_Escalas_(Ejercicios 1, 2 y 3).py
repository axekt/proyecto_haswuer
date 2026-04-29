import wave
import struct
import math

# Diccionario con las frecuencias de cada nota
frecuencias = {
    'Do': 261.63, 'Re': 293.66, 'Mi': 329.63, 'Fa': 349.23, 
    'Sol': 392.00, 'La': 440.00, 'Si': 493.88
}

def generar_escala(nombre_archivo, notas, rate, canales):
    # Abrimos el archivo wav en modo escritura ('w')
    archivo = wave.open(nombre_archivo, 'w')
    archivo.setnchannels(canales) # 1 para Mono, 2 para Stereo
    archivo.setsampwidth(2)       # 2 bytes = 16 bits
    archivo.setframerate(rate)

    amplitud = 32767.0 / 2.0 # Mitad del volumen máximo de 16-bits para no saturar

    for nota in notas:
        frecuencia = frecuencias[nota]
        # Generamos 1 segundo exacto de audio por nota
        num_muestras = rate * 1 
        
        for i in range(num_muestras):
            # Formula de la onda: A * sin(2 * pi * f * t)
            # donde t = i / rate
            valor = int(amplitud * math.sin(2 * math.pi * frecuencia * (i / rate)))
            
            if canales == 1:
                # Empaquetar 16-bits (Mono)
                data = struct.pack('<h', valor)
            else:
                # Empaquetar 16-bits x2 (Stereo: canal izquierdo y derecho iguales)
                data = struct.pack('<hh', valor, valor)
                
            archivo.writeframesraw(data)
            
    archivo.close()
    print(f"Generado: {nombre_archivo}")

# Resolviendo el Ejercicio 1
generar_escala('escala_1_44100_mono.wav', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'], 44100, 1)

# Resolviendo el Ejercicio 2
generar_escala('escala_2_22050_stereo.wav', ['Si', 'La', 'Sol', 'Fa', 'Mi', 'Re', 'Do'], 22050, 2)

# Resolviendo el Ejercicio 3
generar_escala('escala_3_8000_mono.wav', ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Si'], 8000, 1)