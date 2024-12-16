import os
import sys

from typing import Tuple, List, Optional

from enum import Enum

class NodeMark(Enum):
    UNMARKED = 1
    TEMPORARY_MARKED = 2
    MARKED = 3

class Direction:
    # (x, y)
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def out_of_bounds(x: int, y: int, room: List[List[str]]) -> bool:
    room_height = len(room)
    room_width = len(room[0])

    return x >= room_width or y >= room_height or x < 0 or y < 0

def edges(x: int, y: int, room: List[List[str]]):
    result = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            _x = x + j
            _y = x + i
            if out_of_bounds(_x, _y, room):
                continue

            if room[y][x] == '#':
                continue

            result.append((x, y))

    return result

def get_vertices(room: List[List[str]]) -> List[Tuple[int, int]]:
    result = set()

    for y in range(len(room)):
        for x in range(len(room[y])):
            if room[y][x] == '.':
                result.add((x, y))

    return list(result)
                

class Guard:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.direction = Direction.UP

    def forward(self) -> Tuple[int]:
        x = self.x + self.direction[0]
        y = self.y + self.direction[1]

        return x, y
    
    def turn_right(self):
        match self.direction:
            case Direction.UP:
                self.direction = Direction.RIGHT
            case Direction.RIGHT:
                self.direction = Direction.DOWN
            case Direction.DOWN:
                self.direction = Direction.LEFT
            case Direction.LEFT:
                self.direction = Direction.UP

    def walk(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def patrol(self, original_room: List[List[str]]) -> Optional[Tuple[int, int]]:
        room = original_room.copy()
        trail = []

        while True:
            room[self.y][self.x] = 'X'

            next_x, next_y = self.forward()

            if out_of_bounds(next_x, next_y, room):
                return self.x, self.y

            if room[next_y][next_x] == '#':
                self.turn_right()

            trail.append((self.x, self.y))
            self.walk()            
            

def read_input() -> Tuple[Guard, List[List[str]]]:
    filepath = os.path.join(sys.path[0], 'input.txt')

    with open(filepath, 'r') as file:
        room = list(map(list, file.read().strip().split('\n')))

        for y in range(len(room)):
            for x in range(len(room[y])):
                if room[y][x] == '^':
                    return Guard(x, y), room

def part1(guard: Guard, room: List[List[str]]) -> int:
    guard.patrol(room)

    result = 0
    for row in room:
        for tile in row:
            if tile == 'X':
                result += 1
    
    return result


mem = set()
def dfs(room):

    def visit(node, marks, room):
        if node not in marks:
            marks[node] = NodeMark.UNMARKED

        if marks[node] == NodeMark.MARKED:
            return
            
        if marks[node] == NodeMark.TEMPORARY_MARKED:
            # print('asaaa', node)
            if node not in mem:
                mem.add(node)
                raise Exception()
            return

        marks[node] = NodeMark.TEMPORARY_MARKED

        for v in edges(node[0], node[1], room):
            visit(v, marks, room)

        marks[node] = NodeMark.MARKED

    def all_nodes_permanent_marked(marks):
        for node in marks.keys():
            if marks[node] != NodeMark.MARKED:
                return False
                
        return True

    marks = dict()
    nodes = get_vertices(room)
    # print(nodes)
    # print(len(nodes))
    for node in nodes:
        marks[node] = NodeMark.UNMARKED

    while not all_nodes_permanent_marked(marks):
        node = nodes.pop()
        # if marks[node] == NodeMark.MARKED:
            # continue

        visit(node, marks, room)


def part2(room: List[List[str]]) -> int:
    room_height = len(room)
    room_width = len(room[0])

    vertices = get_vertices(room)
    result = 0
    # print(vertices)
    for v in vertices:
        x, y = v
        if room[y][x] != '.':
            continue
        
        room[y][x] = '#'

        try:
            # TODO dfs to check for circuits
            dfs(room)
        except Exception:
            result += 1

        room[y][x] = '.'
    
    return result

guard, room = read_input()

result_part1 = part1(guard, room)
print(result_part1)

result_part2 = part2(room)
print(result_part2)