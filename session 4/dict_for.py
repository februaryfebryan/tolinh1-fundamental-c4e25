person = {
    "name": "Quan",
    "age": 25,
    "Location": "Hanoi",
}

#thuon dung de DEBUG

# for k in person.keys():
#     print(k, person (k))

# for v in person.value():
#     print(v)

for k,v in person.items():
    print(k,v, sep = ": ")
