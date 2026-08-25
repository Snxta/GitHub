name=input ("Enter your name:")
if len(name) <3:
    print("Name must be atleast 3 character long")
elif len(name) >50:
    print("Name must be maximum of 50 Character")
else:
    print("Name looks good!")