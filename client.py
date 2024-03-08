import requests

server = "http://127.0.0.1:5003"

r = requests.get(server)
print(r.status_code)
print(r.text)

r = requests.get(server+"/info")
print(r.status_code)
print(r.text)

out_json = {"HDL_value": 55}
r = requests.post(server+"/HDL", json=out_json)
print(r.status_code)
print(r.text)
x = r.json()
print(x)
