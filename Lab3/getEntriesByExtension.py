from readLog import read_log


def get_entries_by_extension(log, ext):
    results = []
    extension_str = f".{ext}"
    for entry in log:
        uri = entry[8] .split('?')[0]

        if uri.endswith(extension_str):
            results.append(entry)
    return results

def main():
    data = read_log()
    log = get_entries_by_extension(data, "jpg")
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()