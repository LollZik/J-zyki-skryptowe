import sys
from common import get_sentences

def printLongestSentence(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    longest_sentence = ""

    try:
        for sentence in get_sentences():
            if len(sentence) > len(longest_sentence):
                longest_sentence = sentence

        if longest_sentence:
            output_callback(longest_sentence)
        else:
            output_callback("No sentences")

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")

def main():
    printLongestSentence(print)

if __name__ == '__main__':
    main()