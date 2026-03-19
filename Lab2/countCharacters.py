import sys


def countCharacters(output_callback):
    count = 0
    try:
        for line in sys.stdin:
            for char in line:
                if not char.isspace():
                    count += 1

        output_callback(count)

    except Exception as e:
        sys.stderr.write(f"Error occured: {e}\n")


def main():
    countCharacters(print)


if __name__ == '__main__':
    main()