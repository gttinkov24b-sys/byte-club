def discount(p,d):
    dp = float(p)*float(d)/100
    fp = float(p)-float(dp)
    return fp
cena = float(input("kolko e cenata:"))
namal = float(input("kolko e namalenieto:"))
print(discount(cena,namal))