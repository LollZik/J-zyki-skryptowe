from readLog import read_log
from collections import Counter


def find_most_used_uid(log):
    best_session = Counter(entry[1] for entry in log).most_common(1)

    if best_session:
        return best_session[0]
    return None


def main():
    data = read_log()
    active_session = find_most_used_uid(data)

    if active_session:
        uid, count = active_session
        print(f"Most common UID session: {uid} with: {count} requests")


if __name__ == "__main__":
    main()