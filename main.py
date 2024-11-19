import serial
import firebase_admin
from firebase_admin import credentials, firestore

# Use a service account.
cred = credentials.Certificate('./park-iot-firebase-config.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# data = {"name": "Los Angeles", "state": "CA", "country": "USA"}

# db.collection("cities").document("LA").set(data)

while True:
    ser = serial.Serial('COM4', 9600, timeout=1)

    data = ser.readline()

    data = data.decode('utf-8')

    print(data)

    ser.close()