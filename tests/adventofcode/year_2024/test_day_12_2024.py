import os
from adventofcode.year_2024.day_12_2024 import part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test_part_one_a():
    assert part_one(f"{DIR_NAME}/inputs/day_12_a.txt") == 140


def test_part_one_b():
    assert part_one(f"{DIR_NAME}/inputs/day_12_b.txt") == 772


def test_part_one_c():
    assert part_one(f"{DIR_NAME}/inputs/day_12_c.txt") == 1930


def test_part_two_a():
    assert part_two(f"{DIR_NAME}/inputs/day_12_a.txt") == 80


def test_part_two_b():
    assert part_two(f"{DIR_NAME}/inputs/day_12_b.txt") == 436


def test_part_two_c():
    assert part_two(f"{DIR_NAME}/inputs/day_12_c.txt") == 1206


def test_part_two_d():
    assert part_two(f"{DIR_NAME}/inputs/day_12_d.txt") == 236


def test_part_two_e():
    assert part_two(f"{DIR_NAME}/inputs/day_12_e.txt") == 368