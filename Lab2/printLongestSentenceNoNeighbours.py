import sys
from common import get_sentences,setup_io,get_words


def has_no_same_letter_neighbours(sentence):
    prev_first_char = ""

    for word in get_words(sentence):
        current_first_char = word[0].lower()

        if prev_first_char and current_first_char == prev_first_char:
            return False

        prev_first_char = current_first_char

    return True

def printLongestSentenceNoNeighbours(output_callback):
    setup_io()

    longest_sentence = ""

    try:
        for sentence in get_sentences():
            if has_no_same_letter_neighbours(sentence):
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
    printLongestSentenceNoNeighbours(print)

if __name__ == '__main__':
    main()