while True:
    try:

        entries = input().split(' ')
        studentsquantity = int(entries[0])
        studentDrawnPosition = int(entries[1]) - 1
        students = []

        for _ in range(studentsquantity):
            student = input()
            students.append(student)

        students.sort()

        print(students[studentDrawnPosition])

    except EOFError:
        break
