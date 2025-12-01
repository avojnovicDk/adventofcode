from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


@register_solution(2025, 1, 1)
def part_one(input_file_path: str):
    pos = 50
    return sum(
        (pos := pos + int(line.strip().replace("L", "-").replace("R", ""))) % 100 == 0
        for line in yield_lines(input_file_path)
    )

@register_solution(2025, 1, 2)
def part_two(input_file_path: str):
    pos, counter = 50, 0
    for line in yield_lines(input_file_path):
        change = int(line.strip().replace("L", "-").replace("R", ""))
        pos += change
        if pos <= 0 and pos != change:
            counter += 1
        clicks, abs_pos = divmod(abs(pos), 100)
        pos = 100 - abs_pos if pos * abs_pos < 0 else abs_pos
        counter += clicks

    return counter


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 1)
    part_one(input_file_path)
    part_two(input_file_path)
