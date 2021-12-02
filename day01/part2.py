import argparse
import pytest


def compute(data):

    prev = None
    count = 0
    window = 3
    nums = [int(num) for num in data.splitlines()]
    for i in range(len(nums) - window + 1):
        depth = sum(nums[i : i + window])
        if prev is not None and depth > prev:
            count += 1

        prev = depth

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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 5)])
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
