num1 = int(input("daj chislo 1:"))
num2 = int(input("daj chislo 2:"))
way = input("daj znak(+,-,* ili /):")
if way == "+" or way == "-":
    if way == "+":
        print("a+b=",num1+num2)
    else:
        print("a-b=",num1-num2)
elif way == "*" or way == "/":
    if way == "*":
        print("a*b=",num1*num2)
    else: #znak "/"
        if num2 == "0":
            quit("ne se deli na nula")
        else:
            print("a/b=",num1/num2)
else:
    quit("nevaliden znak")