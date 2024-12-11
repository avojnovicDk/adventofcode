from collections import defaultdict

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input
from adventofcode.util.string_matrix import StringMatrix


def _go_back_and_make_turn(x: int, y: int, dir_x: int, dir_y: int) -> tuple[int, int, int, int]:
    x, y = x - dir_x, y - dir_y

    match (dir_x, dir_y):
        case (-1, 0):
            dir_x, dir_y = 0, 1
        case (0, 1):
            dir_x, dir_y = 1, 0
        case (1, 0):
            dir_x, dir_y = 0, -1
        case (0, -1):
            dir_x, dir_y = -1, 0

    return (x, y, dir_x, dir_y)


def _check_for_loop(lines: StringMatrix, guard: tuple[int, int], obstacle: tuple[int, int]) -> bool:
    x, y = guard
    dir_x, dir_y = (-1, 0)
    directions_for_position = defaultdict(set)
    directions_for_position[(x, y)].add((dir_x, dir_y))

    while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        c = "#" if (x, y) == obstacle else lines[x][y]
        match c:
            case "#":
                x, y, dir_x, dir_y = _go_back_and_make_turn(x, y, dir_x, dir_y)
                directions_for_position[(x, y)].add((dir_x, dir_y))
            case _:
                directions_for_position[(x, y)].add((dir_x, dir_y))
        
        x, y = x + dir_x, y + dir_y
        if (dir_x, dir_y) in directions_for_position.get((x, y), set()):
            return True

    return False


def _get_visited_positions(lines: StringMatrix, guard: tuple[int, int]) -> set[int]:
    visited_positions = set()
    x, y = guard
    dir_x, dir_y = (-1, 0)
    x, y = x + dir_x, y + dir_y

    while 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        match lines[x][y]:
            case "#":
                x, y, dir_x, dir_y = _go_back_and_make_turn(x, y, dir_x, dir_y)
            case _:
                visited_positions.add((x, y))
        x, y = x + dir_x, y + dir_y
    
    return visited_positions


def _count_visited_positions(lines: StringMatrix, x: int, y: int) -> int:
    return len(_get_visited_positions(lines, (x, y))) - 1


def _count_potential_obstacles(lines: StringMatrix, x: int, y: int) -> int:
    return sum(
        1
        for (i, j) in _get_visited_positions(lines, (x, y))
        if (i, j) != (x, y) and _check_for_loop(lines, (x, y), (i, j))
    )


@register_solution(2024, 6, 1)
def part_one(input_file_path: str) -> int:
    return StringMatrix(get_input(input_file_path)).count_from_starting("^", _count_visited_positions) + 1


@register_solution(2024, 6, 2)
def part_two(input_file_path: str):
    return StringMatrix(get_input(input_file_path)).count_from_starting("^", _count_potential_obstacles)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 6)
    part_one(input_file_path)
    part_two(input_file_path)
