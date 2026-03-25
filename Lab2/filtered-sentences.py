import sys

from common import processLine, setup_io, get_words
from upToFourWords import count_words


def get_sentences(string):
    sentence_buffer = ""
    consecutive_newlines = 0
    last_was_space = False
    i = 0
    while i < len(string):
        char = string[i]
        if not char:
            break
        if char == '\r':
            i+=1

        if char == '\n':
            sentence_buffer += char
            i+=1

            consecutive_newlines += 1
            if consecutive_newlines >= 2:
                clean = sentence_buffer.strip()
                if clean:
                    yield clean+"\n"
                sentence_buffer = ""
                last_was_space = False
            else:
                if sentence_buffer and not last_was_space:
                    sentence_buffer += " "
                    last_was_space = True
        else:
            i+=1
            consecutive_newlines = 0
            # if char in ".?!…" if we'd rather include "…" too
            if char in ".?!":
                sentence_buffer += char
                clean = sentence_buffer.strip()
                if clean:
                    yield clean
                sentence_buffer = ""
                last_was_space = False
            elif char.isspace():
                if sentence_buffer and not last_was_space:
                    sentence_buffer += " "
                    last_was_space = True
            else:
                sentence_buffer += char
                last_was_space = False

    clean = sentence_buffer.strip()
    if clean:
        yield clean

def filter(sentence):
    prev = ""
    for word in get_words(sentence):
        if not (word[0].lower() == prev.lower()):
            return False
        else:
            prev = word[0].lower()
    return True


def filtered_sentences(output_callback):
    giantString = ""
    try:
        setup_io()

        line_count = 0
        empty_streak = 0
        checking_preamble = True
        buffer = ""  # To save first 10 lines if there's no preamble

        for line in sys.stdin:
            line = line.replace('\r', '').rstrip('\n')
            if line.strip() == "-----":
                break
            processed_line = processLine(line)

            if checking_preamble:
                line_count += 1
                buffer += processed_line + "\n"

                if line.strip() == "":
                    empty_streak += 1
                else:
                    empty_streak = 0

                if empty_streak >= 2:
                    checking_preamble = False
                    buffer = ""
                    continue
                if line_count >= 10:
                    checking_preamble = False
                    giantString += (buffer.rstrip('\n'))

                continue
            giantString += (processed_line)

        for sentence in get_sentences(giantString):
            if count_words(sentence) >= 6:
                if filter:
                    output_callback(sentence+"\n")


    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")


def main():
    filtered_sentences(print)


if __name__ == '__main__':
    main()