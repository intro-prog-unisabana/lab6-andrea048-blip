def student_averages(students):
    result = {}

    for student, grades in students.items():
        total = sum(grades.values())
        count = len(grades)
        average = round(total / count)
        result[student] = average

    return result


def assignment_averages(students):
    result = {}

    # Tomar las tareas del primer estudiante
    first_student = next(iter(students.values()))

    for assignment in first_student.keys():
        total = 0
        count = 0

        for student in students.values():
            total += student[assignment]
            count += 1

        result[assignment] = round(total / count)

    return result