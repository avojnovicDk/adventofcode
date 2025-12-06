import math
import re

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


@register_solution(2025, 6, 1)
def part_one(input_file_path: str):
    problems = list()
    total = 0
    for line in yield_lines(input_file_path):
        for i, number in enumerate(line.strip().split()):
            try:
                problems[i].append(int(number))
            except IndexError:
                problems.append([int(number)])
            except ValueError:
                total += (sum if number == '+' else math.prod)(problems[i])
    return total


@register_solution(2025, 6, 2)
def part_two(input_file_path: str):
    lines = [l.replace("\n", "") for l in yield_lines(input_file_path)]
    problems = [(m.start(), m.group()) for m in re.finditer(r'\+|\*', lines.pop(-1))]
    total = 0
    for a, b in zip(problems, problems[1:] + [None]):
        a, o = a
        b = b[0] if b else len(lines[0])+ 1
        numbers = map(lambda n: int("".join(n)), (zip(*(line[a:b-1] for line in lines))))
        total += (sum if o == '+' else math.prod)(numbers)
    return total


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 6)
    part_one(input_file_path)
    part_two(input_file_path)
