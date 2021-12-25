import argparse
import pytest
from collections import Counter


def compute(data):

    template, rules_s = data.split("\n\n")

    rules = {}
    for rule in rules_s.splitlines():
        rule_l, rule_r = rule.split(" -> ")
        rules[rule_l] = rule_r

    counts = Counter()
    for idx in range(len(template) - 1):
        letters = template[idx : idx + 2]  # noqa: E203
        counts[letters] += 1

    for _ in range(40):
        tmp_counts = Counter()
        final_counts = Counter()
        for k, v in counts.items():
            tmp_counts[f"{k[0]}{rules[k]}"] += v
            tmp_counts[f"{rules[k]}{k[1]}"] += v
            final_counts[k[0]] += v
            final_counts[rules[k]] += v

        counts = tmp_counts

    final_counts[template[-1]] += 1

    max_val = 0
    min_val = None
    for _, v in final_counts.items():
        if min_val is None:
            min_val = v
        min_val = min(min_val, v)
        max_val = max(max_val, v)

    return max_val - min_val


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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 2188189693529)])
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
