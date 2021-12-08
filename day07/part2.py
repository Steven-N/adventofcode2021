import argparse
import pytest
from collections import Counter


def compute_fuel_for_move(fuel_1, fuel_2):
    min_fuel, max_fuel = min(fuel_1, fuel_2), max(fuel_1, fuel_2)
    fuel_calc = 0
    step = 0
    for _ in range(min_fuel, max_fuel + 1):
        fuel_calc += step
        step += 1

    return fuel_calc


def compute(data):

    positions = [int(fuel) for fuel in data.split(",")]
    sorted_positions = sorted(positions)
    min_pos, max_pos = sorted_positions[0], sorted_positions[-1]
    min_fuel = None
    fuel_tracker = Counter()

    for pos_i in range(min_pos, max_pos):
        for pos_j in positions:
            fuel_for_move = compute_fuel_for_move(pos_i, pos_j)
            fuel_tracker[pos_i] += fuel_for_move

    for _, fuel in fuel_tracker.items():
        if min_fuel is None:
            min_fuel = fuel
        else:
            min_fuel = min(min_fuel, fuel)

    return min_fuel


INPUT = """\
16,1,2,0,4,2,7,1,2,14
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 168)])
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
