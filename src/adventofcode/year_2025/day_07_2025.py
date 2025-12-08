from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path
from adventofcode.util.input_helpers import yield_lines


def _get_map_data(file_path):
    splitters = set()
    for row, line in enumerate(yield_lines(file_path)):
        for col, char in enumerate(line.strip()):
            if char == '^':
                splitters.add(row + col * 1j)
            elif char == 'S':
                start = row + col * 1j

    return start, (row, col), splitters


def _count_splitters_hit(pos, row, col, splitters, visited):
    if pos in visited:
        return 0
    visited.add(pos)

    while True:
        pos += 1
        if pos in visited or pos.real >= row or pos.imag < 0 or pos.imag >= col:
            return 0
        elif pos in splitters:
            return (
                1
                + _count_splitters_hit(pos - 1j, row, col, splitters, visited)
                + _count_splitters_hit(pos + 1j, row, col, splitters, visited)
            )
        else:
            visited.add(pos)


@register_solution(2025, 7, 1)
def part_one(input_file_path: str):
    start, (row, col), splitters = _get_map_data(input_file_path)

    return _count_splitters_hit(start, row, col, splitters, set())


def _count_timelines(pos, row, col, splitters, visited):
    if pos in visited:
        return visited[pos]
    
    while True:
        pos += 1
        if pos in visited:
            return visited[pos]
        if pos.real == row:
            visited[pos] = 1
            return 1
        if pos.imag < 0 or pos.imag >= col:
            return 0
        elif pos in splitters:
            visited[pos] = (
                _count_timelines(pos - 1j, row, col, splitters, visited)
                + _count_timelines(pos + 1j, row, col, splitters, visited)
            )
            return visited[pos]


@register_solution(2025, 7, 2)
def part_two(input_file_path: str):
    start, (row, col), splitters = _get_map_data(input_file_path)

    return _count_timelines(start, row, col, splitters, dict())


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 7)
    part_one(input_file_path)
    part_two(input_file_path)
