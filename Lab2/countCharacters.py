import sys

def main():
    text = sys.stdin.read()
    if text:
        count = 0
        for char in text:
            if not char.isspace():
                count += 1
        print(count)
    else:
        print("0")

if __name__ == '__main__':
    main()
