import sys

from common import get_sentences


def get_first_20_sentences(output_callback):
    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')
    count = 0

    try:
        for sentence in get_sentences():
            output_callback(sentence)
            count += 1
            if count >= 20:
                break

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")


def main():
    get_first_20_sentences(print)

if __name__ == '__main__':
    main()