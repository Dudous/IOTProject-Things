from datetime import datetime
import time
import serial
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate('./park-iot-firebase.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

cards_ref = db.collection('cards')

ser = serial.Serial('COM4', 9600)
print('bora pai')

while True:
    data = ser.readline().decode('utf-8').strip()

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

            print(card_doc.to_dict().get('enter'))

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