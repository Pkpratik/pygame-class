import random
def lost():
    print("Good try...")
def geusses():
    print("What will be your first geuss?")
    if input() == 0:
       print("Game Over!")
       lost()
    else:
        print("Good Geuss!")
        print("What's your next? geuss?")
#Introduction
print("""Welcome to my first game!


Where we will play a game of pure luck.
There is one bomb, and 5 prizes.
The goal is to get as many of the prizes and collect the highest score.
Enter g1, g2, g3, g4, g5 or g6, standing for geuss 1, geuss 2 etc.""")

#This line of code gives each geuss an value
prizes=[0, 50, 100, 250, 500, 1000]
g1=random.choice(prizes)
prizes.remove(g1)
g2=random.choice(prizes)
prizes.remove(g2)
g3=random.choice(prizes)
prizes.remove(g3)
g4=random.choice(prizes)
prizes.remove(g4)
g5=random.choice(prizes)
prizes.remove(g5)
g6=random.choice(prizes)

#First geuss

geusses()
geusses()
geusses()
geusses()
geusses()
geusses()

