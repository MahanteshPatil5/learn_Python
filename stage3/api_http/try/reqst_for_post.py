import requests
data = {
    "name":"vivek","branch":"MBBS"
}

url = "http://127.0.0.1:5000/students"

response = requests.post(url,json= data)
print(response.status_code)
print(response.json())