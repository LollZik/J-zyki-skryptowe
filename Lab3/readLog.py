import sys
from datetime import datetime

def read_log():
    log_data = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        fields = line.split('\t')
        try:
            ts = datetime.fromtimestamp(float(fields[0]))
            uid = fields[1]
            orig_h = fields[2]
            orig_p = int(fields[3])
            resp_h = fields[4]
            resp_p = int(fields[5])
            method = fields[7]
            host = fields[8]
            uri = fields[9]
            status = int(fields[14]) if fields[14] != '-' else 0

            log_data.append((ts, uid, orig_h, orig_p, resp_h, resp_p, method, host, uri, status))
        except (ValueError, IndexError) as e:
            sys.stderr.write("Error while reading\n")
    return log_data

def main():
    data = read_log()
    for entry in data:
        print(entry)

if __name__ == "__main__":
    main()