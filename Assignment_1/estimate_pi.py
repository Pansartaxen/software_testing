import argparse
from pathlib import Path
import random


def estimate_pi(n):
    count = 0
    for i in range(n):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    return 4 * count / n


class PiFileWriter:
    def __init__(self):
        self._content = None
        self._file_path = None

    def write(self, content, file_path):
        self._content = content
        self._file_path = file_path

    def content(self):
        return self._content

    def file_path(self):
        return self._file_path


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='PI Maker', description='Computes pi and stores the result to a file')
    parser.add_argument('-i', '--iterations', default=1000000)
    parser.add_argument('-o', '--out_file', type=Path, default=None)
    args = parser.parse_args()

    if args.out_file:
        args.out_file.parent.mkdir(parents=True, exist_ok=True)

    pi = estimate_pi(args.iterations)

    if args.out_file:
        PiFileWriter.write(str(pi), args.out_file)
    else:
        print(pi)
