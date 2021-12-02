import argparse
import pytest


def compute(data):

    horizontal = 0
    depth = 0

    for line in data.splitlines():
        action, units = line.split()

        if action == "up":
            depth -= int(units)
        elif action == "down":
            depth += int(units)
        elif action == "forward":
            horizontal += int(units)
        else:
            raise NotImplementedError(f"Unrecognized action {action}")

    return horizontal * depth


INPUT = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 150)])
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
