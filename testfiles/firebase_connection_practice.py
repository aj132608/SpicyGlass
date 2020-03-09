from firebase import firebase
import json

if __name__ == "__main__":
    with open('creds.json') as file:
        creds = json.load(file)

    firebase_obj = firebase.FirebaseApplication(creds['databaseURL'], None)
    name = firebase_obj.get('user', None)
    # print(name)
    # response = firebase_obj.post('user', 'YA BOI')
    # returns Key for the value that was posted
    # response_key = response['name']
    # print("Key: ", response_key)

    # response = firebase_obj.put('', 'car-on', False)
    # print(response)

    print((firebase_obj.get('', None)))
    data = {
        'front': False,
        'back': False
    }
    firebase_obj.put('car-on', '', True)
    print((firebase_obj.get('car-on', None)))
