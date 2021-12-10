import argparse
import pytest
import collections
import sys


def compute(data):
    coords = collections.defaultdict(lambda: sys.maxsize)

    lines = data.splitlines()
    low_points = []
    basins = []
    basin_sizes = []
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
            low_points.append((x, y))

    for x, y in low_points:
        basin_l = [(x, y)]
        seen = set()
        seen.add((x, y))

        while True:
            updated = False
            start = 0
            temp_list = []
            for x, y in basin_l[start:]:
                if coords[x + 1, y] < 9:
                    if (x + 1, y) not in seen:
                        temp_list.append((x + 1, y))
                        seen.add((x + 1, y))
                        updated = True
                if coords[x - 1, y] < 9:
                    if (x - 1, y) not in seen:
                        temp_list.append((x - 1, y))
                        seen.add((x - 1, y))
                        updated = True
                if coords[x, y + 1] < 9:
                    if (x, y + 1) not in seen:
                        temp_list.append((x, y + 1))
                        seen.add((x, y + 1))
                        updated = True
                if coords[x, y - 1] < 9:
                    if (x, y - 1) not in seen:
                        temp_list.append((x, y - 1))
                        seen.add((x, y - 1))
                        updated = True

            basin_l.extend(temp_list)
            start += 1
            if not updated:
                basins.append(basin_l)
                if len(basin_sizes) < 3:
                    basin_sizes.append(len(basin_l))
                elif len(basin_l) > basin_sizes[0]:
                    basin_sizes[0] = len(basin_l)

                basin_sizes = sorted(basin_sizes)
                break

    result = 1
    for basin_size in basin_sizes:
        result *= basin_size
    return result


INPUT = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 1134)])
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
