while True:
    try:
        entriesQuantity = int(input())

        evenNums = []
        oddNums = []

        for e in range(entriesQuantity):
            value = int(input())

            if value % 2 == 0:
                evenNums.append(value)
            else:
                oddNums.append(value)

        evenNums.sort()
        oddNums.sort(reverse=True)

        for num in evenNums:
            print(num)
        for num in oddNums:
            print(num)

    except EOFError:
        break
