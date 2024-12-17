import os
import sys

from typing import List, Tuple
import itertools

def read_input():
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        data = file.read().strip().split('\n')

        input = []
        for line in data:
            splitted = line.split(': ')
            result = int(splitted[0])
            equation = list(map(int, splitted[1].split(' ')))

            input.append((result, equation))

        return input
    
input = read_input()

def solve_equation(equation: List[int], operators: List[str]) -> int:
    result = equation[0]

    for i in range(len(equation) - 1):
        operator = operators[i]
        match operator:
            case '+':
                result += equation[i + 1]
            case '*':
                result *= equation[i + 1]

    return result

def part1(input: List[Tuple[int, List[int]]]):
    operators = ['*', '+']
    result = 0

    for equation in input:
        possible_operators = itertools.product(operators, repeat=len(equation[1])-1)
        for operator in possible_operators:
            if equation[0] == solve_equation(equation[1], operator):
                result += equation[0]
                break

    return result

def solve_equation_part2(equation: List[int], operators: List[str]) -> int:
    result = equation[0]

    for i in range(len(equation) - 1):
        operator = operators[i]
        match operator:
            case '+':
                result += equation[i + 1]
            case '*':
                result *= equation[i + 1]
            case '||':
                result = int(str(result) + str(equation[i + 1]))

    return result

def part2(input: List[Tuple[int, List[int]]]):
    operators = ['*', '+', '||']
    result = 0

    for equation in input:
        possible_operators = itertools.product(operators, repeat=len(equation[1])-1)
        for operator in possible_operators:
            if equation[0] == solve_equation_part2(equation[1], operator):
                result += equation[0]
                break

    return result
            
result_part1 = part1(input)
print(result_part1)

result_part2 = part2(input)
print(result_part2)