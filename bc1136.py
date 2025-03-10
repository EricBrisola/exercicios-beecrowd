while True:
    try:
        entryValues1 = input().split()
        highestValue = int(entryValues1[0])
        numOfBallsInTheGlobe = int(entryValues1[1])

        if (highestValue == 0 and numOfBallsInTheGlobe == 0):
            break

        ballsInTheGlobe = list(map(int, input().split()))
        absoluteDiffs = [False] * (highestValue + 1)
        absoluteDiffs[0] = True

        for i in range(len(ballsInTheGlobe)):
            for j in range(i + 1, len(ballsInTheGlobe)):
                absoluteDiffs[abs(ballsInTheGlobe[i] -
                                  ballsInTheGlobe[j])] = True

        if (False in absoluteDiffs):
            print("N")
        else:
            print("Y")

    except EOFError:
        break
