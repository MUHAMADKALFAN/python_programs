v=[2, 7, 11, 15]
l=[]
for i in range(len(v)):
    for j in range(i+1,len(v)):
        if v[i]+v[j]==9:
            l.append(v.index(v[i]))
            l.append(v.index(v[j]))
print(l)

