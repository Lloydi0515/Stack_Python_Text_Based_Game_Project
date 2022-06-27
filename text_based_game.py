import time

#Title: Government Scholarship

name = input(f"What is your name? ")
print (f"Hello, {name} good to see you :)")
game = input(f"Do you want to Play text based adventure game? [yes/no] ").lower()

if game == "yes":
    print("That's great!")
    # timer start countdown
    count = 10
    while count > 0:
        print (count),
        time.sleep(1),
        count -=1
    time.sleep(1)
    print (f"Start Now!")
    time.sleep(1)
    print()

    answer = input(f"The Government has Offer a scholarship program abroad, choices are (You just need to pick one): [mit/harvard/singapore/oxford] ").lower()
    if answer == "singapore":
        answer = input(f"Your GF won't approved! will you still continue? [yes/no] ")
        if answer == "yes":
            answer = input(f"your struggling in your studies because of high standard, proceed? [yes/no] ")
            if answer == "yes":
               answer = input(f"You're project very challenging, Proceed? [yes/no] ")
               if answer == "yes":
                print(f"Congratulations! You're Magna cum laude!! and won you're GF back.")
               else:
                print(f"You Lose, you're almost there but you quit!")
            else:
                print(f"You Lose, cause you give up!")
        else:
            print(f"You Loss because you choose love rather than your scholarship")
    elif answer == "mit":
        answer = input(f"You are offered a high paying jobs but you need to quit school. continue in studies? [yes/no] ")
        if answer == "yes":
            answer = input(f"You have difficulty in doing your research project. proceed? [yes/no] ")
            if answer == "yes":
                print(f"Congratulations!! you finish your studies and became a scientist!")
            else:
                print(f"You loss you give in to pressure!")
        else:
            print(f"You loss you're almost there but you stop!")
    elif answer == "harvard":
        print(f"You loss because you meet a blonde girl you fall in love and choose to get married!")
    elif answer == "oxford":
        print("You loss because your plane is crash!")
    else:
        print(f"Invalid Option")
else:
    print(f"But this is really an awesome game! Ok nxt time.")