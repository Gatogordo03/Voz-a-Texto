@echo off
REM Verificar si Python está instalado
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python no está instalado. Por favor, instala Python y asegúrate de que esté en la variable de entorno PATH.
    pause
    exit /b
)

REM Actualizar pip
echo Actualizando pip...
python -m pip install --upgrade pip

REM Instalar las dependencias necesarias
echo Instalando dependencias...
pip install vosk sounddevice scipy

REM Descargar el modelo de Vosk en español (puede tardar unos minutos)
echo Descargando el modelo de Vosk en español...
curl -L -o vosk-model.zip https://alphacephei.com/vosk/models/vosk-model-small-es-0.42.zip

echo Descomprimiendo el modelo...
powershell -Command "Expand-Archive -Path vosk-model.zip -DestinationPath vosk-model"

REM Eliminar el archivo ZIP después de descomprimirlo
del vosk-model.zip

REM Ejecutar el script de Python
echo Ejecutando el reconocimiento de voz...
python prueba2.py

pause
