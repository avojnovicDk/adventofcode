from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_changes(input_file_path: str):
    for line in yield_lines(input_file_path):
        yield int(line.strip().replace("L", "-").replace("R", ""))


@register_solution(2025, 1, 1)
def part_one(input_file_path: str):
    pos, changes = 50, _yield_changes(input_file_path)
    return sum(not (pos := pos + change) % 100 for change in changes)


def _yield_clicks(changes):
    pos = 50
    for change in changes:
        if (pos := pos + change) <= 0 and pos != change:
            yield 1
        clicks, abs_pos = divmod(abs(pos), 100)
        yield clicks
        pos = 100 - abs_pos if pos * abs_pos < 0 else abs_pos


@register_solution(2025, 1, 2)
def part_two(input_file_path: str):
    return sum(_yield_clicks(_yield_changes(input_file_path)))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 1)
    part_one(input_file_path)
    part_two(input_file_path)
