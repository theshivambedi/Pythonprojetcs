student_score = (input("Put marks of all the students\n")).split()
for i in range(len(student_score)):
    student_score[i] = int(student_score[i])
print(student_score)
highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score
print(highest_score)        
    