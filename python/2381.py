n_students, picked_number = input().split()
n_students, picked_number = int(n_students), int(picked_number)
students = []

for i in range(n_students):
  students.append(input())

students.sort(key=lambda x: x)

print(students[picked_number-1])
