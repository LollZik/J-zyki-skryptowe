import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def main():
    text = sys.stdin.read()
    if text:
        longestSentence = ""
        currentSentence = ""

        inWord = False
        isValid = True
        prevFirstChar = ""

        for char in text:
            if char in ".?!":
                if isValid and len(longestSentence) < len(currentSentence) + 1:
                    longestSentence = currentSentence + char

                isValid = True
                inWord = False
                prevFirstChar = ""
                currentSentence = ""
            else:
                currentSentence += char
                if char.isspace():
                    inWord = False
                elif not inWord:
                    if char.lower() == prevFirstChar.lower():
                        isValid = False
                    inWord = True
                    prevFirstChar = char


        if isValid and len(longestSentence) < len(currentSentence) + 1:
            longestSentence = currentSentence

        print(longestSentence)
    else:
        print("No sentences")

if __name__ == '__main__':
    main()