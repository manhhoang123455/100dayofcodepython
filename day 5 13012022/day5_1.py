student_heights = input("input a list of student heights: ").split()

for n in range(0 ,len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
for height in student_heights:
    total += height

number_student = len(student_heights)

print(total // number_student)