import os
import sys
import re

from typing import Tuple

def read_input() -> str:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        return file.read().strip()

input = read_input()

def part1(input: str) -> int:
    mul_regex = r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)'
    instructions = re.findall(mul_regex, input)

    result = 0
    number_regex = r'\b\d{1,3}\b'
    for match in instructions:
        numbers = re.findall(number_regex, match)
        result += int(numbers[0]) * int(numbers[1])

    return result

def clear_instruction(instruction: Tuple[str, str, str]) -> str:
    return next(field for field in instruction if field)

def part2(input: str) -> int:
    instructions_regex = r"(mul\(\b\d{1,3}\b,\b\d{1,3}\b\))|(do\(\))|(don't\(\))"
    instructions = re.findall(instructions_regex, input)

    should_do = True
    result = 0
    number_regex = r'\b\d{1,3}\b'
    for instruction in instructions:
        command = clear_instruction(instruction)
        match command:
            case 'do()':
                should_do = True
            case "don't()":
                should_do = False
            case _:
                if should_do:
                    numbers = re.findall(number_regex, command)
                    result += int(numbers[0]) * int(numbers[1])
                
    return result


result_part1 = part1(input)
print(result_part1)

result_part2 = part2(input)
print(result_part2)
