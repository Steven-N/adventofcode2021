import argparse
import pytest
import collections


def compute(data):

    score = {")": 3, "]": 57, "}": 1197, ">": 25137}

    opposite = {")": "(", "]": "[", "}": "{", ">": "<"}

    illegal = []
    lines = data.splitlines()
    for line in lines:
        paren_counter = collections.defaultdict(int)
        paren_position = collections.defaultdict(list)
        recent = []
        for idx, paren in enumerate(line):
            if paren in score:
                if opposite[paren] != recent[-1]:
                    illegal.append(score[paren])
                    break
                else:
                    recent.pop()
            else:
                recent.append(paren)
                paren_position[paren].append(idx)
                paren_counter[paren] += 1

    return sum(illegal)


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


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 26397)])
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
