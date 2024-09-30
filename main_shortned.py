# Project with less loc
#Project No : 1 (Snake - Water - Gun)
""" Snake 1
    water -1
    Gun 0 """


import random #used to generate random choice of computer

computer = random.choice([0,1,-1])
youstr = input("Enter Your Choice : ")
youdict = { "s":1 , "w":-1 , "g":0}
reversedict = {1: "Snake", -1:"Water", 0:"Gun"}
you = youdict[youstr]
print(f"You chose {reversedict[you]}\n Commputer chose {reversedict[computer]}")

if computer == you:
    print("It's a Draw!")

else:
    if (((computer - you) == -2) or (computer - you)==1) :
      print("You Win!")

    else:
       print("You Lose!")

