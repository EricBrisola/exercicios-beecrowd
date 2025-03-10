while True:
    try:
        numsQuantity = input()
        binosList = input().split()

        multiplesOf2, multiplesOf3, multiplesOf4, multiplesOf5 = 0, 0, 0, 0

        for num in binosList:
            aux = int(num)
            if (aux % 5 == 0):
                multiplesOf5 += 1

            if (aux % 4 == 0):
                multiplesOf4 += 1

            if (aux % 3 == 0):
                multiplesOf3 += 1

            if (aux % 2 == 0):
                multiplesOf2 += 1

        print(f'{multiplesOf2} Multiplo(s) de 2\n{multiplesOf3} Multiplo(s) de 3\n{multiplesOf4} Multiplo(s) de 4\n{multiplesOf5} Multiplo(s) de 5')

    except EOFError:
        break
