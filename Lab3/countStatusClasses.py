from readLog import read_log
def count_status_classes(log):
    classes = {"2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}
    for entry in log:
        status = entry[9]
        if status == 0:
            continue

        first_digit = status // 100
        key = f"{first_digit}xx"
        if key in classes:
            classes[key] += 1

    return classes

def main():
    data = read_log()
    log = count_status_classes(data)
    for code, count in log.items():
        print(f"{code} : {count}")

if __name__ == "__main__":
    main()