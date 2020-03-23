import itertools
from typing import List, Optional, Any, Iterator


def constrain(area: List[List[int]]) -> int:
    """ Constrain options in area so that values are unique in the area
    :returns The number of positions constrained to a single value
    """
    n_solved = 0
    for i, list1 in enumerate(area):
        if len(list1) == 1:
            # only one option left at index i, all other options can therefor be constrained
            for j, list2 in enumerate(area):
                if i == j:
                    continue
                if list1[0] in list2:
                    list2.remove(list1[0])
                    if len(list2) is 1:
                        n_solved += 1
        # It's possible to do better constraining, but let's wait with that for now

    return n_solved


def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    """ Transpose a matrix
    turns the matrix
    [[1, 2]
     [3, 4]]
    into
    [[1, 3]
     [2, 4]]
    """
    return [list(l) for l in zip(*matrix)]


def sudoku_boxes(board: List[List[Any]]) -> List[List[Any]]:
    """ Returns a matrix of the inner boxes in a sudoku-board """
    box_board = [
        [
            [board[box_i * 3 + i][box_j * 3 + j] for j in range(3) for i in range(3)]
            for box_j in range(3)
        ]
        for box_i in range(3)
    ]

    return box_board


def flatten(iter: Iterator[Iterator[Any]]) -> Iterator[Any]:
    # itertools.chain(*l) "flattens" a list l, i.e. [[1, 2, 3], [6, 8], [4, 5]]
    # becomes [1, 2, 3, 6 ,8, 4, 5]
    return itertools.chain(*iter)


def solve(board: List[List[Optional[int]]]) -> List[List[int]]:
    """ Solve a 9x9 sudoku board
    
    @param board A 9x9 matrix with either an integer or `None`
    """

    n_unsolved = sum(1 if v is None else 0 for v in flatten(board))

    options: List[List[List[int]]] = [
        [
            list(range(1, 10)) if board[i][j] is None else [board[i][j]]
            # [1...9] if value isn't determined, otherwise list with just the value
            for j in range(9)
        ]
        for i in range(9)
    ]

    while n_unsolved > 0:
        n_unsolved_prev_iteration = -1  # So that we enter the loop
        while n_unsolved_prev_iteration != n_unsolved:
            n_unsolved_prev_iteration = n_unsolved

            for row in options:
                n_unsolved -= constrain(row)

            for column in transpose(options):
                n_unsolved -= constrain(column)

            for box in flatten(sudoku_boxes(options)):
                n_unsolved -= constrain(box)

    solved_board = [[options[i][j][0] for j in range(9)] for i in range(9)]

    return solved_board
