import numpy as np, matplotlib.pyplot as plt

FREQ_0 = 1000
FREQ_1 = 50
SAMPLE = 44100
S_RATE = 44100.0

S_1 = [np.sin(2*np.pi * FREQ_0 * i/S_RATE) for i in range(SAMPLE)]
S_2 = [np.sin(2*np.pi * FREQ_1 * i/S_RATE) for i in range(SAMPLE)]
W_1 = np.array(S_1)
W_2 = np.array(S_2)
W12 = W_1 + W_2

# La FFT (Transformada Rápida de Fourier) convierte la señal del dominio del tiempo
# al dominio de la frecuencia, permitiendo identificar qué frecuencias componen la onda.
FFT_W12 = np.fft.fft(W12)
FREQ = np.fft.fftfreq(len(W12), 1/S_RATE)

# Crear una figura con 4 subgráficas para visualizar las ondas y su espectro de frecuencias.
fig, axes = plt.subplots(2, 2, figsize=(14, 8))

# Gráfica 1: Onda Original
axes[0, 0].plot(W_1[:500])
axes[0, 0].set_title('Onda Original', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('Amplitud')
axes[0, 0].set_xlabel('Muestras')
axes[0, 0].set_xlim(0, 500)
axes[0, 0].grid(True, alpha=0.3)

# Gráfica 2: Onda Ruido
axes[0, 1].plot(W_2[:4000])
axes[0, 1].set_title('Onda Ruido', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Amplitud')
axes[0, 1].set_xlabel('Muestras')
axes[0, 1].set_xlim(0, 4000)
axes[0, 1].grid(True, alpha=0.3)

# Gráfica 3: Onda Original + Ruidosa
axes[1, 0].plot(W12[:3000])
axes[1, 0].set_title('Onda Original + Ruidosa', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Amplitud')
axes[1, 0].set_xlabel('Muestras')
axes[1, 0].set_xlim(0, 3000)
axes[1, 0].grid(True, alpha=0.3)

# Gráfica 4: Frecuencias (FFT)
freq_limit = 1200
freq_idx = np.where(FREQ[:len(FREQ)//2] <= freq_limit)[0]
axes[1, 1].plot(FREQ[freq_idx], np.abs(FFT_W12)[freq_idx])
axes[1, 1].set_title('Frecuencias en las Ondas (FFT)', fontsize=12, fontweight='bold')
axes[1, 1].set_ylabel('Magnitud')
axes[1, 1].set_xlabel('Frecuencia (Hz)')
axes[1, 1].set_xlim(0, freq_limit)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()