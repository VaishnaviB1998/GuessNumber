import random
n = random.randint(0,999)
g = 0
while (g<=9):
    inp = int(input("guess the number: "))
    g=g+1
    if g==9:
        print("sorry you lost the game")
        break
    elif inp<n:
        print("you have enterd a smaller number\nnumber of guesses left: ",9-g)
    elif inp>n:
        print("you have enterd a greater number\nnumber of guesses left: ",9-g)
    elif inp==n:
        print("Congrats! your guess is correct\nYou won the game in",g,"attempts")
        break



