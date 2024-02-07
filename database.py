# print("This is the database.py file.")
# print("Python thinks this is called {}".format(__name__))


import blood_calculator as bc


patient_HDL = 65

HDL_level = bc.analyse_HDL(patient_HDL)
LDL_lelel = bc.analyse_LDL(100)

if HDL_level == "Low":
    print("Contact the doctor.")
else:
    print("Looks good.")
