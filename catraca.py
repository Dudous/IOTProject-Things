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

users_ref = db.collection('users')

ser = serial.Serial('COM4', 9600, timeout=1)
print('bora pai')

while True:
    catraca = catraca_ref.document('entrada').get().to_dict().get('state')

    data = ser.readline().decode('utf-8').strip()

    print(data)
    
    print(catraca)

    if catraca:
        ser.write(b'1')
    else:
        ser.write(b'0')

    if(data):
        cards = cards_ref.get()

        users = users_ref.get()

        cardId = ''

        validate = False

        for user in users:
            if user.to_dict().get('card') == data:
                validate = True
                break
        
        if validate:
            ser.write(b'0')
        else:
            continue

        for card in cards:
            if card.to_dict().get('card') == data and card.to_dict().get('exit') == '':
                cardId = card.id
                break
            
        time.sleep(4)

        if cardId:
            cards_ref.document(cardId).update({
                'exit': str(datetime.now())
            })
            continue

        data = {'card': data,
                'enter': str(datetime.now()),
                'exit': ''
            }

        cards_ref.add(data)

