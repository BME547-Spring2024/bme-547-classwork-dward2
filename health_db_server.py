from flask import Flask, request, jsonify
from pymodm import connect, MongoModel, fields
from pymodm import errors as pymodm_errors
from server_database import Patient

app = Flask(__name__)


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """Route handler for addition of new patient to server database

    This function acts as the Flask handler for the "/new_patient" route.
    Information is received about the new patient and that information is
    validated and added to the database if a valid entry.

    For this route, a JSON string is received as input and should be in the
    following format:

    {"name": str, "id": int, "blood_type": str}

    Flask handler functions should only do three things:
    1. Get the data sent with the request.
    2. Call other functions to do all the work.
    3. Return the response.

    Returns:
        str: a message about the success or failure of the route
        int: the status code for the response

    """
    # Get the data sent with the request.
    in_json = request.get_json()
    # Call other functions to do all the work.
    result, status_code = new_patient_driver(in_json)
    # Return the response
    return result, status_code


def new_patient_driver(in_json):
    """ Validates and adds new patient information to the database

    This function implements the /new_patient route of the server.  The input
    is a dictionary in the following format:

    {"name": str, "id": int, "blood_type": str}

    First, this function calls a validation function to ensure that the
    expected keys and data types exist in the input dictionary.  If the
    input data is successfully validated, a correctly formatted dictionary
    is made with the new patient information and this dictionary is added
    to the database.

    Args:
        in_json (dict): the input data for the new patient

    Returns:
        str: Message about the success or failure of the function
        int: a status code to send back with the response

    """
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    message, status_code = validate_dictionary_input(in_json,
                                                     expected_keys,
                                                     expected_types)
    if message is not True:
        return message, status_code
    new_patient = Patient(
        name=in_json["name"],
        id=in_json["id"],
        blood_type=in_json["blood_type"],
    )
    new_patient.save()
    return "Patient added", 200


def validate_dictionary_input(in_json, expected_keys, expected_types):
    if type(in_json) is not dict:
        return "The input was not a dictionary as needed.", 400
    for key in expected_keys:
        if key not in in_json.keys():
            return "The key {} was missing.".format(key), 400
    for key, exp_type in zip(expected_keys, expected_types):
        if type(in_json[key]) is not exp_type:
            return "The {} key has an incorrect value type".format(key), 400
    return True, 200


@app.route("/add_test", methods=["POST"])
def post_add_test():
    in_json = request.get_json()
    message, status_code = add_test_driver(in_json)
    return message, status_code


def add_test_driver(in_json):
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    message, status_code = validate_dictionary_input(in_json,
                                                     expected_keys,
                                                     expected_types)
    if message is not True:
        return message, status_code
    patient = get_patient(in_json["id"])
    if patient is None:
        return "Id {} not found in database".format(in_json["id"]), 400
    add_test_to_patient(patient, in_json["test_name"], in_json["test_result"])
    return "Test successfully added to patient", 200


def get_patient(id_number):
    try:
        patient = Patient.objects.raw({"_id": id_number}).first()
    except pymodm_errors.DoesNotExist:
        return None
    return patient


def add_test_to_patient(patient, test_name, test_result):
    patient.test_names.append(test_name)
    patient.test_results.append(test_result)
    patient.save()


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
    """ Route handler for the /get_results/<patient_id> GET route

    This function handles the /get_results/<patient_id> GET route for the
    server.  This is a variable URL in which the user is expected to put the
    patient id in place of the <patient_id> in the url.  For example:
    /get_results/101.  The actual input for the variable URL is placed in the
    patient_id parameter as a string.  This function then calls another
    function that implements the retrieval of the requested patient
    information.

    Args:
        patient_id (str): the user supplied patient id number

    Returns:
        str: a JSON-string of either a list of test results or an error message
        int: a status code for the response

    """
    results, status_code = get_results_driver(patient_id)
    return jsonify(results), status_code


def get_results_driver(patient_id):
    try:
        patient_id = int(patient_id)
    except ValueError:
        return "Id {} is not a valid patient id".format(patient_id), 400
    patient = get_patient(patient_id)
    if patient is None:
        return "Id {} not found in database".format(patient_id), 400
    output_list = []
    for test_name, test_result in zip(patient.test_names,
                                      patient.test_results):
        output_list.append("{}: {}".format(test_name, test_result))
    return output_list, 200


def init_server():
    connect("mongodb+srv://daw_spring:daw_spring@bme547.ba348.mongodb.net/"
            "class_work?retryWrites=true&w=majority&appName=BME547")
    # logging.basicConfig()


if __name__ == '__main__':
    init_server()
    app.run()
