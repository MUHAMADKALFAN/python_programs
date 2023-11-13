l1=[]
def create():
    n=int(input("Enter liment"))
    for i in range(n):
        m=int(input("Enter Element"))
        l1.append(m)
    print(l1)
def add():
    m=int(input("Enter Element"))
    l1.append(m)
    print(l1)
def Replas():
    n=int(input("position:"))
    m=int(input("Enter Element"))
    l1.pop(n)
    l1.insert(n,m)
    print(l1)
def Remove():
    n=int(input("Remove:"))
    l1.remove(n)
    print(l1)
while True:
    print("list operations:\n1.create list\n2.Add element\n3.Replace\n4.Remove\n5.sort\n6.Exit\n")
    k=int(input("Enter the choes:"))
    if k==1:
        create()
    elif k==2:
        add()
    elif k==3:
        Replas()
    elif k==4:
        Remove()
    elif k==5:
            l1.sort()
            print(l1)
    elif k==6:    
        print("Exet")
        break