import math
from collections import namedtuple
from itertools import combinations

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


BoxPair = namedtuple("BoxPair", ["box1", "box2", "distance"])


def _get_distance(box1, box2):
    return sum((box1[d] - box2[d]) ** 2 for d in range(3))


def _connect_next_closest_pair(boxes):
    pairs = {BoxPair(p1, p2, _get_distance(p1, p2)) for p1, p2 in combinations(boxes, 2)}
    circuits = list()
    for next_pair in sorted(pairs, key=lambda p: p.distance):
        next_pair = {next_pair.box1, next_pair.box2}
        matching_circuits = [c for c in circuits if next_pair & c]
        if not matching_circuits:
            circuits.append(next_pair)
        elif len(matching_circuits) == 1:
            matching_circuits[0] |= next_pair
        elif len(matching_circuits) == 2:
            matching_circuits[0] |= matching_circuits[1]
            matching_circuits[1].clear()

        yield circuits, next_pair


def part_one_with_iterations(input_file_path, no_of_iterations=1000):
    boxes = {tuple(map(int, box.split(','))) for box in yield_lines(input_file_path)}

    connector = _connect_next_closest_pair(boxes)
    for _ in range(no_of_iterations):
        circuits, _ = next(connector)

    return math.prod(sorted(map(len, circuits), reverse=True)[:3])


@register_solution(2025, 8, 1)
def part_one(input_file_path):
    return part_one_with_iterations(input_file_path, 1000)


@register_solution(2025, 8, 2)
def part_two(input_file_path: str):
    boxes = {tuple(map(int, box.split(','))) for box in yield_lines(input_file_path)}

    connector = _connect_next_closest_pair(boxes)
    for circuits, next_pair in connector:
        if len(next(c for c in circuits if c)) == len(boxes):
            return next_pair.pop()[0] * next_pair.pop()[0]


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 8)
    part_one(input_file_path)
    part_two(input_file_path)
