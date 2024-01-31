"""
Single patient record:  [Name (str), age (int), MRN (int), Tests (list)]
"""

def create_database_entry(name, age, mrn):
    new_patient = [name, age, mrn, []]
    return new_patient
    

def main():
    db = []
    db.append(create_database_entry("Ann Ables", 36, 101))
    db.append(create_database_entry("Bob Boyles", 25, 102))
    db.append(create_database_entry("Chris Chou", 50, 103))
    
    print(db)
    
    
if __name__ == "__main__":
    main()

