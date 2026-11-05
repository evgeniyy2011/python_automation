import requests
from requests.auth import HTTPBasicAuth

response = requests.post("http://127.0.0.1:8080/auth",
                         auth=HTTPBasicAuth("test_user", "test_pass"))
print(response.status_code)
print(response.json())