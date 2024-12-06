from typing import List
from collections import defaultdict
from enum import Enum

class NodeMark(Enum):
    UNMARKED = 1
    TEMPORARY_MARKED = 2
    MARKED = 3

def swap(print_order: List[str], i: int, j: int):
    print_order[i], print_order[j] = print_order[j], print_order[i]

class Graph:
    def __init__(self, edges: List[List[str]]):
        self.edges = defaultdict(list)

        for edge in edges:
            self.edges[edge[0]].append(edge[1])

    def is_print_order_correct(self, print_order: List[str]) -> bool:
        for i in range(len(print_order) - 1):
            current_page = print_order[i]
            next_page = print_order[i + 1]

            if next_page not in self.edges[current_page]:
                return False

        return True

    def fix_print_order(self, print_order: List[str]) -> List[str]:
        def visit(node, marks, fixed_order, graph):
            if node not in marks:
                marks[node] = NodeMark.UNMARKED

            if marks[node] == NodeMark.MARKED:
                return
            
            if marks[node] == NodeMark.TEMPORARY_MARKED:
                return
            
            marks[node] = NodeMark.TEMPORARY_MARKED

            for m in graph.edges[node]:
                visit(m, marks, fixed_order, graph)

            marks[node] = NodeMark.MARKED
            fixed_order.append(node)

        def all_nodes_permanent_marked(marks):
            for node in marks.keys():
                if marks[node] != NodeMark.MARKED:
                    return False
                
            return True

        graph = Graph([])
        for page in print_order:
            for v in self.edges[page]:
                if v in print_order and v != page:
                    graph.edges[page].append(v)

        fixed_order = []
        nodes = set(graph.edges.keys())
        marks = dict()
        for node in nodes:
            marks[node] = NodeMark.UNMARKED

        while not all_nodes_permanent_marked(marks):
            node = nodes.pop()
            if marks[node] == NodeMark.MARKED:
                continue
            visit(node, marks, fixed_order, graph)

        return fixed_order
