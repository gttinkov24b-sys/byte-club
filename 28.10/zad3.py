def check_age(age):
    if age >= int(18):
        return True
    else:
        return False
vuzrast = int(input("na kolko godini si"))
print(check_age(vuzrast))


