import re
v=input("Email:")
z=re.search('[a-z]+[0-9]*[@]gmail.com',v)
if z:
    print("Email is yes")
else:
    print("Not Email")
