from functools import reduce
from typing import Generator, Self

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _yield_game_and_cubes(input_file_path) -> Generator[tuple[str], None, None]:
    for line in yield_lines(input_file_path):
        yield line.replace(";", ",").split(":")


class MaxCubes(dict[str, int]):
    def yield_not_enoughs(self, cubes: str) -> Generator[tuple[str, int], None, None]:
        for cube in cubes.split(","):
            count, color = cube.split()
            count = int(count)
            if self[color] < count:
                yield color, count
    
    def update(self, cubes: str) -> Self:
        for color, count in self.yield_not_enoughs(cubes):
            self[color] = count
        return self
        

@register_solution(2023, 2, 1)
def part_one(input_file_path: str) -> int:
    mc = MaxCubes(red=12, green=13, blue=14)
    return sum(
        int(game_tag.split()[1])
        for game_tag, cubes in _yield_game_and_cubes(input_file_path)
        if next(mc.yield_not_enoughs(cubes), None) is None
    )


@register_solution(2023, 2, 2)
def part_two(input_file_path: str) -> int:
    return sum(
        reduce(
            lambda x, y: x * y,
            MaxCubes(red=0, green=0, blue=0).update(cubes).values()
        )
        for _, cubes in _yield_game_and_cubes(input_file_path)
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2023, 2)
    part_one(input_file_path)
    part_two(input_file_path)
