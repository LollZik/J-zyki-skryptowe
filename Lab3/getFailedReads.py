from readLog import read_log

def get_failed_reads(log, merge=False):
    e4xx = [e for e in log if 400 <= e[9] < 500]
    e5xx = [e for e in log if 500 <= e[9] < 600]
    return e4xx + e5xx if merge else (e4xx, e5xx)

def main():
    data = read_log()
    log = get_failed_reads(data, True)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()