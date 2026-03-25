from readLog import read_log


def get_unique_methods(log):
    unique_methods = []
    for entry in log:
        method = entry[6]
        if method not in unique_methods:
            unique_methods.append(method)
    return unique_methods

def main():
    data = read_log()
    log = get_unique_methods(data)
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()