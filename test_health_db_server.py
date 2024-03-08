import pytest


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
    }),
    ({
        "in_json": {"nxame": "Dave", "id": 101, "blood_type": "O+"},
        "expected_answer": "The key name was missing.",
        "status_code": 400,
        "expected_db": []
    }),
])
def test_new_patient_driver(data):
    from health_db_server import new_patient_driver, db
    answer, status_code = new_patient_driver(data["in_json"])
    is_same_db = (db == data["expected_db"])
    db.clear()
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
    assert is_same_db


@pytest.mark.parametrize("data", [
    ({
        "id_to_find": 101,
        "db": [{"id": 101, "name": "one"},
               {"id": 102, "name": "two"}],
        "expected": {"id": 101, "name": "one"}
    }),
    ({
        "id_to_find": 103,
        "db": [{"id": 101, "name": "one"},
               {"id": 102, "name": "two"}],
        "expected": None
    }),
])
def test_get_patient(data):
    from health_db_server import get_patient, db
    db.extend(data["db"])
    answer = get_patient(data["id_to_find"])
    db.clear()
    assert answer == data["expected"]


@pytest.mark.parametrize("data", [
    ({
        "patient": {"name": "Dave", "id": 101, "blood_type": "O+",
                    "test_names": ["LDL"], "test_results": [46]},
        "test_to_add": "HDL",
        "result_to_add": 35,
        "expected_tests": ["LDL", "HDL"],
        "expected_results": [46, 35]
    })
])
def test_add_test_to_patient(data):
    from health_db_server import add_test_to_patient, db
    add_test_to_patient(data["patient"],
                        data["test_to_add"],
                        data["result_to_add"])
    answer_tests = data["patient"]["test_names"]
    answer_results = data["patient"]["test_results"]
    assert answer_tests == data["expected_tests"]
    assert answer_results == data["expected_results"]


@pytest.mark.parametrize("data", [
    ({  # All correct
        "db": [{"name": "Dave", "id": 101, "blood_type": "O+",
                        "test_names": ["LDL"], "test_results": [46]},
               {"name": "Andrew", "id": 102, "blood_type": "A+",
                "test_names": [], "test_results": []}
               ],
        "in_json": {"id": 101, "test_name": "HDL", "test_result": 44},
        "expected_answer": "Test successfully added to patient",
        "status_code": 200,
        "expected_db":
            [{"name": "Dave", "id": 101, "blood_type": "O+",
              "test_names": ["LDL", "HDL"], "test_results": [46, 44]},
             {"name": "Andrew", "id": 102, "blood_type": "A+",
              "test_names": [], "test_results": []}
             ],
    }),
    ({  # Bad validation
        "db": [{"name": "Dave", "id": 101, "blood_type": "O+",
                "test_names": ["LDL"], "test_results": [46]},
               {"name": "Andrew", "id": 102, "blood_type": "A+",
                "test_names": [], "test_results": []}
               ],
        "in_json": {"ixd": 101, "test_name": "HDL", "test_result": 44},
        "expected_answer": "The key id was missing.",
        "status_code": 400,
        "expected_db":
            [{"name": "Dave", "id": 101, "blood_type": "O+",
              "test_names": ["LDL"], "test_results": [46]},
             {"name": "Andrew", "id": 102, "blood_type": "A+",
              "test_names": [], "test_results": []}
             ],
    }),
({  # Patient not in database
        "db": [{"name": "Dave", "id": 101, "blood_type": "O+",
                "test_names": ["LDL"], "test_results": [46]},
               {"name": "Andrew", "id": 102, "blood_type": "A+",
                "test_names": [], "test_results": []}
               ],
        "in_json": {"id": 103, "test_name": "HDL", "test_result": 44},
        "expected_answer": "Id 103 not found in database",
        "status_code": 400,
        "expected_db":
            [{"name": "Dave", "id": 101, "blood_type": "O+",
              "test_names": ["LDL"], "test_results": [46]},
             {"name": "Andrew", "id": 102, "blood_type": "A+",
              "test_names": [], "test_results": []}
             ],
    }),
])
def test_add_test_driver(data):
    from health_db_server import add_test_driver, db
    db.extend(data["db"])
    answer, status_code = add_test_driver(data["in_json"])
    new_db = db.copy()
    db.clear()
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
    assert new_db == data["expected_db"]


patient_1 = {"name": "Dave", "id": 101, "blood_type": "O+",
                        "test_names": ["LDL", "HDL"], "test_results": [46, 35]}
patient_2 = {"name": "Andrew", "id": 102, "blood_type": "A+",
                        "test_names": [], "test_results": []}


@pytest.mark.parametrize("data", [
    ({  # Correct
        "db": [patient_1, patient_2],
        "id_to_use": 101,
        "expected_answer": ["LDL: 46", "HDL: 35"],
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
    from health_db_server import get_results_driver, db
    db.extend(data["db"])
    answer, status_code = get_results_driver(data["id_to_use"])
    db.clear()
    assert answer == data["expected_answer"]
    assert status_code == data["status_code"]
