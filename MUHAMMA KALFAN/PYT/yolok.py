z=input("Enter The ....")
c=z.split()
n=c[0]
for i in range(len(c)):
    if len(c[i])>len(n):
        n=c[i]
print("largest word is: ",n)