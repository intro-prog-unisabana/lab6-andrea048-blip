def assignment_averages(students):
    result = {}

    # ✅ SOLUCIÓN CLAVE
    if len(students) == 0:
        return result

    first_student = next(iter(students.values()))

    for assignment in first_student.keys():
        total = 0
        count = 0

        for student in students.values():
            total += student[assignment]
            count += 1

        result[assignment] = round(total / count)

    return result