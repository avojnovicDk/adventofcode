from itertools import product

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path
from adventofcode.util.input_helpers import yield_lines


outside_area, air_pocket_area = set(), set()

def _is_neighbour(cube_a, cube_b):
    pairs = zip(cube_a, cube_b)
    has_different_dimension = False
    for a, b in pairs:
        if a != b:
            if has_different_dimension:
                return False
            has_different_dimension = True
            if abs(a - b) > 1:
                return False
    return True

def _is_air_pocket(curr, cubes, visited, min_p, max_p):
    global outside_area
    global air_pocket_area
    if curr in cubes:
        return False
    for p in curr:
        if p in (min_p, max_p):
            return False
    x, y, z = curr
    possible = {
        (x - 1, y,     z),
        (x + 1, y,     z),
        (x,     y - 1, z),
        (x,     y + 1, z),
        (x,     y,     z - 1),
        (x,     y,     z + 1),
    } - cubes - visited
    for pos in possible:
        visited.add(pos)
        if _is_air_pocket(pos, cubes, visited, min_p, max_p) is False:
            outside_area |= visited
            return False
    air_pocket_area |= visited
    return True

def _calc_all_sides(line_yielder):
    cubes = set()
    sides = 0
    for line in line_yielder:
        cube = tuple(map(int, line.strip().split(',')))
        sides += 6
        for other_cube in cubes:
            if _is_neighbour(cube, other_cube):
                sides -= 2
        cubes.add(cube)
    return sides, cubes


@register_solution(2022, 18, 1)
def part_one(input_file_path: str):
    sides, _ = _calc_all_sides(yield_lines(input_file_path))
    return sides


@register_solution(2022, 18, 2)
def part_two(input_file_path: str):
    sides, cubes = _calc_all_sides(yield_lines(input_file_path))
    min_p = min(min(cube) for cube in cubes)
    max_p = max(max(cube) for cube in cubes)

    air_pockets = set()
    for curr in product(range(min_p, max_p + 1), repeat=3):
        if curr in outside_area:
            continue
        if curr in air_pocket_area or _is_air_pocket(curr, cubes, {curr}, min_p, max_p):
            sides -= 6
            for air_pocket in air_pockets:
                if _is_neighbour(curr, air_pocket):
                    sides += 2
            air_pockets.add(curr)

    return sides


if __name__ == '__main__':
    input_file_path = get_input_file_path(2022, 18)
    part_one(input_file_path)
    part_two(input_file_path)
