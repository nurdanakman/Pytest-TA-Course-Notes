import requests

#default header
response = requests.get("https://httpbin.org/get")
print(response.text)

#customized header
header_data = {"T1":"Header Title 1", "T2":"Header Title 2"}
response = requests.get("https://httpbin.org/get", headers=header_data)
print(response.text)
