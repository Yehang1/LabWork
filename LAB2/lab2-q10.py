#find sum of three integers
#if two inputs are same the sum is 0
a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if a==b or b==c or a==c:
    print("the sum is 0")
else:
    print("the sum is:",(a+b+c))