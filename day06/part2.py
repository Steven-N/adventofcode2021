import argparse
import pytest
import collections


def compute(data):

    track = collections.defaultdict(int)
    states = [int(s) for s in data.split(",")]

    for state in states:
        if state not in track:
            track[state] = 0
        track[state] += 1

    day = 0
    while day < 256:
        current_state = collections.defaultdict(int)
        for days_remaining, state in track.items():
            if days_remaining == 0:
                current_state[6] += state
                current_state[8] += state
            else:
                current_state[days_remaining - 1] += state
        day += 1
        track = current_state

    return sum(track.values())


INPUT = """\
3,4,3,1,2
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 26984457539)])
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
