# add 2 students POST
import requests
url = "http://127.0.0.1:5000/students"

respons1 = requests.post(url , json= {"name":"MANTU","branch":"CSE"})
print("Post student 1 : ",respons1.json())

data2= {
    "name":"VIVEK","branch":"MBBS"
}
response2 = requests.post(url,json = data2)
print("2nd student data added : ",response2.json())

# get single by id::
url = "http://127.0.0.1:5000/students/1"
# res = requests.get(url)
# print("single get by id : id=1" , res.json())

# using put chnage student 1 data ::
chng_data = {
    "name":"crazy updated","branch":"ZZZ updated"
}
res= requests.put(url,json=chng_data)
print("chnaged data using PUT : ",res.json())

# # partial chnage using patchh
# datapatch = {"branch":"MECH"}
# url = "http://127.0.0.1:5000/students/2"
# respatch = requests.patch(url,json= datapatch)
# print("patch : ",respatch.json())


# # delete using id
# resdel = requests.delete(url)
# print("delete result : ",res.json())