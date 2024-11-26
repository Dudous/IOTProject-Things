from datetime import datetime
import time
import serial
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate("./park-iot-firebase.json")

app = firebase_admin.initialize_app(cred)

db = firestore.client()

cards_ref = db.collection('cards')

catraca_ref = db.collection('catraca')

ser = serial.Serial('COM4', 9600)
print('bora pai')

while True:
    catraca = catraca_ref.document('entrada').get().to_dict().get('state')

    print(catraca)

    if catraca:
        ser.write(b'True')
    else:
        ser.write(b'False')

    time.sleep(1)

    data = ser.readline().decode('utf-8').strip()
    print('teste')

    if(data):
        print(data)
        cards = cards_ref.get()

        cardId = ''

        for card in cards:
            if card.to_dict().get('card') == data and card.to_dict().get('exit') == '':
                cardId = card.id
                break

        if cardId:
            card_doc = cards_ref.document(cardId).get()

            if card_doc.to_dict().get('exit') == '':
                cards_ref.document(cardId).update({
                    'exit': str(datetime.now())
                })
                continue

        data = {'card': data,
                'enter': str(datetime.now()),
                'exit': ''
            }

        cards_ref.add(data)