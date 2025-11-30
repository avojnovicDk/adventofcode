import os
from adventofcode.year_2024.day_17_2024 import part_one, _part_one, part_two


DIR_NAME, _ = os.path.split(os.path.abspath(__file__))


def test__part_one():
    examples = (
        ({"C": 9}, "2,6", {"B": 1}),
        ({"A": 10}, "5,0,5,1,5,4", {"output": "0,1,2"}),
        ({"A": 2024}, "0,1,5,4,3,0", {"A": 0, "output": "4,2,5,6,7,7,7,7,3,1,0"}),
        ({"B": 29}, "1,7", {"B": 26}),
        ({"B": 2024, "C": 43690}, "4,0", {"B": 44354}),
    )
    for registry, program, expect in examples:
        output = _part_one(registry, program)
        for k, v in expect.items():
            assert v == (output if k == "output" else registry[k])


def test_part_one():
    assert part_one(f"{DIR_NAME}/inputs/day_17.txt") == "4,6,3,5,6,3,5,2,1,0"


def test_part_two():
    assert part_two(f"{DIR_NAME}/inputs/day_17.txt") == 'x'
