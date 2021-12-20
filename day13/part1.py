import argparse
import pytest


def compute(data):

    lines = data.split("\n\n")
    coords = lines[0].splitlines()
    folds = lines[1].splitlines()

    dots = []
    for coord in coords:
        x, y = coord.split(",")
        dots.append((int(x), int(y)))

    result = set()
    for fold in folds[:1]:
        axis, loc = fold.split(" ")[-1].split("=")
        for x, y in dots:
            if axis == "y":
                if y < int(loc):
                    result.add((x, y))
                else:
                    new_y = int(loc) - (y - int(loc))
                    result.add((x, new_y))
            else:
                if x < int(loc):
                    result.add((x, y))
                else:
                    new_x = int(loc) - (x - int(loc))
                    result.add((new_x, y))

    return len(result)


INPUT = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 17)])
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
