while True:
    try:
        entryValues = input().split(" ")

        leftChildWeight = int(entryValues[0])
        leftSideSeesawLength = int(entryValues[1])

        rightChildWeight = int(entryValues[2])
        rightSideSeesawLength = int(entryValues[3])

        if leftChildWeight * leftSideSeesawLength == rightChildWeight * rightSideSeesawLength:
            print('0')
        elif leftChildWeight * leftSideSeesawLength < rightChildWeight * rightSideSeesawLength:
            print('1')
        else:
            print('-1')

    except EOFError:
        break
