import argparse
import pytest
import collections


def compute(data):

    lines = data.splitlines()
    edges = collections.defaultdict(set)
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
            if hop.isupper() or hop not in hops:
                remaining.append((*hops, hop))

    return len(seen)


INPUT = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 226)])
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
