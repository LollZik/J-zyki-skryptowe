import sys

from common import get_sentences,setup_io


def get_first_20_sentences(output_callback):
    setup_io()
    count = 0

    try:
        for sentence in get_sentences():
            output_callback(sentence)
            count += 1
            if count >= 20:
                break


    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")


def main():
    get_first_20_sentences(print)

if __name__ == '__main__':
    main()