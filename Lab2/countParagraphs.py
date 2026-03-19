import sys

def countParagraphs(output_callback):
    paragraphs = 0
    inParagraph = False

    try:
        for line in sys.stdin:
            if line.strip() == "":
                inParagraph = False
            else:
                if not inParagraph:
                    paragraphs += 1
                    inParagraph = True

        output_callback(paragraphs)

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    countParagraphs(print)

if __name__ == '__main__':
    main()