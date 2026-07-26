age = input("Enter age : ")

if(age>18):
    print("U r major u can vote")
else:
    print("minor nt eleigble for voting");

# ()
marks = input("Enter ur marks : ")
attendence = input("Entter the marks : ")

# instead
# if marks >= 35:
#     if attendance >= 75:
#         print("Pass")
# use 
if marks>35 and attendence>85:
    print("U r eligble for vote")

# style 2
# instead of

# if fruit == "Apple" or fruit == "Mango" or fruit == "Orange":
#     print("use below way");
# # use 
# if fruit in ["apple",'banana',"orange"]: