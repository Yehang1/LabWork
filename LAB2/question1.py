#WAP check whether 5 is in the list of first 5 natural numbers or not
list=[1,2,3,4,5]
a=5
for i in list:
    if i==a:
        c=1

if c==1:
    print(f'{a} is in the list')
else:
    print("it is not on the list")
