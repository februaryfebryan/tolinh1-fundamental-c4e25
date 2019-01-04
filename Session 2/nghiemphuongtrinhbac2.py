a = int(input("Nhap a: "))
b= int(input("Nhap b: "))
c = int(input("Nhap c: "))




delta = b**2 - 4*a*c

if delta < 0:
    print("Vo nghiem")
elif delta == 0:
    
    x = (-b)/(2*a)
else:
    delta_sqrt = delta**0.5
    x1 = (-b + delta_sqrt) / (2*a)
    x2 = (-b - delta_sqrt)/(2*a)
    print ("2 solutions, x1 =", x1, "x2=", x2)