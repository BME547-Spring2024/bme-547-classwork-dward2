from flask import Flask, request, jsonify

app = Flask(__name__)

"""
db = []
patient = { "name": <str>,
            "id": <int>,
            "blood_type": <str>,
            "test_names": <list(str)>
            "test_results": <list(anything)>
    }
"""

db = []


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """
    1. Get the data sent with the request.
    2. Call other functions to do all the work.  One of those functions
       should be an input validator.
    3. Return the response.

    {"name": str, "id": int, "blood_type": str}
    """
    # Get the data sent with the request.
    in_json = request.get_json()
    # Call other functions to do all the work.
    result, status_code = new_patient_driver(in_json)
    # Return the response
    return result, status_code


def new_patient_driver(in_json):
    message, status_code = validate_new_patient_input(in_json)
    if message is not True:
        return message, status_code
    new_patient = {"name": in_json["name"],
                   "id": in_json["id"],
                   "blood_type": in_json["blood_type"],
                   "test_names": [],
                   "test_results": []}
    db.append(new_patient)
    return "Patient added", 200


def validate_new_patient_input(in_json):
    if type(in_json) is not dict:
        return "The input was not a dictionary as needed.", 400
    expected_keys = ["name", "id", "blood_type"]
    for key in expected_keys:
        if key not in in_json.keys():
            return "The key {} was missing.".format(key), 400
    expected_types = [str, int, str]
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
    message, status_code = validate_add_test_input(in_json)
    if message is not True:
        return message, status_code
    patient = get_patient(in_json["id"])
    if patient is None:
        return "Id {} not found in database".format(in_json["id"]), 400
    add_test_to_patient(patient, in_json["test_name"], in_json["test_result"])
    return "Test successfully added to patient", 200


def validate_add_test_input(in_json):
    if type(in_json) is not dict:
        return "The input was not a dictionary as needed.", 400
    expected_keys = ["id", "test_name", "test_result"]
    for key in expected_keys:
        if key not in in_json.keys():
            return "The key {} was missing.".format(key), 400
    expected_types = [int, str, int]
    for key, exp_type in zip(expected_keys, expected_types):
        if type(in_json[key]) is not exp_type:
            return "The {} key has an incorrect value type".format(key), 400
    return True, 200


def get_patient(id_number):
    for patient in db:
        if patient["id"] == id_number:
            return patient
    return None


def add_test_to_patient(patient, test_name, test_result):
    patient["test_names"].append(test_name)
    patient["test_results"].append(test_result)


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_get_results(patient_id):
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
    for test_name, test_result in zip(patient["test_names"],
                                      patient["test_results"]):
        output_list.append("{}: {}".format(test_name, test_result))
    return output_list, 200


if __name__ == '__main__':
    app.run()
