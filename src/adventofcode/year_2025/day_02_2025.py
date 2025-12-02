from itertools import count, takewhile

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


def _yield_invalid_ids(range, repeater):
    start, end = map(int, range.split("-"))
    for seq in takewhile(lambda seq: int(seq + seq) <= end, map(str, count(1))):
         for invalid_id in repeater(seq):
            if invalid_id >= start:
                if invalid_id <= end:
                    yield invalid_id
                else:
                     break


def _yield_repeated(seq):
    yield int(seq + seq)


def _yield_repeated_unlimited(seq):
    repeated = seq
    while True:
        yield int(repeated := repeated + seq)


@register_solution(2025, 2, 1)
def part_one(input_file_path: str):
    return sum(
        invalid_id
        for range in read_file(input_file_path).split(",")
        for invalid_id in _yield_invalid_ids(range, _yield_repeated)
    )


@register_solution(2025, 2, 2)
def part_two(input_file_path: str):
    return sum(
        invalid_id
        for range in read_file(input_file_path).split(",")
        for invalid_id in set(_yield_invalid_ids(range, _yield_repeated_unlimited))
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 2)
    part_one(input_file_path)
    part_two(input_file_path)
