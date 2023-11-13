import random
words=['apple', 'orange', 'kivi']
word=random.choice(words)
gusesss=[]
tries=6
while tries>0:
    display=""
    for l in word:
        if l in gusesss: 
            display+=l
        else:
            display+='_'
    print(display)
    guses=input("Guses a letter: ").lower() 
    if guses in gusesss:
            print("You already gussed that letter!")
            continue
    gusesss.append(guses)
    if guses in word: 
            print("Correct!!")
    else: 
            print("Worng!!") 
            tries-=1
    if "_" not in display: 
            print("you win!")
            break
    elif tries==0:
            print("you lose!..th ewords was :",word)
            break
