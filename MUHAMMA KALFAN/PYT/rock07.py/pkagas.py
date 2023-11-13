n=input("Enter the password:-")
if len(n)>=8:
     for i in n:
         if(i.isupper() or i.islower or i.isdigit()):
            print("Password is win!!")
else:
    print("password is not win")
