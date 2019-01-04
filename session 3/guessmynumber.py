#sinh ra mot so ngau nhien tu mot den 100
# cho nguoi dung doan, ra TRue hay false

from random import randint
x = randint (1,100)
print(x)
loop = True
while loop:
    guess = int(input("Guess your number:"))
    loop = False
    if guess == x:
        loop = False
        print("Bingo")
    if guess > x:   #dau khac nhau la !=
        loop = True
        print("number too big")
    if guess < x:
        loop = True
        print ("Number too small")