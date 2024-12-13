from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _calc_perimeter(plots, region, position):
    if position in region:
        return 0
    region.add(position)

    return sum(
        _calc_perimeter(plots, region, position + direction)
        if plots.get(position + direction) == plots[position] else 1
        for direction in (-1, 1, -1j, 1j)
    )
            

@register_solution(2024, 12, 1)
def part_one(input_file_path: str) -> int:
    plots = dict()
    for i, line in enumerate(yield_lines(input_file_path)):
        for j, plot in enumerate(line.strip()):
            plots[i + j * 1j] = plot

    price = 0
    remaining_plots = set(plots.keys())
    while remaining_plots:
        region = set()
        perimeter = _calc_perimeter(plots, region, next(iter(remaining_plots)))
        price += len(region) * perimeter
        remaining_plots -= region
    
    return price


# @register_solution(2024, 12, 2)
# def part_two(input_file_path: str):
#     raise SolutionNotFoundError(2024, 12, 2)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 12)
    part_one(input_file_path)
    # part_two(input_file_path)
