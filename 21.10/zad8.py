#from datetime import date, datetime
#today = date.today()
today = "21/10/25"
godina = input("data(format: dd/mm/yy):")
if godina == today:
    print("bravo znaesh datata!")
else:
    print("bravo NE znaesh datata!")
vgodina = int(input("koq godina sme"))

if vgodina%400 == 0:
    print(f"{vgodina} e visokosna godina")
    z = int("1")
else:
    print(f"{vgodina} ne e visokosna godina")
    z = int("0")
mesec = int(input("koj mesec sme(chislo):"))
if mesec == int("1") or mesec == int("3") or mesec == int("5") or mesec == int("7") or mesec == int("8") or mesec == int("10") or mesec == int("12"):
    print(mesec, "mesec ima 31 dena")
elif mesec == int("2"):
    if z == int("1"):
        print("fevroari ima 29 dena")
    else: #z == int("0"):
        print("fevroari ima 28 dena")
else:
    print(mesec, "mesec ima 30 dena")
