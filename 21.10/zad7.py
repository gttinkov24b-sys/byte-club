a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a > int("0") and b > int("0") and c > int("0"):
    if a < b+c and b< c+a and c < a+b:
        print("validen")
    else:
        quit("nevaliden")
else:
    quit("nevaliden")