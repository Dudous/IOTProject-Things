from datetime import datetime
import time
import serial
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Inicializa o Firebase
cred = credentials.Certificate("./park-iot-firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Referência à coleção "vagas"
vagas_ref = db.collection('vagas')

# Configura a porta serial
ser = serial.Serial('COM3', 9600)
time.sleep(2)  # Tempo para inicializar a comunicação serial

while True:
    try:
        data = ser.readline().decode('utf-8').strip()

        data = json.loads(data)

        print(data)

        for vaga, dist in data.items():
            # Lógica para ativar/desativar o campo 'vaga' com base na distância
            if dist < 15:  # Se a distância for menor que 15 cm, ativar a vaga
                vagas_ref.document(vaga).update({'vaga': False})
                print(f'Vaga ativada: {dist} cm')
            else:  # Caso contrário, desativar a vaga
                vagas_ref.document(vaga).update({'vaga': True})
                print(f'Vaga desativada: {dist} cm')

        time.sleep(0.5)  # Ajuste o tempo entre as leituras conforme necessário

    except Exception as e:
        print(f'Erro: {e}')
        break

ser.close()
