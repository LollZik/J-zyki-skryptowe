from readLog import read_log


def get_session_paths(log):
    paths_dict = {}

    for entry in log:
        uid = entry[1]
        uri = entry[8]

        paths_dict.setdefault(uid, []).append(uri)

    return dict(paths_dict)


def main():
    data = read_log()
    session_paths = get_session_paths(data)

    if session_paths:
        best_uid = max(session_paths, key=lambda k: len(session_paths[k]))
        paths = session_paths[best_uid]

        print(f"UID: {best_uid}")
        print(f"Amount of visited paths: {len(paths)}")


if __name__ == "__main__":
    main()