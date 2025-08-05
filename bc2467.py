while True:
    try:
        entries = input().split(' ')
        boardLength = int(entries[0])
        numberOfOperations = int(entries[1])

        board = []

        for _ in range(boardLength):
            board.append([0 for _ in range(boardLength)])

        for e in range(numberOfOperations):
            operationEntries = input().split(' ')
            entriesAsInts = [int(e) for e in operationEntries]
            operationType = entriesAsInts[0]

            if operationType == 1:

                line = entriesAsInts[1]
                value = entriesAsInts[2]

                board[line] = [value for _ in board[line]]

            elif operationType == 2:

                line = entriesAsInts[1]
                value = entriesAsInts[2]

                board[line] = [value for _ in board[line]]

            elif operationType == 3:

            else:

    except EOFError:
        break
