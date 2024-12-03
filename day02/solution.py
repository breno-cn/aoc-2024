import os
import sys

from typing import List, Set

def read_input() -> List[List[int]]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        data = file.read().strip().split('\n')
        rows = [row.split() for row in data]

        return [list(map(int, row)) for row in rows]

input = read_input()

def report_breaks_order(report: List[int]) -> Set[int]:
    is_crescent = report[0] < report[1]
    index = set()

    for i in range(len(report) - 1):
        if is_crescent:
            if report[i] > report[i + 1]:
                if i > 0:
                    index.add(i - 1)
                index.add(i)
                index.add(i + 1)
        else:
            if report[i] < report[i + 1]:
                if i > 0:
                    index.add(i - 1)
                index.add(i)
                index.add(i + 1)

    return index

def where_report_is_unsafe(report: List[int]) -> Set[int]:
    unsafe_index = set()

    for i in range(len(report) - 1):
        difference = abs(report[i] - report[i + 1])
        if difference < 1 or difference > 3:
            if i > 0:
                unsafe_index.add(i - 1)
            unsafe_index.add(i)
            unsafe_index.add(i + 1)
        
    return unsafe_index

def part1(input: List[List[int]]) -> int:
    result = 0

    for report in input:
        if not where_report_is_unsafe(report) and not report_breaks_order(report):
            result += 1

    return result

def part2(input: List[List[int]]) -> int:
    result = 0
    for report in input:
        unsafe_index = where_report_is_unsafe(report)
        break_order_index = report_breaks_order(report)

        if not unsafe_index and not break_order_index:
            result += 1
            continue
        
        test_index = unsafe_index.union(break_order_index)
        for index in test_index:
            new_report = report[:index] + report[index+1:]
            if not where_report_is_unsafe(new_report) and not report_breaks_order(new_report):
                result += 1
                break

    return result

result_part1 = part1(input)
print(result_part1)

result_part2 = part2(input)
print(result_part2)
