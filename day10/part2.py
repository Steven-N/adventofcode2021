import argparse
import pytest
import collections


def compute(data):

    scores = {")": 1, "]": 2, "}": 3, ">": 4}

    opposite = {")": "(", "]": "[", "}": "{", ">": "<"}

    forward = {"(": ")", "[": "]", "{": "}", "<": ">"}

    illegal = []
    result = []
    lines = data.splitlines()
    for line in lines:
        paren_counter = collections.defaultdict(int)
        paren_position = collections.defaultdict(list)
        illegal = False
        recent = []
        for idx, paren in enumerate(line):
            if paren in scores:
                if opposite[paren] != recent[-1]:
                    illegal = True
                    break
                else:
                    recent.pop()
            else:
                recent.append(paren)
                paren_position[paren].append(idx)
                paren_counter[paren] += 1

        if not illegal and len(recent) > 0:
            remaining = "".join(recent[::-1])
            score = 0
            for remain in remaining:
                score *= 5
                score += scores[forward[remain]]
            result.append(score)

    result = sorted(result)
    return result[len(result) // 2]


INPUT = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 288957)])
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
