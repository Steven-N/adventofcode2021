import argparse
import pytest


def parse(binary, i):

    type_id = int(binary[i + 3 : i + 6], 2)  # noqa: E203
    len_id = int(binary[i + 6], 2)

    if type_id == 4:  # Literal value packet
        i += 6
        literal_value_result = ""
        while True:
            literal_value_result += binary[i + 1 : i + 5]  # noqa: E203
            if binary[i] == "0":
                return int(literal_value_result, 2), i + 5
            i += 5

    else:
        packet_vals = []
        if len_id == 0:
            sub_pckt_length = int(binary[i + 7 : i + 22], 2)  # noqa: E203
            start = i + 22
            i = start
            while True:
                val, i = parse(binary, i)
                packet_vals.append(val)
                if i - start == sub_pckt_length:
                    break
        else:
            sub_packets = int(binary[i + 7 : i + 18], 2)  # noqa: E203
            i += 18
            for _ in range(sub_packets):
                val, i = parse(binary, i)
                packet_vals.append(val)

    if type_id == 0:
        return sum(packet_vals), i
    elif type_id == 1:
        result = 1
        for num in packet_vals:
            result *= num
        return result, i
    elif type_id == 2:
        return min(packet_vals), i
    elif type_id == 3:
        return max(packet_vals), i
    elif type_id == 5:
        if packet_vals[0] > packet_vals[1]:
            return 1, i
        else:
            return 0, i
    elif type_id == 6:
        if packet_vals[0] < packet_vals[1]:
            return 1, i
        else:
            return 0, i
    elif type_id == 7:
        if packet_vals[0] == packet_vals[1]:
            return 1, i
        else:
            return 0, i


def compute(data, i=0):

    binary = bin(int(data, 16))[2:]
    binary = binary.zfill(len(binary) + len(binary) % 4)

    result, _ = parse(binary, 0)
    return result


INPUT = """\
C200B40A82
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 3)])
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
