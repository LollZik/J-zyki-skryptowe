import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')


def main():
    text = sys.stdin.read()
    if text:
        longestSentence = ""
        currentSentence = ""

        for char in text:
            if char in ".?!":
                if len(longestSentence) < len(currentSentence) + 1:
                    longestSentence = currentSentence + char

                currentSentence = ""
            else:
                currentSentence += char

        if len(longestSentence) < len(currentSentence) + 1:
            longestSentence = currentSentence

        print(longestSentence)
    else:
        print("No sentences")

if __name__ == '__main__':
    main()