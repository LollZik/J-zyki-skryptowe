from readLog import read_log
from datetime import datetime


def get_entries_in_time_range(log, start, end):
    return [e for e in log if start <= e[0] < end]

def main():
    data = read_log()
    log = get_entries_in_time_range(data, datetime(2012, 3, 16, 15, 35, 38, 60000), datetime(2012, 3, 16, 15, 35, 38, 120000))
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()