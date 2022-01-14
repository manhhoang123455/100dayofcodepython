# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

heightest_student = student_scores[0]

for score in student_scores:
    if heightest_student < score:
        heightest_student = score

print(heightest_student)
