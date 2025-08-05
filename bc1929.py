while True:
    try:
        stickValues = input().split(' ')

        stickValues = [int(x) for x in stickValues]

        a = stickValues[0]
        b = stickValues[1]
        c = stickValues[2]
        d = stickValues[3]
        isTrianglePossible = False

        # a, b, c
        if a < b+c and b < a+c and c < a+b:
            isTrianglePossible = True

        # b, c, d
        if b < c+d and c < b+d and d < c+b:
            isTrianglePossible = True

        # a, b, d
        if a < b+d and b < a+d and d < a+b:
            isTrianglePossible = True

        # a, c, d
        if d < a+c and a < d+c and c < d+a:
            isTrianglePossible = True

        if isTrianglePossible:
            print('S')
        else:
            print('N')

    except EOFError:
        break
