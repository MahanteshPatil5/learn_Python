import requests
url = "http://127.0.0.1:5000/students"
data = {
    "name":"Vivek","branch":"MBBS"
}
response = requests.post(url,json = data)
print(response.json())