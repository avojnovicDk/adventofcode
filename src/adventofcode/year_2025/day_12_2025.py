from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_regions(file_path):
    for line in yield_lines(file_path):
        try:
            region, counters = line.strip().split(':')
            width, length = map(int, region.split('x'))
            yield width, length, tuple(map(int, counters.strip().split(' ')))
        except ValueError:
            pass


@register_solution(2025, 12, 1)
def part_one(input_file_path: str):
    return sum(
        sum(counters) <= width // 3 * length // 3
        for width, length, counters in _yield_regions(input_file_path)
    )


@register_solution(2025, 12, 2)
def part_two(input_file_path: str):
    ...


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 12)
    part_one(input_file_path)
    part_two(input_file_path)
