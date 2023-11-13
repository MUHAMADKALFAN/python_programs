l1=[2,4,3]
l2=[5,6,4]
l3=[]
s1=""
s2=""
for i in range(2,-1,-1):
    s1+=str(l1[i])
    s2+=str(l2[i])
sum=int(s1)+int(s2)
n=str(sum)
for j in range(2,-1,-1):
    l3.append(int(n[j]))
print(l3)
