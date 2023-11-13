import random
x=("Apple","Paper","orannge","Grape")
v=random.choice(x)
c=[]
tries=6
while tries>0:
    display=""
    for i in v:
        if i in c:
            display+=1
        else:
                display+="_"
                print(display)
                m=input("Guses a letter:-").lower()
                if m in c:
                        print("Guses already gussed that letter!")
                        continue
                c.append(m)
                if m in v:
                        print("Correct!!")
                else:
                        print("Worng!!")
                        tries-=1
                        if "_" not in display:
                               print("You win!")
                        elif tries==0:
                               print("You lose!..the words was:",v)
                               break
                        print("Tries left :",tries)