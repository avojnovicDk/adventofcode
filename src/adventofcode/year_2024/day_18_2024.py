from math import ceil, floor
from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _get_heuristic(start, end):
    return (abs(start.real - end.real) + abs(start.imag - end.imag))


def _part_one(input_file_path: str, size: int, number_of_bytes: int):
    obstacles = set()
    for line in yield_lines(input_file_path):
        x, y = line.strip().split(",")
        obstacles.add(int(x) + int(y) * 1j)
        if len(obstacles) == number_of_bytes:
            break

    for i in range(size):
        obstacles |= {
            -1 + (i * 1j),
            size + (i * 1j),
            i - 1j,
            i + (size * 1j),
        }
    
    end = (size - 1) + (size - 1) * 1j
    positions_to_process = {0}
    g_score = {0: 0}
    f_score = {0: _get_heuristic(0, end)}

    while positions_to_process:
        current = sorted(positions_to_process, key=f_score.get)[0]
        if current == end:
            return g_score[current]
        
        positions_to_process.remove(current)
        for direction in (1, -1, 1j, -1j):
            neighbour = current + direction
            if neighbour in obstacles:
                continue
            if g_score[current] + 1 < g_score.get(neighbour, size * size):
                g_score[neighbour] = g_score[current] + 1
                f_score[neighbour] = g_score[neighbour] + _get_heuristic(neighbour, end)
                positions_to_process.add(neighbour)


def _has_path(obstacles, size):
    for i in range(size):
        obstacles |= {
            -1 + (i * 1j),
            size + (i * 1j),
            i - 1j,
            i + (size * 1j),
        }
    
    end = (size - 1) + (size - 1) * 1j
    positions_to_process = {0}

    while positions_to_process:
        current = positions_to_process.pop()
        if current == end:
            return True
        
        obstacles.add(current)
        for direction in (1, -1, 1j, -1j):
            neighbour = current + direction
            if neighbour not in obstacles:
                positions_to_process.add(neighbour)
    
    return False


def _part_two(input_file_path: str, size: int):
    obstacles = list()
    for line in yield_lines(input_file_path):
        x, y = line.strip().split(",")
        obstacles.append(int(x) + int(y) * 1j)
    
    max_has_path, min_has_not_path = 0, len(obstacles)
    while min_has_not_path - max_has_path > 1:
        current_number_of_bytes = max_has_path + ((min_has_not_path - max_has_path) // 2)
        if _has_path(set(obstacles[:current_number_of_bytes]), size):
            if max_has_path < current_number_of_bytes:
                max_has_path = current_number_of_bytes
        else:
            if min_has_not_path > current_number_of_bytes:
                min_has_not_path = current_number_of_bytes
    return obstacles[min_has_not_path - 1]


@register_solution(2024, 18, 1)
def part_one(input_file_path: str):
    return _part_one(input_file_path, 71, 1024)


@register_solution(2024, 18, 2)
def part_two(input_file_path: str):
    return _part_two(input_file_path, 71)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 18)
    part_one(input_file_path)
    part_two(input_file_path)
