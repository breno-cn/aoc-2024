import os
import sys

import itertools

from typing import List, Dict, Generator, Tuple
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Antenna:
    i: int
    j: int
    frequency: str

def read_input() -> List[List[str]]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        data = file.read().strip().split('\n')
        return list(map(list, data))

def generate_antennas(board: List[List[str]]) -> Dict[str, Antenna]:
    antennas = defaultdict(list)

    for i in range(len(board)):
        for j in range(len(board[i])):
            tile = board[i][j]
            if tile == '.':
                continue

            antennas[tile].append(Antenna(i, j, tile))

    return antennas

def is_coord_valid(i: int, j: int, board: List[List[str]]) -> bool:
    return not (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]))

def get_four_corners(a: Antenna, horizontal_dist: int, vertical_dist: int, board: List[List[str]]) -> Generator[Tuple[int, int]]:
    corners = [
        (a.i - vertical_dist, a.j - horizontal_dist),
        (a.i + vertical_dist, a.j - horizontal_dist),
        (a.i - vertical_dist, a.j + horizontal_dist),
        (a.i + vertical_dist, a.j + horizontal_dist)
    ]
    
    for i, j in corners:
        if is_coord_valid(i, j, board):
            yield (i, j)

def mark_antinodes(a: Antenna, horizontal_dist: int, vertical_dist: int, board: List[List[str]]):
    i = a.i + vertical_dist
    j = a.j + horizontal_dist
    while is_coord_valid(i, j, board):
        if board[i][j] == '.':
            board[i][j] = '#'
            
        i += vertical_dist
        j += horizontal_dist
            
def distance(a: Tuple[int, int], b: Tuple[int, int]) -> Tuple[int, int]:
    return (abs(a[0] - b[0]), abs(a[1] - b[1]))
            
def generate_antinodes(a: Antenna, b: Antenna, board: List[List[str]]):
    horizontal_distance = abs(a.j - b.j)
    vertical_distance = abs(a.i - b.i)

    for i, j in get_four_corners(a, horizontal_distance, vertical_distance, board):
        dist_to_b = distance((i, j), (b.i, b.j))
        dist_to_a = distance((i, j), (a.i, a.j))
        
        if dist_to_b[0] == 2*dist_to_a[0] and dist_to_b[1] == 2*dist_to_a[1]:
            board[i][j] = '#'

    for i, j in get_four_corners(b, horizontal_distance, vertical_distance, board):
        dist_to_a = distance((i, j), (a.i, a.j))
        dist_to_b = distance((i, j), (b.i, b.j))
        
        if dist_to_a[0] == 2*dist_to_b[0] and dist_to_a[1] == 2*dist_to_b[1]:
            board[i][j] = '#'

def generate_antinodes_part2(a: Antenna, b: Antenna, board: List[List[str]]):
    horizontal_distance = (a.j - b.j)
    vertical_distance = (a.i - b.i)
    mark_antinodes(a, horizontal_distance, vertical_distance, board)

    horizontal_distance = (b.j - a.j)
    vertical_distance = (b.i - a.i)
    mark_antinodes(b, horizontal_distance, vertical_distance, board)

def part1(board: List[List[str]]) -> int:
    antennas = generate_antennas(board)

    for frequency in antennas:
        pairs = itertools.combinations(antennas[frequency], 2)
        for pair in pairs:
            generate_antinodes(pair[0], pair[1], board)

    result = 0
    for row in board:
        for tile in row:
            if tile == '#':
                result += 1

    return result

def part2(board: List[List[str]]) -> int:
    antennas = generate_antennas(board)

    for frequency in antennas:
        pairs = itertools.combinations(antennas[frequency], 2)
        for a, b in pairs:
            generate_antinodes_part2(a, b, board)

    result = 0
    for row in board:
        for tile in row:
            if tile != '.':
                result += 1

    return result


result_part1 = part1(read_input())
print(result_part1)

result_part2 = part2(read_input())
print(result_part2)
