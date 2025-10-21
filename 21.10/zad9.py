ocenka = int(input("ocenka:"))
if ocenka >= int("90") and ocenka < int("100"):
    quit("A")
elif ocenka >= int("80") and ocenka < int("89"):
    quit("B")
elif ocenka >= int("70") and ocenka < int("79"):
    quit("C")
elif ocenka >= int("60") and ocenka < int("69"):
    quit("D")
elif ocenka >= int("0") and ocenka < int("59"):
    quit("F")
else:
    print("nevalidni tochki")
    quit("opitaj otnovo")