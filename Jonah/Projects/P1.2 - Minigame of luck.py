import random

# Gives all options additional prizes
prizes=[0, 50, 100, 250, 500, 1000]
option1=random.choice(prizes)
prizes.remove(option1)
option2=random.choice(prizes)
prizes.remove(option2)
option3=random.choice(prizes)
prizes.remove(option3)
option4=random.choice(prizes)
prizes.remove(option4)
option5=random.choice(prizes)
prizes.remove(option5)
option6=random.choice(prizes)

#Introduction       
print("""Welcome to my first game!

Where we will play a game of pure luck.
There is one bomb, and 5 prizes.
The goal is to get as many of the prizes and collect the highest score.
Enter option1, option2, option3, etc.""")

#Hi Pratik, what is wrong here? I tested if this worked but it did'nt. option 1 is one of the 6 choises of prizes. Why doesnt this work?

uc=int(input())
if uc=option1:
    if uc==0:
        lost()
    else:
        print("Well done! Total score:",uc)

