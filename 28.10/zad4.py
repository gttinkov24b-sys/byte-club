import random
def random_num():
    num = random.randint(1,100)
    return num
while True:
    answer = input("Napishi 's' za da go spresh i 'g' za da generirash sluchajno chislo ")
    if answer == "s":
        break
    elif answer == "g":
        print(random_num())
    else: quit("ne napisa nito ednoto")
quit("svurshi")
    
    
