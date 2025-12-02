import math

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, read_file


def _yield_candidates(range: str):
    start, end = range.split("-")
    half_start = int(start[:math.floor(len(start)/2)] or 0)
    candidate = int(f"{half_start}{half_start}")
    while candidate < int(start):
        half_start += 1
        candidate = int(f"{half_start}{half_start}")

    while candidate <= int(end):
        yield candidate
        half_start += 1
        candidate = int(f"{half_start}{half_start}")


@register_solution(2025, 2, 1)
def part_one(input_file_path: str):
    return sum(
        candidate
        for range in read_file(input_file_path).split(",")
        for candidate in _yield_candidates(range)
    )


def _yield_candidates_2(range: str):
    start, end = range.split("-")
    seq = 1
    while int(f"{seq}{seq}") <= int(end):
        min_rep = max(math.floor(len(start)/len(str(seq))), 2)
        start_seq = str(seq) * min_rep
        if int(start_seq) < int(start):
            start_seq += str(seq)
        while int(start_seq) <= int(end):
            yield start_seq
            start_seq += str(seq)
        seq += 1


@register_solution(2025, 2, 2)
def part_two(input_file_path: str):
    result = 0
    for range in read_file(input_file_path).split(","):
        candidates = set(_yield_candidates_2(range))
        result += sum(map(int, candidates))
    return result


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 2)
    part_one(input_file_path)
    part_two(input_file_path)
