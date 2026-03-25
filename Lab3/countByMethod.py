from readLog import read_log


def count_by_method(log):
    method_counts = {}
    for entry in log:
        method = entry[6]
        if method in method_counts:
            method_counts[method] += 1
        else:
            method_counts[method] = 1
    return method_counts

def main():
    data = read_log()
    log = count_by_method(data)
    print(log)

if __name__ == "__main__":
    main()