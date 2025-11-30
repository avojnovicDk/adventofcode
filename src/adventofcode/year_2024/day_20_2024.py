from collections import Counter

from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _get_path(start, end, track):
    path = [start]
    while path[-1] != end:
        for direction in (1, -1, 1j, -1j):
            curr = start + direction
            if curr in track and curr not in path:
                break
        path.append(curr)
        start = curr
    return path


@register_solution(2024, 20, 1)
def part_one(input_file_path: str):
    track = set()
    start, end = None, None
    for i, line in enumerate(yield_lines(input_file_path)):
        for j, el in enumerate(line):
            if el == "#":
                continue
            p = i + j * 1j
            track.add(p)
            if el == "S":
                start = p
            elif el == "E":
                end = p

    path = _get_path(start, end, track)
    
    return sum(
        1
        for i, p in enumerate(path[:-1])
        for direction in {1, -1, 1j, -1j} - {path[i + 1] - p}
        if p + direction * 2 in path and (path.index(p + direction * 2) - path.index(p) - 2) >= 100
    )

COUNTER = 0
def _yield_cheats(position, track, walls, visited):
    if len(visited) == 20:
        return
        
    for direction in (-1, 1, -1j, 1j):
        current = position + direction
        if current in track:
            yield current, len(visited) + 1
        if current in walls and current not in visited:
            curr_visited = visited.copy()
            curr_visited.append(current)
            yield from _yield_cheats(current, track, walls, curr_visited)


@register_solution(2024, 20, 2)
def part_two(input_file_path: str):
    track = set()
    walls = set()
    start, end = None, None
    for i, line in enumerate(yield_lines(input_file_path)):
        for j, el in enumerate(line):
            p = i + j * 1j
            match el:
                case "#":
                    walls.add(p)
                case ".":
                    track.add(p)
                case "S":
                    track.add(p)
                    start = p
                case "E":
                    track.add(p)
                    end = p
                    
    path = _get_path(start, end, track)

    counter = list()

    cheats = dict()
    for p in path:
        for c_start in {p + 1, p - 1, p + 1j, p - 1j} & walls:
            for c_end, c_len in _yield_cheats(c_start, track, walls, list()):
                saved_len = path.index(c_end) - path.index(p) - c_len - 1
                if saved_len < 50:
                    continue
                if (c_start, c_end) not in cheats or cheats[(c_start, c_end)] < saved_len:
                    # if c_start == 4 + 1j and c_end == 7 + 3j:
                        # print(c_start, c_end, path.index(c_end), path.index(p), c_len)
                    cheats[(c_start, c_end)] = saved_len
    for k, v in cheats.items():
        if v == 76:
            print(k[0], k[1])

    from pprint import pprint
    pprint(Counter(cheats.values()))

        # for c, l in (set((c, l) for c, l in if {c + 1, c - 1, c + 1j, c - 1j} & track)):
        #     if c == 6 + 5j:
        #         print(p, c, l)
        #     counter.append((c, max(path.index(c + d) for d in {1, -1, 1j, -1j} if c + d in path) - l))
    
    # counter = Counter(c for c in counter if c[1] > 50)
    # from pprint import pprint
    # pprint([c for c in counter if c[1] >= 76])
    
    return 3
    
    return sum(
        1
        for i, p in enumerate(path[:-1])
        for direction in {1, -1, 1j, -1j} - {path[i + 1] - p}
        if p + direction * 2 in path and (path.index(p + direction * 2) - path.index(p) - 2) >= 100
    )


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 20)
    part_one(input_file_path)
    part_two(input_file_path)
