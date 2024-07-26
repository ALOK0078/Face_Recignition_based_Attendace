import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-a50d6-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name":"HASAN",
            "major":"Robotics",
            "starting_year":2017,
            "total_attendance":60,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2024-06-25 00:54:34"

        },
    "852741":
        {
            "name":"RAJAN",
            "major":"Robotics",
            "starting_year":2017,
            "total_attendance":60,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2024-06-25 00:12:34"

        },
    "963852":
        {
            "name":"ELON MUSK",
            "major":"TESLA",
            "starting_year":2017,
            "total_attendance":60,
            "standing":"G",
            "year":4,
            "last_attendance_time":"2024-06-25 00:12:34"

        },
    "223456":
        {
            "name":"ALOK",
            "major":"KIIT",
            "starting_year":2022,
            "total_attendance":5,
            "standing":"E",
            "year":4,
            "last_attendance_time":"2024-06-25 00:12:34"

        },
}
for key , value in data.items():
    ref.child(key).set(value)