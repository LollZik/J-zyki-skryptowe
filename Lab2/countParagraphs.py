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

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    countParagraphs(print)

if __name__ == '__main__':
    main()