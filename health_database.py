"""
Single patient record:  [Name (str), age (int), MRN (int), Tests (list)]
"""

def create_database_entry(name, age, mrn):
    new_patient = [name, age, mrn, []]
    return new_patient
    

def main():
    x = create_database_entry("Ann Ables", 36, 101)
    print(x)
    
    
if __name__ == "__main__":
    main()

