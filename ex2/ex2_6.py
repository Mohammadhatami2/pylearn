import random

roll=random.randint(1, 6)

print(roll)

if roll==6 :
    que = input("do you want roll again?")

    if que=="yes":
        roll2=random.randint(1, 6)
    
        print(roll2)

    else :
        print("ok")

