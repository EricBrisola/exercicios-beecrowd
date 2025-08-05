while True:
    try:
        squareDimension = int(input())
        square = []

        for e in range(squareDimension):
            rawValues = input().split(' ')
            squareLine = [int(e) for e in rawValues]
            square.append(squareLine)

        sumMap = {}

        for line in square:
            lineSum = 0
            for e in line:
                lineSum += e

            if not sumMap.get(lineSum):
                sumMap[lineSum] = [line]
            else:
                accumulated = sumMap.get(lineSum)
                sumMap[lineSum].append(line)

        convertedValues = list(sumMap.values())
        dictKeys = list(sumMap.keys())

        rightSum = dictKeys[0]
        wrongSum = dictKeys[1]

        lineSums = []
        columnSums = []

        col, line = 0, 0

        # lineSums = [0]*squareDimension
        # columnSums = [0]*squareDimension

        # for line in range(squareDimension):
        #     for column in range(squareDimension):
        #         value = square[line][column]
        #         lineSums[line] += value
        #         columnSums[column] += value

        while col < len(square[0]):
            currentColSum = 0
            while line < len(square[0]):
                currentColSum += square[line][col]
                line += 1
            columnSums.append(currentColSum)
            col += 1
            line = 0

        for e in square:
            currentLineSum = 0
            for j in e:
                currentLineSum += j
            lineSums.append(currentLineSum)

        wrongSumIdx = [None, None]

        for e in range(len(lineSums)):
            if lineSums[e] != rightSum:
                wrongSumIdx[0] = e
            if columnSums[e] != rightSum:
                wrongSumIdx[1] = e

        wrongValue = square[wrongSumIdx[0]][wrongSumIdx[1]]

        if rightSum < wrongSum:
            print(wrongValue + (rightSum - wrongSum), wrongValue)
        else:
            print(wrongValue - (wrongSum - rightSum), wrongValue)

    except EOFError:
        break
