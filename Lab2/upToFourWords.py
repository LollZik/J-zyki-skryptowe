import sys
from common import get_sentences,setup_io, get_words


def count_words(sentence):
    word_count = 0
    for _ in get_words(sentence):
        word_count += 1
    return word_count


def filter_short_sentences(output_callback):
    try:
        setup_io()

        for sentence in get_sentences():
            if 0 < count_words(sentence) <= 4:
                output_callback(sentence)

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")


def main():
    filter_short_sentences(print)


if __name__ == '__main__':
    main()