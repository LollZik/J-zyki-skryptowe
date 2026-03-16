import sys
from common import processLine

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main(process_line):
    lineCount = 0
    emptyStreak = 0
    preamblePossible = True
    preambleSkipped = False

    for line in sys.stdin:
        line = line.rstrip("\n")
        lineCount += 1

        if line.strip() == "-----":
            return

        if not preambleSkipped and preamblePossible:
            if line.strip() == "":
                emptyStreak += 1
            else:
                emptyStreak = 0

            if emptyStreak >= 2:
                preambleSkipped = True
                continue

            if lineCount >= 10:
                preamblePossible = False

            continue

        processed = process_line(line)
        print(processed)


if __name__ == "__main__":
    main(processLine)