import sys
from common import get_sentences,setup_io

def printLongestSentence(output_callback):
    setup_io()

    longest_sentence = ""

    try:
        for sentence in get_sentences():
            if len(sentence) > len(longest_sentence):
                longest_sentence = sentence

        if longest_sentence:
            output_callback(longest_sentence)
        else:
            output_callback("No sentences")

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    printLongestSentence(print)

if __name__ == '__main__':
    main()