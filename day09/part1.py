import argparse
import pytest
import collections
import sys


def compute(data):
    coords = collections.defaultdict(lambda: sys.maxsize)

    lines = data.splitlines()
    low_points = []
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            coords[(i, j)] = int(num)

    for (x, y), num in tuple(coords.items()):
        if (
            coords[x + 1, y] > num
            and coords[x - 1, y] > num
            and coords[x, y + 1] > num
            and coords[x, y - 1] > num
        ):
            low_points.append(num + 1)

    return sum(low_points)


INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 15)])
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
