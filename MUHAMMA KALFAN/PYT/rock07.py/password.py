password=input("Enter thr password:-")
if len(password)>=8 and any(i.isupper() for i in password)and any(i.islower()for i in password)and any(i.isdigit()for i in password):
    print("Valid Password")
else:
    print("In Valid Password")