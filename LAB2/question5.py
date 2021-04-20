#take input from the user about their weight ,if it is in kg convert into lbs vice vers if no units print didnt understand

weight=float(input("enter your weight"))
siunit=str(input("enter the SI unit of your weight"))
if siunit=="kg":
    new_weight=weight*2.2
    print("your weight in lbs is",new_weight)
elif siunit=="lbs":
    new_weight=weight/2.2
    print("your weight in kgs is",new_weight)
else:
    print("did not understand")