from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path


@register_solution(2024, 1, 1)
def part_one(input_file_path: str):
    raise SolutionNotFoundError(2024, 1, 1)


@register_solution(2024, 1, 2)
def part_two(input_file_path: str):
    raise SolutionNotFoundError(2024, 1, 2)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 1)
    part_one(input_file_path)
    part_two(input_file_path)
