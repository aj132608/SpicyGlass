from firebase import firebase
import json

if __name__ == "__main__":
    with open('creds.json') as file:
        creds = json.load(file)

    firebase_obj = firebase.FirebaseApplication(creds['databaseURL'])


