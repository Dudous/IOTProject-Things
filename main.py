from datetime import datetime
import time
import serial
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate('./park-iot-firebase-config.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

cards_ref = db.collection('cards')

ser = serial.Serial('COM3', 9600)
print('bora pai')

while True:
    data = ser.readline().decode('utf-8').strip()

    if(data):
        cards = cards_ref.get()

        flag = False

        for card in cards:
            if(card.to_dict().get('card') == data):
                flag = True
                cards_ref.document(card.id).update({
                    'exit' : str(datetime.now())
                })
                print(f'{card.id}: {card.to_dict()}')

        if not flag:
            data = {'card': data,
                    'enter': str(datetime.now()),
                    'exit': ''
                    }

            cards_ref.add(data)

            time.sleep(1)

        print('ok')