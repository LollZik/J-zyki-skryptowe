from readLog import read_log


def get_top_ips(log, n=10):
    counts = {}
    for entry in log:
        ip = entry[2]
        if ip in counts:
            counts[ip] += 1
        else:
            counts[ip] = 1

    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)

    return items[:n]

def main():
    data = read_log()
    log = get_top_ips(data)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()