import argparse
import pytest
import collections


def compute(data):

    result_map = collections.Counter()

    for line in data.splitlines():
        entry = line.split(" -> ")
        start, end = entry
        x1_s, y1_s = start.split(",")
        x2_s, y2_s = end.split(",")
        x1, y1 = int(x1_s), int(y1_s)
        x2, y2 = int(x2_s), int(y2_s)
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                result_map[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                result_map[(x, y1)] += 1

    return len([pos for pos, count in result_map.items() if count > 1])


INPUT = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 5)])
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
