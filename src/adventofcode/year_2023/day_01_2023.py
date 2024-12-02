from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _get_edge_value(line: str, valid_mappings: dict[tuple[str], int], is_start: bool) -> int:
    edgewith = getattr(line, "startswith" if is_start else "endswith")
    start_index = 0 if is_start else None
    end_index = None if is_start else len(line) - 1
    for _ in range(len(line)):
        for valid_strings, value in valid_mappings.items():
            if edgewith(valid_strings, start_index, end_index):
                return value
        if is_start:
            start_index += 1
        else:
            end_index -= 1
            

def _calc_calibration_value(line: str, valid_mappings: dict[tuple[str], int]) -> int:
    first, last = _get_edge_value(line, valid_mappings, True), _get_edge_value(line, valid_mappings, False)
    return first * 10 + last


@register_solution(2023, 1, 1)
def part_one(input_file_path: str):
    valid_mappings = {(number,): int(number) for number in DIGITS.values()}
    return sum(_calc_calibration_value(line, valid_mappings) for line in yield_lines(input_file_path))


@register_solution(2023, 1, 2)
def part_two(input_file_path: str):
    valid_mappings = {(number_string, number): int(number) for number_string, number in DIGITS.items()}
    return sum(_calc_calibration_value(line, valid_mappings) for line in yield_lines(input_file_path))


if __name__ == '__main__':
    input_file_path = get_input_file_path(2023, 1)
    part_one(input_file_path)
    part_two(input_file_path)
