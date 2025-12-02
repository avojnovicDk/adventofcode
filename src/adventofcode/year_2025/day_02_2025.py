from itertools import count, takewhile

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


def _yield_invalid_ids(range, are_reps_limited):
    start, end = map(int, range.split("-"))
    is_possible_seq = lambda seq: int(seq + seq) <= end
    for seq in takewhile(is_possible_seq, map(str, count(1))):
        no_of_reps = 2
        candidate = int(seq * no_of_reps)
        if are_reps_limited and candidate < start:
            continue

        while candidate < start:
            no_of_reps += 1
            candidate = int(seq * no_of_reps)

        if candidate <= end:
            yield candidate


@register_solution(2025, 2, 1)
def part_one(input_file_path: str):
    return sum(
        invalid_id
        for range in read_file(input_file_path).split(",")
        for invalid_id in _yield_invalid_ids(range, True)
    )


@register_solution(2025, 2, 2)
def part_two(input_file_path: str):
    return sum(
        invalid_id
        for range in read_file(input_file_path).split(",")
        for invalid_id in set(_yield_invalid_ids(range, False))
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 2)
    part_one(input_file_path)
    part_two(input_file_path)
