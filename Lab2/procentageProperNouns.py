import sys

def main():
    text = sys.stdin.read()
    if text:
        allSentences = 0
        sentencesWithProperNouns = 0

        inSentence = False
        firstWordFinished = False
        inWord = False
        foundProperInPara = False

        for char in text:
            if char in ".?!":
                if inSentence:
                    allSentences += 1
                    if foundProperInPara:
                        sentencesWithProperNouns += 1
                inSentence = False
                firstWordFinished = False
                inWord = False
                foundProperInPara = False

            elif not char.isspace():
                if not inSentence:
                    inSentence = True

                if not inWord:
                    if firstWordFinished and char.isupper():
                        foundProperInPara = True
                    inWord = True

            else:
                if inWord:
                    inWord = False
                    firstWordFinished = True

        if inSentence:
            allSentences += 1
            if foundProperInPara:
                sentencesWithProperNouns += 1

        if allSentences > 0:
            print((sentencesWithProperNouns / allSentences) * 100)
        else:
            print("0")
    else:
        print("0")

if __name__ == '__main__':
    main()