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

# # get single by id::
# url = "http://127.0.0.1:5000/students/1"
# # res = requests.get(url)
# # print("single get by id : id=1" , res.json())


# # 2. Update that specific student using PUT
put_url = "http://127.0.0.1:5000/students/1"
chng_data = {
    "name":"crazy updated","branch":"ZZZ updated"
}
res = requests.put(put_url, json=chng_data)
if res.status_code == 200:
    print("changed data using PUT : ", res.json())
else:
    print(f"Failed! Status code: {res.status_code}, Server response: {res.text}")

# # partial chnage using patchh
datapatch = {"branch":"MECH"}
url = "http://127.0.0.1:5000/students/2"
respatch = requests.patch(url,json= datapatch)
print("patch : ",respatch.json())


# delete using id

url = "http://127.0.0.1:5000/students/2"
resdel = requests.delete(url)
print("delete result : ",resdel.json())

# output
# $ python -u requst_crud.py
# Post student 1 :  {'branch': 'CSE', 'id': 1, 'name': 'MANTU'}
# 2nd student data added :  {'branch': 'MBBS', 'id': 2, 'name': 'VIVEK'}
# changed data using PUT :  {'branch': 'ZZZ updated', 'id': 1, 'name': 'crazy updated'}
# patch :  {'branch': 'MECH', 'id': 2, 'name': 'VIVEK'}
# delete result :  {'message ': 'student deleted:: '}
