#!/bin/python3

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade < 38:
            rounded_grades.append(grade)
        else:
            split_grade = list(str(grade))
            if int(split_grade[1]) in (0, 1, 2, 5, 6, 7):
                rounded_grades.append(grade)
            elif int(split_grade[1]) in (3, 8):
                rounded_grades.append(grade + 2)
            else:
                rounded_grades.append(grade + 1)
    return rounded_grades
