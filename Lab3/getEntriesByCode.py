import sys
from readLog import read_log

def get_entries_by_code(log, code):
    if not isinstance(code, int):
        sys.stderr.write("Code HTTP has to be an integer.")
    return [entry for entry in log if entry[5] == code]

def main():
    data = read_log()
    log = get_entries_by_code(data, 80)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()