import os
import sys

from graph import Graph
from typing import List, Tuple

def read_input() -> Tuple[Graph, List[List[str]]]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        data = file.read().strip().split('\n\n')
        graph_edges = list(map(lambda x: x.split('|'), data[0].split('\n')))
        print_order = list(map(lambda x: x.split(','), data[1].split('\n')))

        return Graph(graph_edges), print_order

rule_graph, page_orders = read_input()

def part1(rule_graph: Graph, print_orders: List[List[str]]) -> int:
    result = 0
    
    for print_order in print_orders:
        if rule_graph.is_print_order_correct(print_order):
            middle = (len(print_order) - 1) // 2
            result += int(print_order[middle])

    return result

def part2(rule_graph: Graph, print_orders: List[List[str]]) -> int:
    result = 0

    for print_order in print_orders:
        if not rule_graph.is_print_order_correct(print_order):
            fixed = rule_graph.fix_print_order(print_order)
            middle = (len(fixed) - 1) // 2
            result += int(fixed[middle])

    return result

result_part1 = part1(rule_graph, page_orders)
print(result_part1)

result_part2 = part2(rule_graph, page_orders)
print(result_part2)