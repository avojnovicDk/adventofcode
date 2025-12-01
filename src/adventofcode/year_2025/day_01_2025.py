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
        new_pos = pos + change
        if new_pos <= 0 and pos > 0:
            counter += 1
        q, reminder = divmod(abs(new_pos), 100)
        new_pos = 100 - reminder if new_pos < 0 else reminder
        if new_pos == 100:
            new_pos = 0
        counter += q
        pos = new_pos

    return counter


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 1)
    part_one(input_file_path)
    part_two(input_file_path)
