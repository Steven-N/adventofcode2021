import argparse
import pytest


def compute(data):

    states = [int(s) for s in data.split(",")]

    day = 0
    while day < 80:
        for idx, state in enumerate(states.copy()):
            if state == 0:
                states.append(8)
                states[idx] = 6
            else:
                states[idx] -= 1
        day += 1

    return len(states)


INPUT = """\
3,4,3,1,2
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 5934)])
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
