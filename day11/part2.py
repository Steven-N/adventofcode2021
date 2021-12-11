import argparse
import pytest
import collections
import sys


def compute(data):

    coords = collections.defaultdict(lambda: sys.maxsize)
    flashes = 0
    steps = 1
    coord_list = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    lines = data.splitlines()
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            coords[(i, j)] = int(num)

    while True:
        coords_to_update = []
        for (x, y), num in tuple(coords.items()):
            coords[x, y] += 1
            if coords[x, y] > 9:
                coords_to_update.append((x, y))

        while len(coords_to_update) > 0:
            flash_coord = coords_to_update.pop()
            x_f, y_f = flash_coord
            if coords[flash_coord] == 0:
                continue
            flashes += 1
            coords[flash_coord] = 0
            for coord_x, coord_y in coord_list:
                if (x_f + coord_x, y_f + coord_y) in coords and coords[
                    (x_f + coord_x, y_f + coord_y)
                ] != 0:
                    coords[x_f + coord_x, y_f + coord_y] += 1
                    if coords[x_f + coord_x, y_f + coord_y] > 9:
                        coords_to_update.append((x_f + coord_x, y_f + coord_y))

        if sum(coords.values()) == 0:
            return steps

        steps += 1


INPUT = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 195)])
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
