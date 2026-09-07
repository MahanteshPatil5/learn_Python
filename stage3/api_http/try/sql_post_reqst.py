import requests
# url = "http://127.0.0.1:5000/students"
# data = {
#     "name":"Vivek","branch":"MBBS"
# }
# response = requests.post(url,json = data)
# print(response.json())

# put
puturl = "http://127.0.0.1:5000/students/15"
putdata = {
    "name" : "VINAY Put chnged","branch":"AI"
}
resput = requests.put(puturl,json=putdata)
if resput.status_code==200:
    print("Chnged using put: ",resput.json())
else:
    print("Failed to change data ")
    

patchurl = "http://127.0.0.1:5000/students/16"
patchdata = {
    "branch":"MBBS MD updated patch" #updating only branch  
}
res = requests.patch(patchurl,json=patchdata)

if res.status_code==200:
    print("Chnged using patch: ",res.json())
else:
    print("Failed to change data ")
    
posturl = "http://127.0.0.1:5000/students"
data = {
    "name":"Vandana","branch":"CSE engineer"
}
response = requests.post(posturl,json = data)
print(response.json())


delete_url = "http://127.0.0.1:5000/students/20"
res_delete = requests.delete(delete_url)
if res_delete.status_code==200:
    print("Delete using delete :: ")
else:
    print("Failed to delete")


