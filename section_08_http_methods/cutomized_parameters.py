import requests

param= {"p1":"pp1", "p2":"p22"}
response = requests.get("https://httpbin.org/get", params=param)
print(response.text)
