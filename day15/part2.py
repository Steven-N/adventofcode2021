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
    line_len = len(lines[0])
    for i, line in enumerate(lines):
        for j, num in enumerate(line):
            coords[(i, j)] = int(num)

    temp_coords = defaultdict(lambda: sys.maxsize)
    for tile_i in range(5):
        for tile_j in range(5):
            for coord, val in coords.items():
                x, y = coord
                new_x = x + (line_len * tile_i)
                new_y = y + (line_len * tile_j)

                if (new_x, new_y) in coords:
                    temp_coords[(new_x, new_y)] = val
                    continue

                if (new_x - line_len, new_y) in temp_coords:
                    new_num = temp_coords[(new_x - line_len, new_y)] + 1
                elif (new_x, new_y - line_len) in temp_coords:
                    new_num = temp_coords[(new_x, new_y - line_len)] + 1

                if new_num > 9:
                    new_num = 1

                temp_coords[(new_x, new_y)] = new_num
                final_x = new_x
                final_y = new_y

    coords = temp_coords
    s_paths = {(0, 0): 0}
    checked = set()
    current_node = (0, 0)

    for coord, _ in coords.items():
        i, j = coord
        if (i, j) == current_node:
            distances[(i, j)] = 0
        else:
            distances[(i, j)] = sys.maxsize

    while (final_x, final_y) not in checked:
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
        if len(checked) % 1000 == 0:
            print(f"Current Node: {current_node}")
            print(f"Nodes checked: {len(checked)}")

    return distances[(final_x, final_y)]


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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 315)])
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
