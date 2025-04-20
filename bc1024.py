while True:
    try:

        entriesAmount = int(input())

        for _ in range(entriesAmount):
            word = input()

            newWord = ''
            for e in word:
                if e.isalpha():
                    newWord += chr(ord(e) + 3)
                else:
                    newWord += e

            reversedNewWord = newWord[::-1]
            halfIndex = len(reversedNewWord) // 2
            finalWord = ''

            for i in range(halfIndex):
                finalWord += reversedNewWord[i]

            for i in range(halfIndex, len(reversedNewWord)):
                finalWord += chr(ord(reversedNewWord[i]) - 1)

            print(finalWord)

    except EOFError:
        break
    except ValueError:
        break
