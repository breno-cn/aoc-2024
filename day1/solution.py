import os
import sys

from typing import List, Tuple
from collections import defaultdict

def read_input() -> Tuple[List[int], List[int]]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    left = []
    right = []
    with open(filepath, 'r') as file:
        data = file.read().strip().split('\n')

        for row in data:
            splitted = row.split()
            left.append(int(splitted[0]))
            right.append(int(splitted[1]))

    return left, right

input = read_input()

def part1() -> int:
    left, right = input
    left.sort()
    right.sort()

    result = 0
    for i in range(len(left)):
        result += abs(left[i] - right[i])
    
    return result

def part2() -> int:
    left, right = input
    frequency = defaultdict(int)

    for number in right:
        frequency[number] += 1

    result = 0
    for number in left:
        result += number * frequency[number]

    return result

part1_result = part1()
print(part1_result)

part2_result = part2()
print(part2_result)