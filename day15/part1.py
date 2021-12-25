import argparse
import pytest
import sys
from collections import defaultdict


def get_adjacent(loc, coords, checked):

    adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    x, y = loc
    locations = set()
    for x_adj, y_adj in adj:
        adj_loc = (x + x_adj, y + y_adj)
        if adj_loc in coords:
            if adj_loc not in checked:
                locations.add(adj_loc)

    return locations


def get_lowest_distance(distances, checked):

    coord = None
    min_distance = sys.maxsize
    for k, v in distances.items():
        if k in checked:
            continue
        if v < min_distance:
            coord = k
            min_distance = v

    return coord


def compute(data):
    current_node = (0, 0)
    coords = defaultdict(lambda: sys.maxsize)
    distances = defaultdict(lambda: sys.maxsize)
    lines = data.splitlines()
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            coords[(i, j)] = int(num)
            if (i, j) == current_node:
                distances[(i, j)] = 0
            else:
                distances[(i, j)] = sys.maxsize

    s_paths = {(0, 0): 0}
    checked = set()
    current_node = (0, 0)
    while (i, j) not in checked:
        checked.add(current_node)
        unvisited = get_adjacent(current_node, coords, checked)

        for node in unvisited:
            if node in checked:
                continue
            if node not in s_paths:
                s_paths[node] = s_paths[current_node] + coords[node]
                if distances[node] > s_paths[node]:
                    distances[node] = s_paths[node]
            elif s_paths[node] > s_paths[current_node] + coords[node]:
                s_paths[node] = s_paths[current_node] + coords[node]
                if distances[node] > s_paths[node]:
                    distances[node] = s_paths[node]

        current_node = get_lowest_distance(distances, checked)

        s_paths = {current_node: distances[current_node]}

    return distances[(i, j)]


INPUT = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 40)])
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
