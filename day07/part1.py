import argparse
import pytest
from collections import Counter


def compute(data):

    fuels = [int(fuel) for fuel in data.split(",")]
    min_fuel = None
    fuel_tracker = Counter()
    for fuel_i in fuels:
        if fuel_i in fuel_tracker:
            continue
        for fuel_j in fuels:
            fuel_tracker[fuel_i] += abs(fuel_i - fuel_j)

    for _, fuel in fuel_tracker.items():
        if min_fuel is None:
            min_fuel = fuel
        else:
            min_fuel = min(min_fuel, fuel)

    return min_fuel


INPUT = """\
16,1,2,0,4,2,7,1,2,14
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 37)])
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
