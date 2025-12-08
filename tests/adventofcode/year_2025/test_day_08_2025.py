import os
from adventofcode.year_2025.day_08_2025 import part_one_with_iterations, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one_with_iterations(f"{DIR_NAME}/inputs/day_08.txt", 10) == 40


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_08.txt") == 25272
