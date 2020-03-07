from firebaseinterface.firebase_interface import FirebaseInterface
import json

if __name__ == "__main__":

    with open('creds.json') as file:
        creds_dict = json.load(file)

    interface_obj = FirebaseInterface(creds_dict=creds_dict)

    # Fetch the current database held locally as a dictionary
    current_database = interface_obj.get_database_dict()

    print(f"database: {current_database}")

    # Perform a GET request to retrieve a dictionary from the
    # database itself
    current_database = interface_obj.get_data(key='')

    print(f"database: {current_database}")

    # Get the value of a key
    car_on = interface_obj.get_data(key='car-on')

    print(f"car-on: {car_on}")

    # Get a nested value using subkey
    front_defrost = interface_obj.get_data(key='defrost',
                                           subkey='front')

    print(f"front defrost: {front_defrost}")

    # response = interface_obj.change_value(key='car-on', val=True)
    #
    # print(f"PUT request response: {response}")
    #
    # current_database = interface_obj.get_database_dict()
    #
    # print(f"new database: {current_database}")
