import argparse
import pytest


def calculate_occurences(current_dict):
    nums = [key for key, value in current_dict.items() if value]
    counts = [0] * len(nums[0])
    for num in nums:
        for i, c in enumerate(num):
            if c == "1":
                counts[i] += 1
    return counts, len(nums)


def compute(data):

    lines = data.splitlines()

    # Oxygen generator rating
    oxygen_generator = {num_s: True for num_s in lines}
    for i in range(len(lines[0])):
        counts, nums_remaining = calculate_occurences(oxygen_generator)
        if counts[i] >= (nums_remaining - counts[i]):
            for num, exists in oxygen_generator.items():
                if exists:
                    if num[i] != "1":
                        oxygen_generator[num] = False
        elif counts[i] < (nums_remaining - counts[i]):
            for num, exists in oxygen_generator.items():
                if exists:
                    if num[i] != "0":
                        oxygen_generator[num] = False

        oxygen_generator_result = [
            key for key, value in oxygen_generator.items() if value
        ]
        if len(oxygen_generator_result) == 1:
            break

    # C02 Scrubber
    c02_scrubber = {num_s: True for num_s in lines}
    for i in range(len(lines[0])):
        counts, nums_remaining = calculate_occurences(c02_scrubber)
        if counts[i] >= (nums_remaining - counts[i]):
            for num, exists in c02_scrubber.items():
                if exists:
                    if num[i] != "0":
                        c02_scrubber[num] = False
        elif counts[i] < (nums_remaining - counts[i]):
            for num, exists in c02_scrubber.items():
                if exists:
                    if num[i] != "1":
                        c02_scrubber[num] = False

        c02_scrubber_result = [k for k, val in c02_scrubber.items() if val]
        if len(c02_scrubber_result) == 1:
            break

    return int(oxygen_generator_result[0], 2) * int(c02_scrubber_result[0], 2)


INPUT = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 230)])
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
