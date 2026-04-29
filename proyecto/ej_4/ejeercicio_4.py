import wave
import struct
import math

# Configuración básica
NOTAS = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88] # Do a Si
DURACION = 1  # segundo por nota
AMPLITUD = 16000 # Volumen moderado (máximo es 32767 para 16 bits)

def generar_onda(frecuencia, rate, duracion, amplitud=AMPLITUD):
    n_samples = int(rate * duracion)
    # Generamos los valores de la onda senoidal
    return [int(amplitud * math.sin(2 * math.pi * frecuencia * i / rate)) for i in range(n_samples)]

def guardar_wav(nombre, data, rate, n_channels):
    with wave.open(nombre, 'w') as f:
        f.setnchannels(n_channels)
        f.setsampwidth(2) # 2 bytes = 16 bits
        f.setframerate(rate)
        for frame in data:
            # 'h' es para signed short (16-bit)
            f.writeframes(struct.pack('h', frame))

# --- EJECUCIÓN DE LAS TAREAS ---

# 1. Escala Mono 44.1kHz
data1 = []
for f in NOTAS: data1.extend(generar_onda(f, 44100, DURACION))
guardar_wav('1_escala_44100_mono.wav', data1, 44100, 1)

# 2. Escala Inversa Stereo 22.05kHz
data2 = []
for f in reversed(NOTAS):
    onda = generar_onda(f, 22050, DURACION)
    for sample in onda:
        data2.append(sample) # Canal Izquierdo
        data2.append(sample) # Canal Derecho
guardar_wav('2_escala_22050_stereo.wav', data2, 22050, 2)

# 3. Escala Mono 8kHz
data3 = []
for f in NOTAS: data3.extend(generar_onda(f, 8000, DURACION))
guardar_wav('3_escala_8000_mono.wav', data3, 8000, 1)

# 4. Onda Combinada Stereo 44.1kHz (10 segundos)
rate_4 = 44100
data4 = []
for i in range(rate_4 * 10):
    # Fórmula: y = 8000*sin(...) + 8000*sin(...)
    val = int(8000 * math.sin(2 * math.pi * 500.0 / rate_4 * i) + 
              8000 * math.sin(2 * math.pi * 250.0 / rate_4 * i))
    data4.append(val) # L
    data4.append(val) # R
guardar_wav('4_onda_combinada.wav', data4, rate_4, 2)

# 5. Bajar volumen al 75% (Multiplicar por 0.25)
data5 = [int(sample * 0.25) for sample in data4]
guardar_wav('5_volumen_bajo.wav', data5, rate_4, 2)

# 6. Limpiar canal izquierdo (Poner L a 0)
data6 = []
for i in range(0, len(data5), 2):
    data6.append(0)          # Canal Izquierdo silencio
    data6.append(data5[i+1]) # Canal Derecho se mantiene
guardar_wav('6_limpiar_izquierdo.wav', data6, rate_4, 2)

print("Archivos generados con éxito.")