import argparse
import pytest


def compute(data):
    num_input, *boards_s = data.split("\n\n")

    boards = []
    board_ints = []
    for board in boards_s:
        boards_d = {}
        for line in board.split():
            boards_d[int(line)] = False
        boards.append(boards_d)

    for board in boards_s:
        board_int = []
        for num_s in board.split():
            board_int.append(int(num_s))
        board_ints.append(board_int)

    nums = [int(num) for num in num_input.split(",")]
    for num in nums:
        for board in boards:
            if num in board:
                board[num] = True

        for cur_board, board in enumerate(boards):
            for row in range(5):
                for col in range(5):
                    if not board[board_ints[cur_board][row * 5 + col]]:
                        break
                else:  # Bingo!
                    return (
                        sum([num for num, hit in board.items() if not hit])
                        * num  # noqa
                    )


INPUT = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


@pytest.mark.parametrize(("test_input,expected"), [(INPUT, 4512)])
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
