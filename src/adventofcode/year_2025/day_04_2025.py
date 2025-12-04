from collections import Counter

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_points


def _yield_9_square(point):
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            yield point + dx + dy * 1j


def _init_rolls(input_file_path):
    rolls = Counter({point: 3 for point, c in yield_points(input_file_path) if c == '@'})

    for roll in rolls:
        for dp in _yield_9_square(roll):
            if dp == roll:
                continue
            elif dp in rolls:
                rolls[dp] -= 1

    return rolls


def _yield_moved_rolls(rolls):
    movable = True

    while movable:
        movable = [k for k, v in rolls.items() if v >= 0]
        yield len(movable)

        for roll in movable:
            for dp in _yield_9_square(roll):
                if dp == roll:
                    del rolls[dp]
                elif dp in rolls:
                    rolls[dp] += 1


@register_solution(2025, 4, 1)
def part_one(input_file_path: str):
    return len([k for k, v in _init_rolls(input_file_path).items() if v >= 0])


@register_solution(2025, 4, 2)
def part_two(input_file_path: str):
    return sum(_yield_moved_rolls(_init_rolls(input_file_path)))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 4)
    part_one(input_file_path)
    part_two(input_file_path)
