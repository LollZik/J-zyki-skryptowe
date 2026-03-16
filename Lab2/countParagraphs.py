import sys

def main():
    text = sys.stdin.read()
    if text:
        paragraphs = 0
        inParagraph = False
        for line in text.splitlines():
            if line.strip() == "":
                in_para = False
            else:
                if not in_para:
                    paragraphs += 1
                    inParagraph = True
        print(paragraphs)
    else:
        print("0")

if __name__ == '__main__':
    main()