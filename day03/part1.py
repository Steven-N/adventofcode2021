import argparse
import pytest


def compute(data):

    lines = data.splitlines()
    counts = [0] * len(lines[0])

    for line in lines:
        for i, c in enumerate(line):
            if c == "1":
                counts[i] += 1

    gamma = ""
    eps = ""

    for i in range(len(lines[0])):
        if counts[i] > len(lines) // 2:
            gamma += "1"
            eps += "0"
        else:
            gamma += "0"
            eps += "1"

    return int(gamma, 2) * int(eps, 2)


INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 198)])
def test(test_input, expected):
    assert compute(test_input) == expected


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()

    with open(args.file, "r") as f:
        print(compute(f.read()))


if __name__ == "__main__":
    exit(main())
