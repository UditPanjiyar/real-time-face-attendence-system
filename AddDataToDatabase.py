import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://real-time-face-attendenc-840be-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "22111065":
        {
            "name": "UDIT PANJIYAR",
            "major": "IT",
            "starting_year": 2021,
            "total_attendance": 0,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "22111066":
        {
            "name": "HRITIK ROSHAN",
            "major": "ACTOR",
            "starting_year": 2001,
            "total_attendance": 0,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "22111067":
        {
            "name": "modi ji",
            "major": "PRIME MINISTER",
            "starting_year": 2014,
            "total_attendance": 0,
            "standing": "G",
            "year": 10,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)