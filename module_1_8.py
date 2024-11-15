grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
students_list.sort()
students_grades = dict(zip(students_list, grades))

for i in students_grades:
    students_grades[i] = sum(students_grades[i])/len(students_grades[i])
print(students_grades)