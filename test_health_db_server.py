import pytest
from pymodm import MongoModel, connect, fields
from server_database import Patient
from health_db_server import init_server
import copy
init_server()


@pytest.mark.parametrize("data", [
    ({
        "in_json": {"name": "Dave", "id": 101, "blood_type": "O+"},
        "expected_keys": ["name", "id", "blood_type"],
        "expected_types": [str, int, str],
        "expected_answer": True,
        "status_code": 200
    }),
    ({
        "in_json": ["Dave", 101, "O+"],
        "expected_keys": ["name", "id", "blood_type"],
        "expected_types": [str, int, str],
        "expected_answer": "The input was not a dictionary as needed.",
        "status_code": 400
    }),
    ({
        "in_json": {"id": 101, "blood_type": "O+"},
        "expected_keys": ["name", "id", "blood_type"],
        "expected_types": [str, int, str],
        "expected_answer": "The key name was missing.",
        "status_code": 400
    }),
    ({
        "in_json": {"name": "Dave", "id": "101", "blood_type": "O+"},
        "expected_keys": ["name", "id", "blood_type"],
        "expected_types": [str, int, str],
        "expected_answer": "The id key has an incorrect value type",
        "status_code": 400
    }),
])
def test_validate_dictionary_input(data):
    from health_db_server import validate_dictionary_input
    in_json = data["in_json"]
    expected_keys = data["expected_keys"]
    expected_types = data["expected_types"]
    answer, status_code = validate_dictionary_input(in_json,
                                                    expected_keys,
                                                    expected_types)
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]


@pytest.mark.parametrize("data", [
    ({
        "in_json": {"name": "Dave", "id": 101, "blood_type": "O+"},
        "expected_answer": "Patient added",
        "status_code": 200,
        "expected_db": [{"name": "Dave", "id": 101, "blood_type": "O+",
                        "test_names": [], "test_results": []}]
    })
])
def test_new_patient_driver_successful_add(data):
    from health_db_server import new_patient_driver
    # Act:  Call the function to test and then search database for the newly
    #       added record
    answer, status_code = new_patient_driver(data["in_json"])
    db_patient = Patient.objects.raw({"_id": data["in_json"]["id"]}).first()
    # Clean up the database by removing the added entry so that there is no
    # impact on other tests
    db_patient.delete()
    # Assert to check if answers are correct
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
    assert db_patient.name == data["in_json"]["name"]


@pytest.mark.parametrize("data", [
    ({
        "in_json": {"nxame": "Dave", "id": 101, "blood_type": "O+"},
        "expected_answer": "The key name was missing.",
        "status_code": 400,
        "expected_db": []
    }),
])
def test_new_patient_driver_incorrect_request(data):
    from health_db_server import new_patient_driver
    # Act:  Call the function to test
    answer, status_code = new_patient_driver(data["in_json"])
    # Assert to check if answers are correct
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]


# Create two patients to use as starting cases for remaining tests
patient_1 = Patient(name="One", id=101, blood_type="O+",
                    test_names=["HDL", "LDL"],
                    test_results=[100, 50])
patient_2 = Patient(name="Two", id=102, blood_type="O+")


@pytest.mark.parametrize("data", [
    ({
        "id_to_find": 101,
        "db": [patient_1, patient_2],
        "expected": patient_1
    }),
    ({
        "id_to_find": 103,
        "db": [patient_1, patient_2],
        "expected": None
    }),
])
def test_get_patient(data):
    from health_db_server import get_patient
    # Arrange:  Set-up database to have something to find
    for p in data["db"]:
        p.save()
    # Act:  Call function being tested
    answer = get_patient(data["id_to_find"])
    # Clean up database
    for p in data["db"]:
        p.delete()
    # Assert to check answer
    assert answer == data["expected"]


@pytest.mark.parametrize("data", [
    ({
        "patient": copy.deepcopy(patient_1),
        # A deep copy is made of patient_1 because the function we are going
        # to be testing will make changes to the patient it is sent.  We
        # don't want the original patient to change, so we will use a copy
        # for this test.
        "test_to_add": "HDL",
        "result_to_add": 35,
        "expected_tests": ["HDL", "LDL", "HDL"],
        "expected_results": [100, 50, 35]
    })
])
def test_add_test_to_patient(data):
    from health_db_server import add_test_to_patient
    # Act: Call function to test and get results
    add_test_to_patient(data["patient"],
                        data["test_to_add"],
                        data["result_to_add"])
    answer_tests = data["patient"].test_names
    answer_results = data["patient"].test_results
    # Assert to check answers
    assert answer_tests == data["expected_tests"]
    assert answer_results == data["expected_results"]


@pytest.mark.parametrize("data", [
    ({  # All correct
        "db": [copy.deepcopy(patient_1), copy.deepcopy(patient_2)],
        "in_json": {"id": 101, "test_name": "HDL", "test_result": 44},
        "expected_answer": "Test successfully added to patient",
        "status_code": 200,
        "expected_patient":
            Patient(name="One", id=101, blood_type="O+",
                    test_names=["HDL", "LDL", "HDL"],
                    test_results=[100, 50, 44]),
    }),
    ({  # Bad validation
        "db": [copy.deepcopy(patient_1), copy.deepcopy(patient_2)],
        "in_json": {"ixd": 101, "test_name": "HDL", "test_result": 44},
        "expected_answer": "The key id was missing.",
        "status_code": 400,
        "expected_patient": None,
    }),
    ({  # Patient not in database
        "db": [copy.deepcopy(patient_1), copy.deepcopy(patient_2)],
        "in_json": {"id": 103, "test_name": "HDL", "test_result": 44},
        "expected_answer": "Id 103 not found in database",
        "status_code": 400,
        "expected_patient": None,
    }),
])
def test_add_test_driver(data):
    from health_db_server import add_test_driver
    # Arrange: add patients to database
    for p in data["db"]:
        p.save()
    # Act:  Call function to be tested and get modified database entry
    answer, status_code = add_test_driver(data["in_json"])
    if data["expected_patient"] is not None:
        updated_p = Patient.objects.raw({"_id": data["in_json"]["id"]}).first()
    # Clean up database
    for p in data["db"]:
        p.delete()
    # Assert to check for correct answers
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
    if data["expected_patient"] is not None:
        assert updated_p == data["expected_patient"]


@pytest.mark.parametrize("data", [
    ({  # Correct
        "db": [patient_1, patient_2],
        "id_to_use": 101,
        "expected_answer": ["HDL: 100", "LDL: 50"],
        "status_code": 200
    }),
    ({  # Invalid patient id
        "db": [patient_1, patient_2],
        "id_to_use": "10x3",
        "expected_answer": "Id 10x3 is not a valid patient id",
        "status_code": 400
    }),
    ({  # Patient not in database
        "db": [patient_1, patient_2],
        "id_to_use": 103,
        "expected_answer": "Id 103 not found in database",
        "status_code": 400
    }),
])
def test_get_results_driver(data):
    from health_db_server import get_results_driver
    # Arrange: add data to database
    for p in data["db"]:
        p.save()
    # Act: Call function to be tested
    answer, status_code = get_results_driver(data["id_to_use"])
    # Clean up database
    for p in data["db"]:
        p.delete()
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
