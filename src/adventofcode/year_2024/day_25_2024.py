from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


@register_solution(2024, 25, 1)
def part_one(input_file_path: str):
    is_lock = None
    locks, keys = [], []
    
    for line in yield_lines(input_file_path):
        if not line.strip():
            (locks if is_lock else keys).append(current)
            is_lock = None
        elif is_lock is None:
            is_lock = line[0] == "#"
            current = [0] * 5
        for i, p in enumerate(line):
            if p == "#":
                current[i] += 1
    (locks if is_lock else keys).append(current)
    
    return sum(
        1 if all(l <= k for l, k in zip(lock, key)) else 0
        for lock in locks
        for key in keys
    )


@register_solution(2024, 25, 2)
def part_two(input_file_path: str):
    raise SolutionNotFoundError(2024, 25, 2)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 25)
    part_one(input_file_path)
    part_two(input_file_path)
