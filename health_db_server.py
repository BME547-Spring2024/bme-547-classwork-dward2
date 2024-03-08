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

if __name__ == '__main__':
    app.run()

