teencode = ["hc", "ng", "eny", "any", "ns"]

teencode = {
    "hc" : "hoac",
    "ng" : "nguoi",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu",
    "ns" : "noi",
}

while True: 
    word = input("Enter a word: ")
    if word in teencode:
        print(teencode[word])

    update = input("Do you want to update (Y/N):").upper()
    if update == "Y":
        new_trans = input("New translation? ")
        teencode[word] = new_trans
        print(teencode)
    else:
        need_contribute = input("Code doesn't exist, contribute? (Y/N? ").u
        trans = input("Your translation?")
        teencode[word] = new_trans
        print(teencode)
        if need_contribute == "N":
            print("jk")
           
        
