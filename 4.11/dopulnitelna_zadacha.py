import math
def sqf(a,b,c):
    d = math.pow(b,2) - 4*a*c
    if d == float(0):
        x = (-b)/(2*a)
        return x
    elif d < float(0):
        return f"nqma koreni"
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        if x1 == x2:
            return x1
        else:
            return x1,x2
num1 = float(input("chislo1:"))
num2 = float(input("chislo2:"))
num3 = float(input("chislo3:"))

print("korenite sa:", sqf(num1,num2,num3))