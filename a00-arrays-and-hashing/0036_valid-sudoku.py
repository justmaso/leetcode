def initial_isValidSudoku(board: list[list[str]]) -> bool:
    board_size = len(board)
    thirds = board_size // 3
    rows = [set() for _ in range(board_size)]
    cols = [set() for _ in range(board_size)]

    # list-based subboxes
    subboxes = [set() for _ in range(board_size)]
    
    def get_subbox_idx(row_idx: int, col_idx: int) -> int:
        row_component = thirds * (row_idx // thirds)
        col_component = col_idx // thirds
        return row_component + col_component

    for r_idx in range(board_size):
        for c_idx in range(board_size):
            value = board[r_idx][c_idx]

            # skip unknown cells
            if value == ".": continue

            subbox_idx = get_subbox_idx(r_idx, c_idx)

            # perform checks
            row_valid = value not in rows[r_idx]
            col_valid = value not in cols[c_idx]
            subbox_valid = value not in subboxes[subbox_idx]

            # at least one check isn't valid
            if not (row_valid and col_valid and subbox_valid):
                return False
            # all checks are valid
            else:
                rows[r_idx].add(value)
                cols[c_idx].add(value)
                subboxes[subbox_idx].add(value)

    # all checks have been made and validated
    return True

def cleaner_isValidSudoku(board: list[list[str]]) -> bool:
    from collections import defaultdict

    n = len(board)
    subbox_size = n // 3
    rows = defaultdict(set)
    cols = defaultdict(set)

    # grid-based dict of subboxes
    subboxes = defaultdict(set)

    def get_subbox_idx(row_idx: int, col_idx: int) -> tuple[int, int]:
        return (r_idx // subbox_size, c_idx // subbox_size)

    for r_idx in range(n):
        for c_idx in range(n):
            digit = board[r_idx][c_idx]

            # skip unknown cells
            if digit == ".": continue

            subbox_idx = get_subbox_idx(r_idx, c_idx)

            # at least one check isn't valid
            if (digit in rows or
                digit in cols or
                digit in subboxes[subbox_idx]
            ):
                return False
            
            # all checks valid, add this value for future checks
            rows[r_idx].add(digit)
            cols[c_idx].add(digit)
            subboxes[subbox_idx].add(digit)

    return True


from dataclasses import dataclass

@dataclass
class TestCase:
    board: list[list[str]]
    expected: bool


def run_tests():
    test_cases = [
        TestCase(
            board=[
                ["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ],
            expected=True
        ),
        TestCase(
            board=[
                ["8","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]
            ],
            expected=False
        )
    ]

    solutions = [
        initial_isValidSudoku,
        cleaner_isValidSudoku
    ]

    for idx, case in enumerate(test_cases):
        print(f"case {idx}: ({case.board}) -> {case.expected}")
        for solution in solutions:
            result = solution(case.board)
            passed = result == case.expected
            status = "+" if passed else f"- (got {result})"
            print(f"\t{status}{solution.__name__}")


if __name__ == "__main__":
    run_tests()

