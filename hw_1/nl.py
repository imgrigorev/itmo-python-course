import sys


def read_from_file(filename):
    with open(filename, 'r') as f:
        for index, line in enumerate(f, start=1):
            print(f"{index}\t{line}", end='')


def read_from_stdin():
    index = 1
    try:
        while True:
            line = input()
            print(f"{index}\t{line}")
            index += 1
    except EOFError:
        pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        read_from_file(sys.argv[1])
    else:
        read_from_stdin()
