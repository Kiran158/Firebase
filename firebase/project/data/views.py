from django.http import JsonResponse
from django.shortcuts import render
import pyrebase

firebaseConfig = {
        "apiKey": "AIzaSyAGunbEfXQpugL8eXjRc5hp3PTXrn5h9iA",
        "authDomain": "temp-3bd23.firebaseapp.com",
        "databaseURL": "https://temp-3bd23-default-rtdb.firebaseio.com",
        "projectId": "temp-3bd23",
        "storageBucket": "temp-3bd23.appspot.com",
        "messagingSenderId": "47300505881",
        "appId": "1:47300505881:web:2c14942177a657c34e9588"
      }

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

def index(request):
    dht_Data = database.child("Main").child("DHT").get()
    electrical_Data = database.child("Main").child("Electrical").get()
    dht_Dict = {
        dht_Data : {
            "c2h2_Gas" : dht_Data.val()["C2H2_Gaslevel"],
            "ch4_Gas" :  dht_Data.val()["CH4_Gaslevel"],
            "c0_Gas" :  dht_Data.val()["CO_Gaslevel"],
            "h2_Gas" :  dht_Data.val()["H2_Gaslevel"],
            "oil_Level" :  dht_Data.val()["OIL_LEVEL"],
            "oil_Moisture" :  dht_Data.val()["Oil_Moisture"],
            "oil_Temperature" :  dht_Data.val()["Oil_Temparture"],
            "humidity" :  dht_Data.val()["humidity"]
        }
    } 
    
    electrical_Dict = {
            "active_Power" : electrical_Data.val()["ACTIVE_POWER"],
            "apparent_Power" : electrical_Data.val()["APPARENT_POWER"],
            "current" : electrical_Data.val()["CURRENT"],
            "energy" : electrical_Data.val()["ENERGY"],
            "frequency" : electrical_Data.val()["FREQUENCY"],
            "power_Factor" : electrical_Data.val()["POWEER_FACTOR"],
            "reactive_Power" : electrical_Data.val()["REACTIVE_POWER"],
            "voltage" : electrical_Data.val()["VOLTAGE"]
    }
    return render(request, 'data.html', {'dht_dict': dht_Dict, 'electrical_Dict' : electrical_Dict})
    return JsonResponse(dht_Dict, electrical_Dict)

