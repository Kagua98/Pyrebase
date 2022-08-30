import pyrebase


firebaseConfig = {
    "apiKey": "AIzaSyA6gqDXeU0WtmLN_IBVDVUSzneB-4_98jc",
    "authDomain": "pyfirebasedatabase.firebaseapp.com",
    "databaseURL": "https://pyfirebasedatabase-default-rtdb.firebaseio.com/banner",
    "projectId": "pyfirebasedatabase",
    "storageBucket": "pyfirebasedatabase.appspot.com",
    "messagingSenderId": "466726058918",
    "appId": "1:466726058918:web:a6ec3bb6ee293c410fad67",
    "measurementId": "G-3Q7G360DBE"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Retrieve data
banner = db.child("Users").get()

# To print the key of the db
print(banner.key())

# To print the values of the key
print(banner.val())

# To get individual child of db
banner = db.child("Users").get()
for child in banner.each():
    print(child.val())


