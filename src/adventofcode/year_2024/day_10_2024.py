from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _hike(scores: dict[complex, int], position: complex, next_score: int):
    for direction in (1, -1, 1j, -1j):
        if scores.get(position + direction, -1) == next_score:
            if next_score == 9:
                yield position + direction
            else:
                yield from _hike(scores, position + direction, next_score + 1)


def _get_scores_and_trailheads(input_file_path: str) -> tuple[dict, set]:
    scores = dict()
    trailheads = set()
    for i, line in enumerate(yield_lines(input_file_path)):
        for j, score in enumerate(line.strip()):
            score = int(score)
            scores[i + j * 1j] = score
            if score == 0:
                trailheads.add(i + j * 1j)
    
    return scores, trailheads


@register_solution(2024, 10, 1)
def part_one(input_file_path: str):
    scores, trailheads = _get_scores_and_trailheads(input_file_path)
    
    return sum(
        len(set(_hike(scores, trailhead, 1))) 
        for trailhead in trailheads
    )


@register_solution(2024, 10, 2)
def part_two(input_file_path: str):
    scores, trailheads = _get_scores_and_trailheads(input_file_path)
    
    return sum(
        len(list(_hike(scores, trailhead, 1)))
        for trailhead in trailheads
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 10)
    part_one(input_file_path)
    part_two(input_file_path)
