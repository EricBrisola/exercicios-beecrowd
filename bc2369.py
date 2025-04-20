while True:
    try:

        waterUsage = int(input())
        consumptionRangeTotal = 0
        waterPayment = 7

        prices = [
            [11, 1],
            [31, 2],
            [101, 5]
        ]

        if waterUsage >= prices[2][0]:
            consumptionRangeTotal = waterUsage - prices[2][0] + 1
            waterPayment += (consumptionRangeTotal * prices[2][1])
            waterUsage = waterUsage - consumptionRangeTotal

        if waterUsage >= prices[1][0]:
            consumptionRangeTotal = waterUsage - prices[1][0] + 1
            waterPayment += (consumptionRangeTotal * prices[1][1])
            waterUsage = waterUsage - consumptionRangeTotal

        if waterUsage >= prices[0][0]:
            consumptionRangeTotal = waterUsage - prices[0][0] + 1
            waterPayment += (consumptionRangeTotal * prices[0][1])
            waterUsage = waterUsage - consumptionRangeTotal

        print(waterPayment)

    except EOFError:
        break
