import sys
from common import get_sentences


def has_no_same_letter_neighbours(sentence):
    prev_first_char = ""
    in_word = False

    for char in sentence:
        if char.isalpha():
            if not in_word:
                current_first_char = char.lower()
                if prev_first_char and current_first_char == prev_first_char:
                    return False

                prev_first_char = current_first_char
                in_word = True
        else:
            in_word = False

    return True

def printLongestSentenceNoNeighbours(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

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

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    printLongestSentenceNoNeighbours(print)

if __name__ == '__main__':
    main()