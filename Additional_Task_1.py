# Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

if len(grades) != len(students):
    print('Кол-во групп оценок не совпадает с кол-вом студентов')
else:
    students = sorted(list(students), key = str)
    print('Отсортированный список студентов:', students, sep = '\n')

    dict_students_grades = []
    for num in range(len(students)):
        student_grade = [] #Создаем временный пустой список

        student_grade.append(students[num])
        grade = sum(grades[num]) / len(grades[num])
        student_grade.append(grade)

        dict_students_grades.append(student_grade) 

    dict_students_grades = dict(dict_students_grades)
    print(dict_students_grades)
