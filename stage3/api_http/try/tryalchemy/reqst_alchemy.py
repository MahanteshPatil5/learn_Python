import requests
data = {
    "name" : "vandana","subject":"Python"
}
url = "http://127.0.0.1:5000/teacher"
response = requests.post(url,json = data)
print(response.status_code)
print(response.json())

#similar way work with Patch put delete