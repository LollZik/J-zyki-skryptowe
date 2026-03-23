import sys
from readLog import read_log
import ipaddress

def get_entries_by_addr(log, addr):
    try:
        ipaddress.ip_address(addr)
    except ValueError:
        sys.stderr.write("Wrong IP address.")
    return [e for e in log if e[2] == addr or e[7] == addr]

def main():
    data = read_log()
    log = get_entries_by_addr(data, '192.168.202.110')
    for entry in log:
        print(entry)

if __name__ == "__main__":
    main()