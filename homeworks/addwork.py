grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(list(students))
students_average = {}
for (index, item) in enumerate(students_sorted):
    sum_average = 0
    sum_average = (sum(grades[index])/(len(grades[index])))
    students_average[item] = sum_average
print(students_average)
