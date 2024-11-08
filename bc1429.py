# -*- coding: utf-8 -*-

def factorial(num: int) -> int:
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


while True:
    try:
        entryValues = list(input())
        finalValue = 0

        if entryValues == 0:
            break

        entryLen = len(entryValues)

        for value in entryValues:
            finalValue += int(value) * factorial(entryLen)

            if (entryLen > 0):
                entryLen -= 1
            else:
                entryLen = 0

        if finalValue != 0:
            print(finalValue)

    except EOFError:
        break
