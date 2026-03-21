import sys
from common import get_sentences, get_words, setup_io

def checkTheCriteria(sentence):
    prev_first_char = ""
    number_of_words = 0
    for word in get_words(sentence):
        number_of_words += 1
        current_first_char = word[0].lower()

        if prev_first_char and current_first_char == prev_first_char:
            return False

        prev_first_char = current_first_char

    return number_of_words >= 6

def printSentences(output_callback):
    setup_io()


    try:

        for sentence in get_sentences():
            if checkTheCriteria(sentence):
                output_callback(sentence)



    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    printSentences(print)

if __name__ == '__main__':
    main()