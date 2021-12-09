import argparse
import pytest


def compute(data):

    parsed_data = {}
    len_check = set([2, 3, 4, 7])
    count = 0
    for data_i in data.splitlines():
        data_split = data_i.split(" | ")
        input_i = data_split[0]
        output_i = data_split[1]
        parsed_data[input_i] = output_i

    # Find pattern

    for input_i, output_i in parsed_data.items():
        pattern_known = {}
        for in_val_known in input_i.split(" "):
            if len(in_val_known) in len_check:
                one = len(in_val_known) == 2
                four = len(in_val_known) == 4
                seven = len(in_val_known) == 3
                eight = len(in_val_known) == 7

                if one:
                    pattern_known[1] = in_val_known
                if four:
                    pattern_known[4] = in_val_known
                if seven:
                    pattern_known[7] = in_val_known
                if eight:
                    pattern_known[8] = in_val_known

        for unknown in input_i.split(" "):
            if len(unknown) not in len_check:

                if len(unknown) == 5:
                    if 1 in pattern_known:
                        if (set(pattern_known[1]) & set(unknown)) == set(
                            pattern_known[1]
                        ):
                            pattern_known[3] = unknown
                            continue
                    if 4 in pattern_known:
                        if len((set(pattern_known[4]) & set(unknown))) == 3:
                            if 1 in pattern_known:
                                pattern_known[5] = unknown
                                continue
                        else:
                            pattern_known[2] = unknown
                            continue

                if len(unknown) == 6:
                    if 4 in pattern_known:
                        if (set(pattern_known[4]) & set(unknown)) == set(
                            pattern_known[4]
                        ):
                            pattern_known[9] = unknown
                            continue

                    if 1 in pattern_known:
                        if len((set(pattern_known[1]) & set(unknown))) == 2:
                            if 4 in pattern_known:
                                pattern_known[0] = unknown
                                continue
                        else:
                            pattern_known[6] = unknown
                            continue

        cur_count = ""
        for output_code in output_i.split(" "):
            for num, code in pattern_known.items():
                code_set = set(code)
                output_code_set = set(output_code)
                if code_set == output_code_set:
                    cur_count += str(num)

        count += int(cur_count)

    return count

    # return count


INPUT = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""  # noqa: E501


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 61229)])
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
