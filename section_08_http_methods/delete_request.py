import requests #intall request package
import http

#pip list -> list all packages

base_url="http://reqres.in"

#DELETE request
response=requests.delete(base_url + "/api/users/2")
print(response.status_code)
assert response.status_code == http.client.NO_CONTENT
