# Задание "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
if len(grades) != len(students): #На всякий случай проверка кол-ва студентов и групп оценок
    print('Кол-во групп оценок не совпадает с кол-вом студентов')
else:
    students = sorted(list(students), key = str) #Преобразование множества в список и его сортировка по алфавиту
    print('Отсортированный список студентов:', students, sep = '\n')

    dict_students_grades = []
    for num in range(len(students)):
        student_grade = [] #Создаем временный пустой список

        student_grade.append(students[num]) #Добавляем во временный список имя студента
        grade = sum(grades[num]) / len(grades[num]) #Вычисляем его среднюю оценку
        student_grade.append(grade) #Добавляем среднюю оценку во временный список

        dict_students_grades.append(student_grade) #Временный список с именем и оценкой добавляем отдельным элементом в общий список

    dict_students_grades = dict(dict_students_grades) #Преобразование общего списка в словарь
    print(dict_students_grades)