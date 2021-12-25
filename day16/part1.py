import argparse
import pytest


def compute(data):

    version_sum = 0
    binary = bin(int(data, 16))[2:]

    while binary:
        if int(binary, 2) == 0:
            break
        version = binary[:3]
        type_id = binary[3:6]

        version_sum += int(version, 2)
        if int(type_id, 2) == 4:  # Literal value packet
            idx = 6
            while True:
                if binary[idx] == "0":
                    break
                idx += 5
            binary = binary[idx + 5 :]  # noqa: E203
        else:  # Operator packet
            if binary[6] == "0":
                binary = binary[22:]
            else:
                binary = binary[18:]

    # breakpoint()
    return version_sum


INPUT = """\
A0016C880162017C3686B18A3D4780
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 31)])
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
