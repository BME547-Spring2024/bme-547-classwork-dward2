import requests

server = "http://127.0.0.1:5000"

patient_1 = { "name": "Ann Ables",
              "id": "101",
              "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient_1)
print(r.status_code)
print(r.text)

patient_2 = {"name": "Bob Boyles",
             "id": 102,
             "blood_type": "A+"}
r = requests.post(server + "/new_patient", json=patient_2)
print(r.status_code)
print(r.text)
