import re
from functools import reduce

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


def _sum_valid_multiplications(input: str):
    return sum(
        reduce(lambda x, y: int(x) * int(y), mul.split(","))
        for mul in re.findall(r"mul\((\d+\,\d+)\)", input)
    )
    

@register_solution(2024, 3, 1)
def part_one(input_file_path: str):
    return _sum_valid_multiplications(read_file(input_file_path))


@register_solution(2024, 3, 2)
def part_two(input_file_path: str):
    return sum(
        _sum_valid_multiplications(enabled.split("don't()")[0])
        for enabled in read_file(input_file_path).split("do()")
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 3)
    part_one(input_file_path)
    part_two(input_file_path)
