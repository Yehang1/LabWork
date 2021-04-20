#WAP which accepts marks of four subjects and display total marks ,percentage,grades
sub1=float(input("enter the marks"))
sub2=float(input("enter the marks"))
sub3=float(input("enter the marks"))
sub4=float(input("enter the marks"))

total=sub1+sub2+sub3+sub4
print("your total marks is:",total)
percentage=(total/400)*100
print("your percentage is:",percentage)
if percentage>80:
    print("your grade is A")
eleif percentage