import sounddevice as sd
import queue
import vosk
import sys
import json

# Cargar el modelo de Vosk (asegúrate de proporcionar la ruta correcta donde tengas tu modelo de Vosk)
rutModel = r'C:\Users\edson\Downloads\model-es-0.42'
model = vosk.Model(rutModel)

# Crea una cola donde estan los registros de audio
q = queue.Queue()

# Funcion que se ejecuta cuando se captura audio
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

# Configura la entrada de audio en tiempo real
with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=callback):
    print('# Grabando... Ctrl+C para detener.')
    
    # Inicializa el reconocedor de Vosk
    rec = vosk.KaldiRecognizer(model, 16000)
    
    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = rec.Result()
            text = json.loads(result)["text"]
            print(f"Texto reconocido: {text}")
        else:
            partial_result = rec.PartialResult()
            print(json.loads(partial_result)["partial"])