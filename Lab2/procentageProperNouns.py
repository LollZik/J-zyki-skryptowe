import sys
from common import get_sentences


def has_proper_noun(sentence):
    is_first_word = True
    in_word = False

    for char in sentence:
        if char.isalpha():
            if not in_word:
                in_word = True

                if is_first_word:
                    is_first_word = False
                else:
                    if char.isupper():
                        return True
        else:
            in_word = False

    return False


def calculate_proper_nouns_percentage(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    total_sentences = 0
    sentences_with_proper_nouns = 0

    try:
        for sentence in get_sentences():
            total_sentences += 1
            if has_proper_noun(sentence):
                sentences_with_proper_nouns += 1

        if total_sentences > 0:
            percentage = (sentences_with_proper_nouns / total_sentences) * 100
            output_callback(percentage)
        else:
            output_callback("0")

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    calculate_proper_nouns_percentage(print)

if __name__ == '__main__':
    main()