from readLog import read_log
from entryToDict import entry_to_dict

def log_to_dict(log):
    dictionairy = {}
    for entry in log:
        dict = entry_to_dict(entry)
        uid = dict["uid"]
        dictionairy.setdefault(uid,[]).append(dict)
    return dictionairy

def main():
    data = read_log()
    for entry in log_to_dict(data):
        print(entry)


if __name__ == "__main__":
    main()