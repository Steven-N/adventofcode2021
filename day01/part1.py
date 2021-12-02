import argparse
import pytest


def compute(data):

    prev = None
    count = 0
    for line in data.splitlines():
        if prev is not None and int(line) > prev:
            count += 1

        prev = int(line)

    return count


INPUT = """\
199
200
208
210
200
207
240
269
260
263
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 7)])
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
