import random

userscore = 0
computerscore = 0
repeate = int(input("how much time you want to play"))
random_choose = ["stone", "paper", "sizers"]
i = 1
while i <= repeate:
    print("attempt", i)
    user_choose = input("enter your choice")
    computerchoice = random.choice(random_choose)
    if (
        user_choose == "sizers"
        and computerchoice == "paper"
        or user_choose == "stone"
        and computerchoice == "sizers"
        or user_choose == "paper"
        and computerchoice == "stone"
    ):
        userscore += 1
        print(computerchoice)
    elif (
        user_choose == "sizers"
        and computerchoice == "stone"
        or user_choose == "stone"
        and computerchoice == "paper"
        or user_choose == "paper"
        and computerchoice == "sizers"
    ):
        computerscore += 1
        print(computerchoice)
    else:
        print(computerchoice)
        print("user score:", userscore)
        print("computer score:", computerscore)
        i += 1
        continue
    print("user score:", userscore)
    print("computer score:", computerscore)
    i += 1
if userscore > computerscore:
    print("***YOU WIN***")
elif userscore < computerscore:
    print("YOU LOSE")
else:
    print("MATCH DRAWN")


def learn_to_code():
    print("you can learn to code")
    learn_to_code()
