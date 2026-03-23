import sys
from readLog import read_log

def sort_log(log, index):
    try:
        return sorted(log, key=lambda x: x[index])
    except IndexError:
        sys.stderr.write("Wrong index\n")

def main():
    data = read_log()
    log = sort_log(data, 1)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()