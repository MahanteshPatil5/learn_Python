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