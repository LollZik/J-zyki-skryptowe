import sys
from common import get_sentences


def count_target_words(sentence):
    count = 0
    current_word = ""

    for char in sentence:
        if char.isalpha():
            current_word += char.lower()
        else: # word is finished
            # if current_word in [...]
            if current_word == "i" or current_word == "oraz" or current_word == "ale" or current_word == "że" or current_word == "lub":
                count += 1
            current_word = ""

    #If sentence doesn't end with punctiation
    if current_word == "i" or current_word == "oraz" or current_word == "ale" or current_word == "że" or current_word == "lub":
        count += 1

    return count


def filter_conjunction_sentences(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    try:
        for sentence in get_sentences():
            if count_target_words(sentence) >= 2:
                output_callback(sentence)

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    filter_conjunction_sentences(print)

if __name__ == '__main__':
    main()