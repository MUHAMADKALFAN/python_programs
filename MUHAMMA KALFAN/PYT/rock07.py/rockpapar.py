n=input("enter in:")
import random
c=("Rock","Paper","Scissors")
x=random.choice(c)
print(x)
if x==n:
    print("the game is a tie")
elif(
    (n=="Rock" and x=="Sicssors")
    or(n=="Sicssors" and x=="Paper")
    or(n=="Paper" and x=="Rock")
    ):
    print("the is You win")
else:
    print("Computer is win")