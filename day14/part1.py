import argparse
import pytest
from collections import Counter


def compute(data):

    template, rules_s = data.split("\n\n")

    rules = {}
    for rule in rules_s.splitlines():
        rule_l, rule_r = rule.split(" -> ")
        rules[rule_l] = rule_r

    for _ in range(10):
        result = []
        for idx in range(len(template) - 1):
            letters = template[idx : idx + 2]  # noqa: E203
            if letters in rules:
                if idx == 0:
                    new_insert = letters[:1] + rules[letters] + letters[1:]
                else:
                    new_insert = rules[letters] + letters[1:]
                result.append(new_insert)
            else:
                result.append(letters)

        template = "".join(result)

    freqs = Counter("".join(result)).most_common()
    return freqs[0][1] - freqs[-1][1]


INPUT = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 1588)])
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
