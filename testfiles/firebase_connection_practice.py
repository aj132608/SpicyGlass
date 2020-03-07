try:
    from firebase import firebase
except AssertionError:
    pass
import json

if __name__ == "__main__":
    with open('creds.json') as file:
        creds = json.load(file)

    # Establish a connection with the database using the databaseURL
    firebase_obj = firebase.FirebaseApplication(creds['databaseURL'], None)

    # Pull data from Database
    response = firebase_obj.get('defrost', 'front')

    print(response)
