from collections import Counter
from readLog import read_log


def get_top_uris(log, n = 10):
    uris = [entry[8] for entry in log]
    return [i for i,j in Counter(uris).most_common(n)]

def main():
    data = read_log()
    log = get_top_uris(data, 10)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()