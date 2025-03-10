while True:
    try:
        entry = input().split(' ')

        if entry[0] == '0' and entry[1] == '0':
            break

        diff = int(entry[1]) - int(entry[0])

        newFirstNum = int(entry[0]) - diff

        print(newFirstNum)

    except EOFError:
        break
