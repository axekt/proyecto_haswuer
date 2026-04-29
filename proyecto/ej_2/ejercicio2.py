import numpy as np
import matplotlib.pyplot as plt

# 1. Configuración de parámetros
Sample = 200
t = np.arange(Sample)

# 2. Creación de las ondas base (Ajustadas para que coincidan con la imagen)
# w_fast: para los picos rápidos
# w_med: para la interferencia en Signal 1
# w_slow: para la curva suave en Signal 2 y 3
w_fast = 5 * np.sin(2 * np.pi * 0.25 * t) 
w_med = 2 * np.sin(2 * np.pi * 0.1 * t)
w_slow = 10 * np.sin(2 * np.pi * 0.005 * t)

# 3. Composición de las Señales (As)
# Signal 1: Suma de ondas rápidas (rango +-6)
# Signal 2: Onda lenta + picos (rango +-15)
# Signal 3: Modulación/Multiplicación (rango +-30)
As = [
    (w_fast + w_med),
    (w_slow + (w_fast * 0.6)),
    (w_slow * (w_fast * 0.5))
]

# 4. Función para filtrar la señal (Filtro Paso Bajo Simple)
def filter_comp(aV, nA):
    aF = np.zeros(len(aV))
    aF[0] = aV[0]
    for i in range(1, len(aV)):
        aF[i] = nA * aV[i] + (1.0 - nA) * aF[i-1]
    return aF

# 5. Aplicar el filtro a las señales
# Ajustamos nA para que la línea roja sea más o menos suave según la foto
f1 = filter_comp(As[0], 0.3)
f2 = filter_comp(As[2], 0.05)
f3 = filter_comp(As[2], 0.1)

# 6. Creación de la figura y gráficas
plt.figure(figsize=(10, 8))

# Gráfico de la Señal 1
plt.subplot(3, 1, 1)
plt.plot(As[0], 'b', linewidth=1) # Original azul
plt.plot(f1, 'r', linewidth=1)    # Filtrada roja
plt.title("Signal 1")
plt.xlim(0, 200)
plt.ylim(-6, 6)

# Gráfico de la Señal 2
plt.subplot(3, 1, 2)
plt.plot(As[1], 'b', linewidth=1)
plt.plot(f2, 'r', linewidth=1)
plt.title("Signal 2")
plt.xlim(0, 200)
plt.ylim(-15, 15)

# Gráfico de la Señal 3
plt.subplot(3, 1, 3)
plt.plot(As[2], 'b', linewidth=1)
plt.plot(f3, 'r', linewidth=1)
plt.title("Signal 3")
plt.xlim(0, 200)
plt.ylim(-30, 30)

# Ajuste estético final
plt.tight_layout()
plt.show()