import sys


def countCharacters(output_callback):
    count = 0
    try:
        for line in sys.stdin:
            for char in line:
                if not char.isspace():
                    count += 1

        output_callback(count)

    except UnicodeDecodeError:
        sys.stderr.write("Encoding error: The input file must be in UTF-8 format.\n")
    except BrokenPipeError:
        sys.stderr.write("Broken pipe: The pipeline was interrupted by the parent process.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {e}\n")


def main():
    countCharacters(print)


if __name__ == '__main__':
    main()