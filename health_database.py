"""
Single patient record:  [Name (str), age (int), MRN (int), Tests (list)]
Test list:  [("HDL", 100), ("LDL", 15), ("HR", 62)]
"""

def create_database_entry(name, age, mrn):
    new_patient = [name, age, mrn, []]
    return new_patient

def print_database(db):
    rooms = ["Room A", "Room B", "Room C"]
    for i, zipped_data in enumerate(zip(db, rooms)):
        patient, room = zipped_data
        print("{} = Name: {}, MRN: {}, Age:{}, Room: {}".format(i, patient[0],
                                                 patient[2],
                                                 patient[1],
                                                 room))

def get_patient(db, MRN):
    for patient in db:
        if patient[2] == MRN:
            answer = patient
            break
    return answer
    
def add_test_to_patient(db, MRN, test_name, test_value):
    patient = get_patient(db, MRN)
    print("In function: {}".format(id(patient)))
    patient[3].append((test_name, test_value))
    


def main():
    db = []
    db.append(create_database_entry("Ann Ables", 36, 101))
    db.append(create_database_entry("Bob Boyles", 25, 102))
    db.append(create_database_entry("Chris Chou", 50, 103))
    print(db)
    print(id(db[0]))
    print()
    add_test_to_patient(db, 101, "HDL", 100)
    add_test_to_patient(db, 101, "LDL", 102)
    print(db)
    print_database(db)
    
    
    
    
if __name__ == "__main__":
    main()

