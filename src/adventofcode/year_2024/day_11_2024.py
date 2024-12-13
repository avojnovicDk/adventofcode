from typing import Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


BLINK_CACHE = {}


def _yield_new_stones(stone: int) -> Generator[int, None, None]:
    if stone == 0:
        yield 1
    elif len(str(stone)) % 2 == 1:
        yield stone * 2024
    else:
        stone = str(stone)
        yield int(stone[:len(stone) // 2])
        yield int(stone[len(stone) // 2:])
    

def _blink(stone: int, blinks_left: int) -> int:
    if blinks_left == 0:
        return 1
    
    if (stone, blinks_left) not in BLINK_CACHE:
        BLINK_CACHE[(stone, blinks_left)] = sum(
            _blink(new_stone, blinks_left - 1)
            for new_stone in _yield_new_stones(stone)
        )

    return BLINK_CACHE[(stone, blinks_left)]


@register_solution(2024, 11, 1)
def part_one(input_file_path: str) -> int:
    return sum(
        _blink(int(stone), 25)
        for stone in read_file(input_file_path).split()
    )


@register_solution(2024, 11, 2)
def part_two(input_file_path: str) -> int:
    return sum(
        _blink(int(stone), 75)
        for stone in read_file(input_file_path).split()
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 11)
    part_one(input_file_path)
    part_two(input_file_path)
