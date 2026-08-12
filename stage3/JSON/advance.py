# 1.nested JSON  data is nested
data = {
    "id" : 94,"name":"Mantu","address":{"city":"Gokak","pin": 591224 },
    "skill":["C","C++","python"]
}

data["address"]["city"] # Gokak


# 2.Serialization and desearilazation
#  python obj to JSON  serialization dump
# JSON to python obj  deserialization load

# 3. serialization limitations  not all python obj become to JSON 
# it only work with : str,int,float,bool,None,list,dict;
# not with tuple,set,custom class etc   these need conversation

# tuple dumping 
import json
# data = {"skill" : {"python","SQL"}} # tuple {} is there
# json.dumps(data)  # gives typeError  
# so chnage it to 
data = {"skill" : list({"python","SQL"}), "name":"mahantesh"} # converted to listnow it can dump 
file = json.dumps(data)  # No error   
print(file)


# 5.pretty JSON  to print the output in readable form
# normal json.dumps(data) 
file2 = json.dumps(data,indent=3,sort_keys=True)
print(file2)    # pretty print of file2

# 6.property with ascii value ::  use ensure_ascii = Flase
# when to save data other then english use ensure_ascii = Flase  
data = {
    "name": "ಮಹಾಂತೇಶ್"   #  this is used when ascii is flase
}
file3 = json.dumps(data, ensure_ascii=False)

# 7.JSON validation
# when data enterder from backend is wrong and not going to save then error occures:: JSONDecodeError
# so use try,except method 
try:
    file4 = json.loads(JSON_string)  #json string is a sting entering to json file
except json.JSONDecodeError:
    print("Invalid JSON")
    
