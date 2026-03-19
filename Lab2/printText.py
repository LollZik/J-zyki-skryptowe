import sys
from common import processLine,setup_io

def extract_content(output_callback):
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
                    output_callback(buffer.rstrip('\n'))

                continue
            output_callback(processed_line)

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")


def main():
    extract_content(print)

if __name__ == "__main__":
    main()