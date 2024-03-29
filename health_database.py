"""
Single patient record:  {"First Name": str,
                         "Last Name": str,
                         "Age": int,
                         "MRN": int,
                         "Tests": list]
Test list:  [("HDL", 100), ("LDL", 15), ("HR", 62)]
"""


def create_database_entry(first_name, last_name, age, mrn):
    new_patient = {"First Name": first_name,
                   "Last Name": last_name,
                   "Age": age,
                   "MRN": mrn,
                   "Tests": []}
    return new_patient


def get_full_name(patient):
    full_name = "{} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def print_database(db):
    for patient in db:
        print("MRN: {}, Full Name: {}, Age:{}".format(patient["MRN"],
                                                      get_full_name(patient),
                                                      patient["Age"]))


def get_patient(db, MRN):
    for patient in db:
        if patient["MRN"] == MRN:
            answer = patient
            break
    return answer


def add_test_to_patient(db, MRN, test_name, test_value):
    patient = get_patient(db, MRN)
    patient["Tests"].append((test_name, test_value))


def main():
    db = []
    db.append(create_database_entry("Ann", "Ables", 36, 101))
    db.append(create_database_entry("Bob", "Boyles", 25, 102))
    db.append(create_database_entry("Chris", "Chou", 50, 103))
    print(db)
    print()
    add_test_to_patient(db, 101, "HDL", 100)
    add_test_to_patient(db, 101, "LDL", 102)
    print(db)
    print()
    print_database(db)


if __name__ == "__main__":
    main()
