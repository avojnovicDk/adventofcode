from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _is_fresh(ranges, ingredient):
    for start, end in ranges:
        if start > ingredient:
            return False
        if end >= ingredient:
            return True
    return False


@register_solution(2025, 5, 1)
def part_one(input_file_path: str):
    line_yielder = yield_lines(input_file_path)
    ranges = []
    while line := next(line_yielder).strip():
        ranges.append(tuple(map(int, line.split("-"))))
    ranges.sort()

    return sum(_is_fresh(ranges, int(line)) for line in line_yielder)


def _merge_ranges(ranges_to_merge, merged_ranges):
    while ranges_to_merge:
        start, end = ranges_to_merge.pop()
        new_overlapping_ranges = {
            (curr_start, curr_end)
            for curr_start, curr_end in merged_ranges
            if curr_start <= end and curr_end >= start}
        if new_overlapping_ranges:
            merged_ranges -= new_overlapping_ranges
            ranges_to_merge |= {
                (min(start, curr_start), max(end, curr_end))
                for curr_start, curr_end in new_overlapping_ranges
            }
        else:
            merged_ranges.add((start, end))
    return merged_ranges


@register_solution(2025, 5, 2)
def part_two(input_file_path: str):
    line_yielder = yield_lines(input_file_path)
    ranges = set()
    while line := next(line_yielder).strip():
        _merge_ranges({tuple(map(int, line.split("-")))}, ranges)
    return sum(end - start + 1 for start, end in ranges)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 5)
    part_one(input_file_path)
    part_two(input_file_path)
