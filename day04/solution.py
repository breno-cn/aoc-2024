import os
import sys
import re

from typing import List, Generator

def read_input() -> List[str]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        return file.read().strip().split('\n')

input = read_input()

def get_horizontal_rows(puzzle: List[str]) -> Generator[str]:
    for row in puzzle:
        yield ''.join(row)

def get_vertical_rows(puzzle: List[str]) -> Generator[str]:
    for i in range(len(puzzle[0])):
        col = []
        for j in range(len(puzzle)):
            col.append(puzzle[j][i])
        yield ''.join(col)
        col = []

def get_diagonal_rows(puzzle: List[str]) -> Generator[str]:
    col_length = len(puzzle[0])
    row_length = len(puzzle)

    first_diag = [[] for _ in range(row_length + col_length - 1)]
    second_diag = [[] for _ in range(len(first_diag))]

    min_second_diag = -row_length + 1

    for x in range(col_length):
        for y in range(row_length):
            first_diag[x+y].append(puzzle[y][x])
            second_diag[x-y-min_second_diag].append(puzzle[y][x])

    for diag in first_diag:
        yield ''.join(diag)

    for diag in second_diag:
        yield ''.join(diag)


def part1(puzzle: List[str]) -> int:
    xmas = r'XMAS'
    result = 0

    for row in get_horizontal_rows(puzzle):
        result += len(re.findall(xmas, row)) + len(re.findall(xmas, row[::-1]))

    for row in get_vertical_rows(puzzle):
        result += len(re.findall(xmas, row)) + len(re.findall(xmas, row[::-1]))

    for row in get_diagonal_rows(puzzle):
        result += len(re.findall(xmas, row)) + len(re.findall(xmas, row[::-1]))

    return result

def is_xmas(board: List[str]) -> bool:
    first_diag = ''.join([board[0][0], board[1][1], board[2][2]])
    second_diag = ''.join([board[2][0], board[1][1], board[0][2]])

    return (first_diag == 'MAS' or first_diag[::-1] == 'MAS') and (second_diag == 'MAS' or second_diag[::-1] == 'MAS')

def get_board(puzzle: List[str], x: int, y: int) -> int:
    rows = []

    for i in range(3):
        col = []
        for j in range(3):
            col.append(puzzle[x + i][y + j])

        rows.append(col)
        col = []

    return rows

def part2(puzzle: List[str]) -> int:
    puzzle_length = len(puzzle)
    result = 0

    for i in range(puzzle_length - 2):
        for j in range(puzzle_length - 2):
            board = get_board(puzzle, j, i)
            if is_xmas(board):
                result += 1

    return result

result_part1 = part1(input)
print(result_part1)

result_part2 = part2(input)
print(result_part2)
