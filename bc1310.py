while True:
    try:
        entriesAmount = int(input())
        costPerDay = int(input())
        daysProfit = []

        for e in range(entriesAmount):
            value = int(input())
            daysProfit.append(value - costPerDay)

        bestSum = float('-inf')
        currentSum = 0

        for e in daysProfit:
            currentSum = max(e, currentSum + e)

            bestSum = max(bestSum, currentSum)

        print(max(bestSum, 0))

    except EOFError:
        break
