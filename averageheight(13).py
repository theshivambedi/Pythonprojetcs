#changing data type of list to integer to string
student_heights = (input("Put the heights of all the students\n")).split()
for i in range(len(student_heights)):
    student_heights[i] = int(student_heights[i])
print(student_heights)

#finding total height
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

#finding number of students
students = 0
for count in student_heights:
    students += 1
print(students)    

#now finding average height  
average_height = total_height/students

print(f"The average height of class is {average_height}")
