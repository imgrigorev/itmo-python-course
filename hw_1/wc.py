import sys


def count_lines_words_bytes(filename, file):
    lines = words = bytes_count = 0
    for line in file:
        lines += 1
        words += len(line.split())
        bytes_count += len(line.encode())
    return lines, words, bytes_count


def print_stats(lines, words, bytes_count, name=""):
    print(f"{lines:8}{words:8}{bytes_count:8}", name)


def main():
    files = sys.argv[1:]

    total_lines = total_words = total_bytes = 0
    if files:
        for filename in files:
            try:
                with open(filename, "rb") as file:
                    decoded_file = (line.decode(errors="ignore") for line in file)
                    lines, words, bytes_count = count_lines_words_bytes(filename, decoded_file)
                    print_stats(lines, words, bytes_count, filename)
                    total_lines += lines
                    total_words += words
                    total_bytes += bytes_count
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}", file=sys.stderr)

        if len(files) > 1:
            print_stats(total_lines, total_words, total_bytes, "total")

    else:
        lines, words, bytes_count = count_lines_words_bytes("<stdin>", sys.stdin)
        print_stats(lines, words, bytes_count)


if __name__ == "__main__":
    main()
