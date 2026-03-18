import sys
from common import get_sentences


def count_words(sentence):
    word_count = 0
    in_word = False

    for char in sentence:
        if char.isalpha():
            in_word = True
        else:
            if in_word:
                word_count += 1
                in_word = False

    if in_word:
        word_count += 1

    return word_count


def filter_short_sentences(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    for sentence in get_sentences():
        if 0 < count_words(sentence) <= 4:
            output_callback(sentence)


def main():
    filter_short_sentences(print)


if __name__ == '__main__':
    main()