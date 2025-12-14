from collections import defaultdict, namedtuple
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


@register_solution(2025, 9, 1)
def part_one(input_file_path: str):
    rectangles = {tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)}
    return max((abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1) for a, b in combinations(rectangles, 2))


def _check_is_inside(point, allowed_per_row):
    x, row = point
    allowed = sorted(allowed_per_row[row], key=lambda p: p[0] if isinstance(p, tuple) else p)
    while allowed:
        nxt = allowed.pop(0)
        if (nxt[1] if isinstance(nxt, tuple) else nxt) >= x:
            break

    if (nxt[1] if isinstance(nxt, tuple) else nxt) < x:
        return False

    if isinstance(nxt, tuple):
        if nxt[0] <= x <= nxt[1]:
            return True
    elif nxt == x:
        return True
    
    allowed.append(nxt)
    counter = 0
    for a in allowed:
        if isinstance(a, tuple):
            counter += len(set(a) - allowed_per_row[row + 1])
        else:
            counter += 1

    return counter % 2 == 1


def _check_sides(a, b, row_sides, col_sides):
    horizontals = (min(a[0], b[0]) + 1, max(a[0], b[0]))
    verticals = (min(a[1], b[1]) + 1, max(a[1], b[1]))

    for col in range(*horizontals):
        for side in sorted(col_sides[col]):
            if side[0] < a[1] < side[1]:
                return False
            if side[0] < b[1] < side[1]:
                return False
    for row in range(*verticals):
        for side in sorted(row_sides[row]):
            if side[0] < a[0] < side[1]:
                return False
            if side[0] < b[0] < side[1]:
                return False
    return True


@register_solution(2025, 9, 2)
def part_two(input_file_path: str):
    rectangles = [tuple(map(int, r.split(','))) for r in yield_lines(input_file_path)]
    allowed_per_row = defaultdict(set)
    row_sides, col_sides = defaultdict(set), defaultdict(set)
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        if a[0] == b[0]:
            for row in range(min(a[1], b[1]) + 1, max(a[1], b[1])):
                allowed_per_row[row].add(a[0])
            col_sides[a[0]].add((min(a[1], b[1]), max(a[1], b[1])))
        else:
            allowed_per_row[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))
            row_sides[a[1]].add((min(a[0], b[0]), max(a[0], b[0])))

    max_area = 0
    for a, b in combinations(rectangles, 2):
        if (
            not (a[0] == b[0] or a[1] == b[1])
            and _check_is_inside((a[0], b[1]), allowed_per_row)
            and _check_is_inside((b[0], a[1]), allowed_per_row)
            and _check_sides(a, b, row_sides, col_sides)
        ):
            area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
            if area > max_area:
                max_area = area

    segments = []
    for a, b in zip(rectangles, rectangles[1:] + [rectangles[0]]):
        segments.append((a[0] // 100, a[1] // 100, b[0] // 100, b[1] // 100))
    
    return max_area


if __name__ == "__main__":
    input_file_path = get_input_file_path(2025, 9)
    part_one(input_file_path)
    part_two(input_file_path)
