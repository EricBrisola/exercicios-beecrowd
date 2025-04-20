from collections import deque

while True:
    try:

        boardSize = input().split(' ')
        lineNum = int(boardSize[0])
        columnNum = int(boardSize[1])
        board = []

        for _ in range(lineNum):
            line = list(input())
            board.append(line)

        playerPlays = int(input())

        positionsPlayed = []

        for _ in range(playerPlays):
            play = input().split()
            positionsPlayed.append(play)

        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        visited = [[False] * columnNum for _ in range(lineNum)]
        hit = [[False] * columnNum for _ in range(lineNum)]

        for e in positionsPlayed:
            line = int(e[0]) - 1
            column = int(e[1]) - 1

            hit[line][column] = True

        destroyedShips = 0

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))

            visited[x][y] = True
            shipParts = [(x, y)]

            while queue:
                cx, cy = queue.popleft()

                for dx, dy in neighbors:
                    nx = cx + dx
                    ny = cy + dy

                    isInLine = 0 <= nx < lineNum
                    isInColumn = 0 <= ny < columnNum

                    if isInLine and isInColumn:
                        isShipPart = board[nx][ny] == '#'
                        wasVisited = visited[nx][ny]
                        if isShipPart and not wasVisited:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            shipParts.append((nx, ny))

            destroyed = True

            for x, y in shipParts:
                if not hit[x][y]:
                    destroyed = False
                    break

            return destroyed

        for i in range(lineNum):
            for j in range(columnNum):
                if board[i][j] == '#' and not visited[i][j]:
                    if bfs(i, j):
                        destroyedShips += 1

        print(destroyedShips)
    except EOFError:
        break
