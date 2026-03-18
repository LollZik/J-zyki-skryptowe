import sys

def main():
    paragraphs = 0
    inParagraph = False
    for line in sys.stdin:
        if line.strip() == "":
            inParagraph = False
        else:
            if not inParagraph:
                paragraphs += 1
                inParagraph = True
    print(paragraphs)

if __name__ == '__main__':
    main()