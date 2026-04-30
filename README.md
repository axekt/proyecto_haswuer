# Proyecto de Hardware y Señales

Este proyecto contiene una colección de scripts de Python que exploran la generación y manipulación de señales de audio, el análisis de frecuencias mediante FFT y el control de aplicaciones a través de puertos serie virtuales.

## Contenido del Proyecto

El proyecto está dividido en cuatro ejercicios principales:

### Ejercicio 1: Análisis de Señales con FFT
- **Ubicación:** `proyecto/ej_1/`
- **Descripción:** Scripts que demuestran cómo una señal de audio puede ser contaminada con ruido y cómo la Transformada Rápida de Fourier (FFT) puede ser utilizada para identificar las frecuencias originales.
- **Archivos:**
    - `test_1.py`: Define y combina una señal principal con una señal de ruido.
    - `test2.py`: Visualiza las señales (original, ruido, combinada) y su espectro de frecuencias (FFT).
    - `from pptx import Presentation.py`: Genera una presentación de PowerPoint que explica el proceso.

### Ejercicio 2: Filtrado de Señales
- **Ubicación:** `proyecto/ej_2/`
- **Descripción:** Script que crea varias señales complejas y les aplica un filtro de paso bajo para suavizarlas.
- **Archivos:**
    - `ejercicio2.py`: Genera, filtra y visualiza tres tipos de señales compuestas.

### Ejercicio 3: Control Remoto por Puerto Serie
- **Ubicación:** `proyecto/ej_3/`
- **Descripción:** Un par de scripts que simulan un control remoto. Un cliente envía comandos a través de un puerto serie virtual y un servidor los recibe para controlar un reproductor de música (como AIMP) mediante la simulación de pulsaciones de teclas.
- **Archivos:**
    - `El_Cliente_(Emisor).py`: Envía los comandos.
    - `El_Servidor_(Controlador).py`: Recibe los comandos y simula las teclas.

### Ejercicio 4: Generación y Manipulación de Archivos WAV
- **Ubicación:** `proyecto/ej_4/`
- **Descripción:** Scripts para generar archivos de audio `.wav` con escalas musicales y ondas complejas, y para manipular sus propiedades como el volumen y los canales de audio.
- **Archivos:**
    - `Generando_las_Escalas_(Ejercicios 1, 2 y 3).py`: Crea archivos `.wav` de escalas musicales.
    - `Ondas_Complejas_y_Manipulación_de_Bits_(Ejercicios 4, 5 y 6).py`: Genera una onda compleja y luego la modifica para crear nuevas versiones (volumen reducido, canal silenciado).

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instalado lo siguiente:

1.  **Python 3:** La mayoría de los scripts requieren Python para ejecutarse.
2.  **Librerías de Python:** Instala las dependencias necesarias:
    ```bash
    pip install numpy matplotlib pyserial pywin32 python-pptx
    ```
3.  **VSPE (Virtual Serial Ports Emulator):** Para el Ejercicio 3, necesitas VSPE para crear un par de puertos COM virtuales (por ejemplo, COM1 y COM2).
4.  **AIMP (o un reproductor similar):** Para el Ejercicio 3, se necesita un reproductor de música donde puedas configurar los siguientes atajos de teclado:
    - **Play/Pause:** `Ctrl + Espacio`
    - **Next:** `Flecha Derecha`
    - **Previous:** `Flecha Izquierda`
    - **Volume Up:** `F8`
    - **Volume Down:** `F9`
    - **Stop:** `Supr`
5.  **Audacity:** Recomendado para visualizar y analizar los archivos `.wav` generados en el Ejercicio 4.

## Instrucciones de Uso

1.  **Clona o descarga el repositorio.**
2.  **Instala los requisitos previos** mencionados anteriormente.
3.  **Para el Ejercicio 3:**
    - Inicia VSPE y crea un par de conectores (por ejemplo, COM1 y COM2).
    - Ejecuta `El_Servidor_(Controlador).py`.
    - Abre AIMP y asegúrate de que los atajos de teclado estén configurados.
    - Ejecuta `El_Cliente_(Emisor).py` y escribe los comandos (`play`, `next`, `stop`, etc.) en la terminal.
4.  **Para los otros ejercicios:**
    - Navega a la carpeta del ejercicio correspondiente (`ej_1`, `ej_2`, `ej_4`).
    - Ejecuta los scripts de Python directamente desde tu terminal (por ejemplo, `python test2.py`).