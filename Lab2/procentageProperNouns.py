import sys
from common import get_sentences, setup_io, get_words


def has_proper_noun(sentence):
    is_first_word = True

    for word in get_words(sentence):
        if is_first_word:
            is_first_word = False
            continue

        if word[0].isupper():
            return True

    return False


def calculate_proper_nouns_percentage(output_callback):
    setup_io()

    total_sentences = 0
    sentences_with_proper_nouns = 0

    try:
        for sentence in get_sentences():
            total_sentences += 1
            if has_proper_noun(sentence):
                sentences_with_proper_nouns += 1

        if total_sentences > 0:
            percentage = (sentences_with_proper_nouns / total_sentences) * 100
            output_callback(str(percentage)+"%")
        else:
            output_callback("0%")

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")

def main():
    calculate_proper_nouns_percentage(print)

if __name__ == '__main__':
    main()