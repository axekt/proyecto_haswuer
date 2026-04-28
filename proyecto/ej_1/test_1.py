import numpy as np, matplotlib.pyplot as plt

FREQ_0 = 1000 #frecuencia main

FREQ_1 = 50 #frecuencia ruido

SAMPLE = 44100 #muestras por segundo

S_RATE = 44100.0 #tasa de muestreo

S_1 = [np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)] # 1000 senos c/1s
S_2 = [np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)] # 50 senos c/1s
W_1 = np.array(S_1)  ;  W_2 = np.array(S_2)   #lista 2 array
W12 = W_1 + W_2 #sumamos 2 ondas


"""este codigo se debe calcular
fft (fft es la transformada rapida de fourier, la cual es un algoritmo extremadamente eficiente
para calcular la tranformada Discreta de Fourier (DFT) y su inversa.
Convierte señales de dominio del tiempo(u osciloscopio) al dominio de la frecuencia (espectro)  
permitiendo descomponer formas de onda complejas en sus frecuencias constituyentes) )


Ademas no se grafica debido a que falta ocupar  matplotlib.pyplot para poder graficar
ahora en el sig coddigo se muestra como deberia quedar"""