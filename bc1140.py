# -*- coding: utf-8 -*-

while True:
    try:
        entry = input()
        isTautogram = True
        words = entry.split()
        firstLetter = words[0][0].lower()

        if "*" in words:
            isTautogram = False
            break

        for word in words:
            if (word[0].lower() != firstLetter):
                isTautogram = False
                break

        if isTautogram:
            print("Y")
        else:
            print("N")

    except EOFError:
        break
