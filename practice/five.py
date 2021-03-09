''' A school decided to replace the desk in three classroom,each desk sits two students
given the number of students in each class
print the smallest possible number of desks that can be purchased'''

no_student_class1=int(input("the number of students in first class"))
no_student_class2=int(input("the number of students in second class"))
no_student_class3=int(input("the number of students in third class"))
total_students=no_student_class1+no_student_class2+no_student_class3
number_of_bench=total_students/2
number=round(number_of_bench)

print("the number of bench is",number)

