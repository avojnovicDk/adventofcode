from collections import defaultdict
from copy import copy
from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_possible_directions(position: complex, direction, impossible_positions: set[complex]):
    if position + direction not in impossible_positions:
        yield direction
    for direction in {1, -1, 1j, -1j} - {direction}:
        if position + direction not in impossible_positions:
            yield direction

MAX = 99999999999999999
COUNTER = 0
    
# def _explore(position: complex, direction: complex, walls: set[complex], explored: set[complex], end: complex):
#     global MAX
#     global COUNTER
#     COUNTER += 1
#     # print(position)
#     # if COUNTER == 10:
#     #     return
#     if position == end:
#         yield 0
#     for new_direction in _yield_possible_directions(position, direction, walls | explored):
#         if new_direction != direction:
#             new_explored = copy(explored)
#             new_explored.add(position + new_direction)
#             for e in _explore(position + new_direction, new_direction, walls, new_explored, end):
#                 # print(e + 1001)
#                 if e + 1001 < MAX:
#                     yield e + 1001
#         else:
#             explored.add(position + new_direction)
#             for e in _explore(position + new_direction, new_direction, walls, explored, end):
#                 # print(e + 1)
#                 if e + 1 < MAX:
#                     yield e + 1


def _get_heuristic(start: complex, end: complex):
    real = abs(start.real - end.real)
    imag = abs(start.imag - end.imag)

    return real + imag + (0 if real * imag == 0 else 1000)


def _calc_score(came_from, current, direction):
    score = 0
    while current in came_from:
        new_current = came_from[current]  # {current: previous}, new_current == previous
        new_direction = current - new_current
        # new_direction = directions[new_current]
        score += 1 if new_direction == direction else 1001
        current = new_current
        direction = new_direction
    print(direction, score)
    if direction != 1j:
        score += 1000
    return score

def _backtrack(current, came_from):
    path = [current]
    while current in came_from:
        path = [came_from[current]] + path
        current = came_from[current]
    return path


@register_solution(2024, 16, 1)
def part_one(input_file_path: str):
    walls = set()
    start, end = None, None
    i = 0
    for line in yield_lines(input_file_path):
        for j, c in enumerate(line.strip()):
            match c:
                case "#":
                    walls.add(i + j * 1j)
                case "S": 
                    start = i + j * 1j
                case "E":
                    end = i + j * 1j
        i += 1
    
    open_set = {start}
    came_from = dict()
    g_score = {start: 0}
    f_score = {start: _get_heuristic(start, end)}
    # directions = {start: 1j}

    while open_set:
        current = sorted(open_set, key=f_score.get)[0]
        path = _backtrack(current, came_from)
        for i in range(len(line)):
            print("".join("#" if i + j * 1j in walls else ("S" if i + j * 1j == start else ("E" if i + j * 1j == end else ("-" if i + j * 1j in path else "."))) for j in range(len(line))))
        if current == start:
            current_direction = 1j
        else:
            current_direction = current - came_from[current]  # current = (5+3j), came_from = (4+3j) => going down, direction == 1
        if current == end:
            # return g_score[current]
            return _calc_score(came_from, current, current_direction)
        
        open_set.remove(current)    
        for direction in {-1, 1, -1j, 1j} - {-1 * current_direction}:
            neighbour = current + direction
            if neighbour in walls:
                continue
            tentative_g_score = g_score[current] + (1 if direction == current_direction else 1001)
            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + _get_heuristic(neighbour, end)
                # directions[neighbour] = direction
                open_set.add(neighbour)
    
                
            


    # global MAX
    # for e in _explore(start, 1, walls, set(), end):
    #     # print(e)
    #     if e < MAX:
    #         MAX = e
    # # print(MAX)
    # return MAX
        


@register_solution(2024, 16, 2)
def part_two(input_file_path: str):
    return True
    raise SolutionNotFoundError(2024, 16, 2)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 16)
    part_one(input_file_path)
    part_two(input_file_path)
