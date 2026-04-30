# Proyecto de Hardware y Señales

Este proyecto contiene una colección de scripts de Python que exploran la generación, manipulación y análisis de señales de audio, así como el control de aplicaciones mediante puertos serie virtuales.

## Estructura del Proyecto

El proyecto se organiza en cuatro carpetas, cada una correspondiente a un ejercicio específico:

- **`proyecto/ej_1/`**: Análisis de señales y Transformada Rápida de Fourier (FFT).
- **`proyecto/ej_2/`**: Filtrado de señales complejas.
- **`proyecto/ej_3/`**: Control remoto de un reproductor de música a través de un puerto serie virtual.
- **`proyecto/ej_4/`**: Generación y manipulación de archivos de audio `.wav`.

## Contenido del Proyecto

### Ejercicio 1: Análisis de Señales con FFT

- **Ubicación:** `proyecto/ej_1/`
- **Descripción:** Este ejercicio demuestra cómo una señal de audio puede ser "contaminada" con ruido y cómo la Transformada Rápida de Fourier (FFT) se puede utilizar para identificar las frecuencias originales presentes en la señal.
- **Archivos:**
    - `test2.py`: Genera una señal principal y una señal de ruido, las combina y luego visualiza las tres señales (original, ruido y combinada) junto con su espectro de frecuencias (FFT).

### Ejercicio 2: Filtrado de Señales

- **Ubicación:** `proyecto/ej_2/`
- **Descripción:** Este script crea varias señales complejas mediante la combinación de ondas senoidales de diferentes frecuencias y amplitudes. Luego, aplica un filtro de paso bajo para suavizar las señales, demostrando un método básico de filtrado.
- **Archivos:**
    - `ejercicio2.py`: Genera, filtra y visualiza tres tipos de señales compuestas, mostrando la señal original y la señal filtrada en un gráfico.

### Ejercicio 3: Control Remoto por Puerto Serie

- **Ubicación:** `proyecto/ej_3/`
- **Descripción:** Este ejercicio simula un sistema de control remoto. Un script "cliente" envía comandos a través de un puerto serie virtual, y un script "servidor" los recibe para controlar un reproductor de música (como AIMP) mediante la simulación de pulsaciones de teclas.
- **Archivos:**
    - `El_Cliente_(Emisor).py`: Envía comandos como `play`, `next`, `stop`, etc., a través de un puerto serie virtual (por ejemplo, COM1).
    - `El_Servidor_(Controlador).py`: Escucha en otro puerto serie virtual (por ejemplo, COM2), recibe los comandos y simula las pulsaciones de teclas correspondientes para controlar el reproductor de música.

### Ejercicio 4: Generación y Manipulación de Archivos WAV

- **Ubicación:** `proyecto/ej_4/`
- **Descripción:** Estos scripts se centran en la generación de archivos de audio `.wav` con escalas musicales y ondas complejas, así como en la manipulación de sus propiedades, como el volumen y los canales de audio.
- **Archivos:**
    - `Generando_las_Escalas_(Ejercicios 1, 2 y 3).py`: Crea tres archivos `.wav` de escalas musicales con diferentes configuraciones (mono, estéreo, y distintas tasas de muestreo).
    - `Ondas_Complejas_y_Manipulación_de_Bits_(Ejercicios 4, 5 y 6).py`: Genera una onda compleja y luego la modifica para crear nuevas versiones con el volumen reducido y un canal de audio silenciado.
    - `ejeercicio_4.py`: Una versión alternativa que combina la generación de escalas y ondas complejas en un solo script.

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instalado lo siguiente:

1.  **Python 3:** La mayoría de los scripts requieren Python para ejecutarse.
2.  **Librerías de Python:** Instala las dependencias necesarias:
    ```bash
    pip install numpy matplotlib pyserial pywin32
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

### Cómo ejecutar los scripts

- **Ejercicio 1:**
  ```bash
  python proyecto/ej_1/test2.py
  ```

- **Ejercicio 2:**
  ```bash
  python proyecto/ej_2/ejercicio2.py
  ```

- **Ejercicio 3:**
    1.  Inicia VSPE y crea un par de conectores (por ejemplo, COM1 y COM2).
    2.  Ejecuta el script del servidor:
        ```bash
        python proyecto/ej_3/El_Servidor_(Controlador).py
        ```
    3.  Abre AIMP y asegúrate de que los atajos de teclado estén configurados.
    4.  Ejecuta el script del cliente en otra terminal y escribe los comandos (`play`, `next`, `stop`, etc.):
        ```bash
        python proyecto/ej_3/El_Cliente_(Emisor).py
        ```

- **Ejercicio 4:**
  ```bash
  python "proyecto/ej_4/Generando_las_Escalas_(Ejercicios 1, 2 y 3).py"
  python "proyecto/ej_4/Ondas_Complejas_y_Manipulación_de_Bits_(Ejercicios 4, 5 y 6).py"
  ```
  Luego, puedes abrir los archivos `.wav` generados con un reproductor de audio o Audacity para verificar los resultados.