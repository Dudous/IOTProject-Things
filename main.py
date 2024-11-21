from datetime import datetime
import serial
import firebase_admin
from firebase_admin import credentials, db

# Use a service account.
cred = credentials.Certificate('./park-iot-firebase-config.json')

app = firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://park-iot-default-rtdb.firebaseio.com/'
})

cards = db.reference('cards')

ser = serial.Serial('COM3', 9600)
print('bora pai')

while True:
    data = ser.readline().decode('utf-8').strip()

    if(data):

        cards.set({
            'code': data,
            'enter': str(datetime.now())
        })

        print(data)
        break


print('ok')