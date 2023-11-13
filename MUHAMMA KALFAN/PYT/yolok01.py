z=input("Enter The ....")
c=z.split()
n=c[0]
l=[]
for i in c:
    if i[0].isupper():
        l.append(i)
print(l)