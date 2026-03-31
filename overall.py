def student_averages(students):
    result = {}

    for student, grades in students.items():
        if len(grades) == 0:
            result[student] = 0
        else:
            total = sum(grades.values())
            count = len(grades)
            result[student] = round(total / count)

    return result


def assignment_averages(students):
    result = {}


    if len(students) == 0:
        return result

    # Obtener tareas del primer estudiante
    first_student = next(iter(students.values()))

    for assignment in first_student.keys():
        total = 0
        count = 0

        for student in students.values():
            total += student[assignment]
            count += 1

        result[assignment] = round(total / count)

    return result