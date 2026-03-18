import sys

def processLine(line):
    stripped = line.strip()
    if not stripped:
        return ""

    result = ""
    last_was_space = False

    for char in stripped:
        if char.isspace():
            if not last_was_space: # Merge multiple spaces into one
                result += " "
                last_was_space = True
        else:
            result += char
            last_was_space = False

    return result


def get_sentences():

    sentence_buffer = ""
    consecutive_newlines = 0
    last_was_space = False

    try:
        while True:
            char = sys.stdin.read(1)
            if not char:
                break
            if char == '\r':
                continue

            if char == '\n':
                consecutive_newlines += 1
                if consecutive_newlines >= 2:
                    clean = sentence_buffer.strip()
                    if clean:
                        yield clean
                    sentence_buffer = ""
                    last_was_space = False
                else:
                    if sentence_buffer and not last_was_space:
                        sentence_buffer += " "
                        last_was_space = True
            else:
                consecutive_newlines = 0
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

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")