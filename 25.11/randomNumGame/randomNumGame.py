import random
done = False
won = False
while (not done):
    RandomNum=random.randint(1,20)

    for i in range(5):
        GuessedNum = int(input("Give your guess(0-20): "))
        if GuessedNum == RandomNum and GuessedNum>0 and GuessedNum<=20:
            print("You Win!")
            won = True
            break
        elif GuessedNum<RandomNum and GuessedNum>0 and GuessedNum<=20:
            print("Higher")
        elif GuessedNum>RandomNum and GuessedNum>0 and GuessedNum<=20:
            print("Lower")
        else:
            print("number not in spectrum")
    if won == False:
        print("You Lose!")
    decision = input("Wanna Play again(y/n): ")
    if decision.lower() == "y":
        done = False
        won = False
    elif decision == "n":
        done = True
        quit()