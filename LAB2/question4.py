'''if name is less tha 3 character print must be more than 3,
if name is more than 50 print must be 50 at most
else print name is good'''

name=str(input("enter your name "))
if len(name)<3:
    print("the characters must be more than 3")
elif len(name)>50:
    print("the charcaters must be of 50 atmost")
else:
    print("name looks good!")

