import argparse
import pytest
from collections import Counter, defaultdict


def can_visit(hops):

    path_counts = Counter(hops)
    for k, c in path_counts.items():
        if k.islower() and c == 2:
            return False

    return True


def compute(data):

    lines = data.splitlines()
    edges = defaultdict(set)
    for line in lines:
        src, dst = line.split("-")
        edges[src].add(dst)
        edges[dst].add(src)

    remaining = [("start",)]
    seen = set()
    while remaining:
        hops = remaining.pop()

        if hops[-1] == "end":
            seen.add(hops)
            continue

        for hop in edges[hops[-1]]:
            if hop == "start":
                continue
            elif hop.isupper() or can_visit(hops) or hop not in hops:
                remaining.append((*hops, hop))

    return len(seen)


INPUT = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 103)])
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
