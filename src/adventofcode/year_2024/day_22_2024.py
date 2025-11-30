from collections import defaultdict
from math import floor
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_changes(secret: int, no_of_iterations: int):
    for _ in range(no_of_iterations):
        last_digit = secret % 10
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ floor(secret / 32)) % 16777216
        secret = (secret ^ secret * 2048) % 16777216
        yield ((secret % 10) - last_digit), secret % 10
    return secret


def _get_next_secret(secret: int, no_of_iterations: int):
    for _ in range(no_of_iterations):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ floor(secret / 32)) % 16777216
        secret = (secret ^ secret * 2048) % 16777216
    return secret


@register_solution(2024, 22, 1)
def part_one(input_file_path: str):
    return sum(
        _get_next_secret(int(line), 2000)
        for line in yield_lines(input_file_path)
    )


@register_solution(2024, 22, 2)
def part_two(input_file_path: str):
    combinations = defaultdict(int)
    lines = list()
    for line in yield_lines(input_file_path):
        line = int(line.strip())
        lines.append(line)
        current = list()
        current_combinations = set()
        for c, bananas in _yield_changes(int(line), 2000):
            current.append(c)
            if len(current) == 4:
                if tuple(current) not in current_combinations:
                    current_combinations.add(tuple(current))
                    combinations[tuple(current)] += bananas
                current.pop(0)

    return max(combinations.values())


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 22)
    part_one(input_file_path)
    part_two(input_file_path)
