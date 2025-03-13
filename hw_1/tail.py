import sys
from collections import deque


def tail_file(filename, num_lines=10):
    try:
        with open(filename, 'r') as f:
            last_lines = deque(f, maxlen=num_lines)
            for line in last_lines:
                print(line, end='')
    except FileNotFoundError:
        print(f"tail: cannot open '{filename}' for reading: No such file or directory", file=sys.stderr)


def tail_stdin(num_lines=17):
    lines = deque(sys.stdin, maxlen=num_lines)
    for line in lines:
        print(line, end='')


def main():
    files = sys.argv[1:]

    if not files:
        tail_stdin()
    else:
        for i, filename in enumerate(files):
            if len(files) > 1:
                if i > 0:
                    print()
                print(f"==> {filename} <==")
            tail_file(filename)


if __name__ == "__main__":
    main()
