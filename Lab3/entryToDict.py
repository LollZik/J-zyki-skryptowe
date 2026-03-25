from readLog import read_log

def entry_to_dict(entry):
    return {
        "ts": entry[0],
        "uid": entry[1],
        "orig_h": entry[2],
        "orig_p": entry[3],
        "resp_h": entry[4],
        "resp_p": entry[5],
        "method": entry[6],
        "host": entry[7],
        "uri": entry[8],
        "status": entry[9]
    }

def main():
    data = read_log()
    for entry in data:
        print(entry_to_dict(entry))

if __name__ == "__main__":
    main()