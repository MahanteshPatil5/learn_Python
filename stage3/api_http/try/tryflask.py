import requests

url = "http://127.0.0.1:5000/student"
new_info = {"name":"MANTU name in tryflask bro","age":25}
response = requests.post(url,json=new_info)
print(response.json())

# a code which uses the link url (api) and chnages the in that url
# and prints  the return data