# Proyecto de Conversión de Voz a Texto con Vosk

Este proyecto permite convertir audio de voz a texto en tiempo real usando Python, la biblioteca Vosk y un modelo de reconocimiento de voz en español.

## Requisitos

- **Python 3.8 o superior**: Asegúrate de tener Python instalado en tu sistema.
  - Puedes descargarlo desde [Python.org](https://www.python.org/downloads/).
- **pip**: Python Package Installer.
  - Si no tienes `pip`, puedes instalarlo siguiendo las instrucciones [aquí](https://pip.pypa.io/en/stable/installation/).

## Instalación

Sigue estos pasos para instalar todas las dependencias necesarias y configurar el proyecto:

1. **Clona este repositorio** o descarga los archivos manualmente.

   ```bash
   git clone https://github.com/Gatogordo03/Voz-a-Texto.git
   cd Voz-a-Texto
   ```

2. **Instala las dependencias** utilizando el script de instalación incluido. Este script instala las bibliotecas necesarias (`vosk`, `sounddevice`, `scipy`) y descarga el modelo de reconocimiento de voz.

   - **Para usuarios de Windows**:

     - Haz doble clic en el archivo `install_and_run.bat` o ejecútalo desde la terminal.

     ```bash
     install_and_run.bat
     ```

     - El script descargará automáticamente el modelo de reconocimiento de voz y lo descomprimirá.

   - **Para usuarios de Linux o Mac**:

     - Instala manualmente las dependencias con:

     ```bash
     pip install vosk sounddevice scipy
     ```

     - Descarga el modelo de reconocimiento de voz en español desde [este enlace](https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip) y descomprímelo en la carpeta del proyecto.

3. **Configura la ruta del modelo**: En el archivo `prog.py`, asegúrate de que la variable `rutModel` apunte a la carpeta donde está descomprimido el modelo Vosk.

## Uso

Una vez que todo esté instalado y configurado, puedes ejecutar el proyecto para convertir tu voz en texto en tiempo real:

```bash
python prog.py
```

El programa capturará el audio desde tu micrófono y convertirá lo que digas en texto en tiempo real. Los resultados se mostrarán en la terminal.

### Notas Importantes:

- Si tienes problemas con el micrófono, asegúrate de que está correctamente configurado en tu sistema y que es compatible con Python a través de la biblioteca `sounddevice`.
- Si usas Linux, puede que necesites permisos adicionales para acceder al dispositivo de audio. Intenta ejecutar el programa con `sudo` si es necesario.
