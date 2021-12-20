import argparse
import pytest


def find_word(coords):

    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0

    result = ""
    for x, y in coords:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in coords:
                result += "#"
            else:
                result += " "
        result += "\n"

    return result


def compute(data):

    lines = data.split("\n\n")
    coords = lines[0].splitlines()
    folds = lines[1].splitlines()

    dots = []
    for coord in coords:
        x, y = coord.split(",")
        dots.append((int(x), int(y)))

    for fold in folds:
        result = set()
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

        dots = list(result)

    print(find_word(result))
    return find_word(result)


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


EXPECTED = """\
#####
#   #
#   #
#   #
#####
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, EXPECTED)])
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
