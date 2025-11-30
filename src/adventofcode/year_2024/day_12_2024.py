from adventofcode.registry.decorators import register_solution
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


def _yield_region(plots):
    other_regions = set(plots.keys())
    while other_regions:
        pos = other_regions.pop()
        plant = plots[pos]
        region = {pos}
        processed_positions = set()

        while region - processed_positions:
            pos = (region - processed_positions).pop()
            processed_positions.add(pos)
            for dir in (-1, 1, -1j, 1j):
                next_pos = pos + dir
                if next_pos not in region and plots.get(next_pos) == plant:
                    region.add(next_pos)

        yield region
        other_regions = other_regions - region


def _calc_sides(region):
    walls = list()
    sides = 0
    for curr in region:
        for dir in (-1, 1, -1j, 1j):
            if (curr + dir) not in region:
                walls.append(curr + dir)

    sides = 0
    while walls:
        curr = walls.pop()
        sides += 1
        done = False
        for dir in (-1, 1):
            new_curr = curr
            while (new_curr + dir) in walls:
                done = True
                new_curr += dir
                walls.remove(new_curr)
        if not done:
            for dir in (-1j, 1j):
                new_curr = curr
                while (new_curr + dir) in walls:
                    new_curr += dir
                    walls.remove(new_curr)
    return sides


@register_solution(2024, 12, 2)
def part_two(input_file_path: str):
    plots = dict()
    for i, line in enumerate(yield_lines(input_file_path)):
        for j, plot in enumerate(line.strip()):
            plots[i + j * 1j] = plot

    price = 0
    for region in _yield_region(plots):
        sides = _calc_sides(region)
        price += len(region) * sides

    return price


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 12)
    part_one(input_file_path)
    part_two(input_file_path)
