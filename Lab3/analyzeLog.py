from readLog import read_log
from getTopIPs import get_top_ips
from topUris import get_top_uris
from countByMethod import count_by_method
from getFailedReads import get_failed_reads
from detectSus import detect_sus


def analyze_log(log):
    return {
        "top_ips": get_top_ips(log),
        "top_uris": get_top_uris(log, 5),
        "methods": count_by_method(log),
        "errors": len(get_failed_reads(log, merge=True)),
        "total_requests": len(log),
        "suspicious_ips": detect_sus(log, 1000)
    }

def main():
    data = read_log()
    log = analyze_log(data)
    print(log)

if __name__ == "__main__":
    main()