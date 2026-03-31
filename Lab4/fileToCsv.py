import sys
import csv
import io
from collections import Counter

def process_file():
    file_path = sys.stdin.read().strip()
    if not file_path:
        return
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return

    chars_count = len(content)
    words = content.split()
    words_count = len(words)
    lines_count = len(content.splitlines())

    most_freq_char = ""
    char_freq = 0
    if chars_count > 0:
        top_char = Counter(content).most_common(1)[0]
        most_freq_char = top_char[0]
        char_freq = top_char[1]

    most_freq_word = ""
    word_freq = 0
    if words_count > 0:
        top_word = Counter(words).most_common(1)[0]
        most_freq_word = top_word[0]
        word_freq = top_word[1]

    output = io.StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow([
        file_path,
        chars_count,
        words_count,
        lines_count,
        most_freq_char,
        char_freq,
        most_freq_word,
        word_freq
    ])
    print(output.getvalue().strip())

if __name__ == "__main__":
    process_file()