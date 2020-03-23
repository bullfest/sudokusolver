import itertools

from solver import transpose, solve, sudoku_boxes


class TestTranspose:
    def test_1x1(self):
        assert transpose([[1]]) == [[1]]
        assert transpose([[17]]) == [[17]]

    def test_2x2(self):
        assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

    def test_2x3(self):
        assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


class TestSolve:
    @classmethod
    def check(cls, solved_board):
        all_values = set(range(1, 10))

        # check rows
        for row in solved_board:
            assert set(row) == all_values

        for column in transpose(solved_board):
            assert set(column) == all_values

        for box in itertools.chain(*sudoku_boxes(solved_board)):
            assert set(box) == all_values

    def test_simple(self):
        # http://www.sudokuessentials.com/images/xeasy_sudoku.gif.pagespeed.ic.hKl3WPT7jB.png
        n = None
        board = [
            [n, 6, n, 3, n, n, 8, n, 4],
            [5, 3, 7, n, 9, n, n, n, n],
            [n, 4, n, n, n, 6, 3, n, 7],
            [n, 9, n, n, 5, 1, 2, 3, 8],
            [n, n, n, n, n, n, n, n, n],
            [7, 1, 3, 6, 2, n, n, 4, n],
            [3, n, 6, 4, n, n, n, 1, n],
            [n, n, n, n, 6, n, 5, 2, 3],
            [1, n, 2, n, n, 9, n, 8, n],
        ]
        solution = solve(board)

        self.check(solution)
