import requests  # Need to import packages for making get and post requests

# ***** GET Request Demonstration - GitHub Branches Request *****
server = "https://api.github.com"  # The server URL for the GitHub API.

# Make a request to get branch information from GitHub
r = requests.get(server + "/repos/dward2/BME547/branches")

print(r)
print(r.status_code)
print(r.text)
# This if statement is example of how you would use the status code to
#   detect problems and report them.
if r.status_code != 200:
    print("Problem with request")
    exit()
answer = r.json()
print(type(answer))
for branch in answer:
    print(branch["name"])


# ***** Post Request Demonstration:  Name Server *****

# Create the information to be sent to the server.  Consult server API for
#   needed format and contents.
out_json = {
   "name": "David Ward",
   "net_id": "daw74",
   "e-mail": "david.a.ward@duke.edu"
}

# Make Post request and print results
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_json)
print(r.status_code)
print(r.text)
