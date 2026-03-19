import sys
from common import get_sentences,setup_io

def count_commas(sentence):
    count = 0
    for char in sentence:
        if char == ',':
            count += 1
    return count


def findFirstComplexSentence(output_callback):
    setup_io()

    try:
        for sentence in get_sentences():
            if count_commas(sentence) > 1:
                output_callback(sentence)
                return

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    findFirstComplexSentence(print)


if __name__ == '__main__':
    main()