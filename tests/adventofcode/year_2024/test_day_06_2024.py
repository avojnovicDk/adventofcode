import os
from adventofcode.year_2024.day_06_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_06.txt") == 41


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_06.txt") == 6


def test_part_two_edge_case():
    assert part_two(f"{DIR_NAME}/inputs/day_06_edge_case.txt") == 1
