import sys
from common import get_sentences

def count_commas(sentence):
    count = 0
    for char in sentence:
        if char == ',':
            count += 1
    return count


def findFirstComplexSentence(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    try:
        for sentence in get_sentences():
            if count_commas(sentence) > 1:
                output_callback(sentence)
                return
    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    findFirstComplexSentence(print)


if __name__ == '__main__':
    main()