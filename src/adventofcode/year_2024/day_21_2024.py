from collections import defaultdict
from itertools import product
from typing import Generator

from adventofcode.registry.decorators import register_solution
from adventofcode.util.helpers import memoize
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


NUMBER_KEYPAD = (
    "789",
    "456",
    "123",
    " 0A"
)


NUMBER_POSITIONS = dict()
POSITION_NUMBERS = dict()
for i, line in enumerate(NUMBER_KEYPAD):
    for j, number in enumerate(line):
        if number.strip():
            NUMBER_POSITIONS[i + j * 1j] = number
            POSITION_NUMBERS[number] = i + j * 1j


DIRECTIONAL_KEYPAD = (
    " ^A",
    "<v>",
)


DIRECTION_POSITIONS = dict()
POSITION_DIRECTIONS = dict()
for i, line in enumerate(DIRECTIONAL_KEYPAD):
    for j, number in enumerate(line):
        if number.strip():
            DIRECTION_POSITIONS[i + j * 1j] = number
            POSITION_DIRECTIONS[number] = i + j * 1j


DIRECTION_CPLX_TO_SIGN = {
    -1: "^",
    1: "v",
    -1j: "<",
    1j: ">",
}


COMMANDS_CACHE = defaultdict(list)


def _yield_commands(
        positions: dict[complex, str], start: complex, end: complex, visited: set[complex], commands: str
) -> Generator[str, None, None]:
    key = (tuple(positions.values()), start, end)
    if not visited:
        if key in COMMANDS_CACHE:
            yield from COMMANDS_CACHE[key]
        else:
            visited = {start}

    for direction, command in DIRECTION_CPLX_TO_SIGN.items():
        curr = start + direction
        if curr == end:
            COMMANDS_CACHE[key].append(commands + command + "A")
            yield commands + command + "A"
        if curr in positions and curr not in visited:
            yield from _yield_commands(positions, curr, end, visited | {curr}, commands + command)


def _get_directions(code: str) -> list[str]:
    shortest_commands = list()
    start = "A"
    for n in code:
        commands = list(_yield_commands(NUMBER_POSITIONS, POSITION_NUMBERS[start], POSITION_NUMBERS[n], set(), ""))
        shortest_commands.append([c for c in commands if len(c) == min(len(c) for c in commands)])
        start = n
    
    return [
        [
            POSITION_DIRECTIONS[command]
            for number_command in complete_command
            for command in number_command
        ]
        for complete_command in product(*shortest_commands)
    ]


@memoize
def _get_min_len(start: int, end: int, max_level: int, level: int = 0) -> int:
    if start == end or level == max_level:
        return 1
    
    commands = list(_yield_commands(DIRECTION_POSITIONS, start, end, set(), "A"))
    
    return min(
        sum(
            _get_min_len(POSITION_DIRECTIONS[start], POSITION_DIRECTIONS[end], max_level, level + 1)
            for start, end in zip(command[:-1], command[1:])
        )
        for command in commands
        if len(command) == min(len(p) for p in commands)
    )


def _get_sum_of_complexities(input_file_path: str, no_of_directional_keypads: int) -> int:
    return sum(
        int(code.replace("A", "")) * min(
            sum(
                _get_min_len(start, end, no_of_directional_keypads)
                for start, end in zip([POSITION_DIRECTIONS["A"]] + input[:-1], input)
            )
            for input in _get_directions(code.strip())
        )
        for code in yield_lines(input_file_path)
    )


@register_solution(2024, 21, 1)
def part_one(input_file_path: str) -> int:
    return _get_sum_of_complexities(input_file_path, 2)


@register_solution(2024, 21, 2)
def part_two(input_file_path: str) -> int:
    return _get_sum_of_complexities(input_file_path, 25)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 21)
    part_one(input_file_path)
    part_two(input_file_path)
