import sys
from common import get_sentences,setup_io, get_words


def count_target_words(sentence):
    count = 0
    for word in get_words(sentence):
        w = word.lower()
        if w == "i" or w == "oraz" or w == "ale" or w == "że" or w == "lub":
            count += 1
    return count


def filter_conjunction_sentences(output_callback):
    setup_io()

    try:
        for sentence in get_sentences():
            if count_target_words(sentence) >= 2:
                output_callback(sentence)

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    filter_conjunction_sentences(print)

if __name__ == '__main__':
    main()