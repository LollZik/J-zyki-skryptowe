from readLog import read_log

def get_most_active_ips(log):
    counts = {}
    time_map = {}

    for entry in log:
        timestamp = entry[0]
        ip = entry[2]

        time_map.setdefault(ip, []).append(timestamp)
        counts[ip] = counts.get(ip, 0) + 1

    result = {}
    for ip, timestamps in time_map.items():
        if counts[ip] >= 2:
            timestamps.sort()

            total_duration = 0
            previous_t = timestamps[0]

            for t in timestamps:
                diff = t - previous_t
                total_duration += diff.total_seconds()
                previous_t = t

            result[ip] = total_duration

    if not result:
        return None

    return max(result.items(), key=lambda x: x[1])


def main():
    data = read_log()
    log = get_most_active_ips(data)
    print(log)

if __name__ == "__main__":
    main()