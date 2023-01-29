import requests #intall request package
import json # install
import http

#pip list -> list all packages

base_url="http://reqres.in"

#GET request
response=requests.get(base_url + "/api/users?page=2")
print("--------------------------")
print(response.status_code) #response code
print("--------------------------")
print(response.content) #body
print("--------------------------")
print(response.headers) #header

#Validate Status code
assert response.status_code == http.client.OK

#Fetch Response Headers
print("--------------------------Fetch")
print(response.headers)
print("--------------------------")
print(response.headers.get("Content-Type"))
print("--------------------------")
print(response.headers.get("Date"))
#Fetch Cookies
print("--------------------------")
print(response.cookies)
#Fetch encoding
print("--------------------------")
print(response.encoding)
#Fetch elapsed time
print("--------------------------")
print(response.elapsed)

#Fetch Response Content
print("--------------------------")
print(response.content)
#Parse response to Json format
print("--------------------------")
json_reponse=json.loads(response.text)
print(json_reponse)
#Fetch value using
total_pages=json_reponse["total_pages"]
print("--------------------------")
print(total_pages)
assert total_pages == 2
#Fetch complex value
first_name_0=json_reponse["data"][0]["first_name"]
print("--------------------------")
print(first_name_0)
first_name_2=json_reponse["data"][2]["first_name"]
print("--------------------------")
print(first_name_2)
first_names=[]
for i in range(0,6):
    first_names.append(json_reponse["data"][i]["first_name"])
print("--------------------------")
print(first_names)