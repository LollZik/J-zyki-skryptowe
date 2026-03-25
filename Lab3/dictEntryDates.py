from collections import Counter
from readLog import read_log
from logToDict import log_to_dict


def print_dict_entry_dates(log_dict):
    for uid, entries in log_dict.items():
        total_requests = len(entries)

        client_ips = set(e["orig_h"] for e in entries)
        hosts = set(e["host"] for e in entries)

        timestamps = [e["ts"] for e in entries]
        first_req = min(timestamps)
        last_req = max(timestamps)

        methods = [e["method"] for e in entries]
        method_counts = Counter(methods)

        codes_2xx_count = sum(1 for e in entries if 200 <= e["status"] < 300)

        print(f"=== Sesja UID: {uid} ===")
        print(f"Adresy IP klienta: {', '.join(client_ips)}")
        print(f"Odwiedzone hosty: {', '.join(hosts)}")
        print(f"Liczba żądań: {total_requests}")
        print(f"Pierwsze żądanie: {first_req}")
        print(f"Ostatnie żądanie: {last_req}")

        print("Procentowy udział metod HTTP:")
        for method, count in method_counts.items():
            percentage = (count / total_requests) * 100
            print(f"  - {method}: {percentage:.2f}%")

        ratio = (codes_2xx_count / total_requests) * 100
        print(f"Kody 2xx: {codes_2xx_count}/{total_requests} ({ratio:.2f}%)")
        print("-" * 40)


def main():
    data = read_log()
    sessions = log_to_dict(data)
    print_dict_entry_dates(sessions)

if __name__ == "__main__":
    main()