    # name age location exes status friends

person = ["Quan", 25, "Hanoi", 3, False, 125]
#kho hieu

# person = {}
# print(person)
# print(type(person))

#(muon dau thang thi dung CTRL va /)
person = {
    "name":"Quan", #cac cap key va value se cach nhau bang mot dau phay
    "age":25,
    "location": "Hanoi",
    "exes": 3,
    "status": "False",
    "friends": 125
} 

person["name"] = "A.Quan" #neu key da ton tai thi la update
person["exp"] = 2         #neu key chua ton tai thi la create

# print(person)
check ="y"
if True:

    if "skills" in person:
        print(person["skills"])
        
    else:
        print("Not exists")
        contribute = input("Code doesnt exist, do you want to contribute: (Y/N) ?")
        if contribute == "Y":
            newcon = input("Enter? ")
            person["skills"] = newcon
  

# print(person["location"])
# print (person["name"])
# print(person["status"])