from copy import deepcopy
from typing import Optional
from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


MOVE_TO_DIRECTION = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}


def _find_empty_spot(map: list[list[str]], pos_x: int, pos_y: int, dir_x: int, dir_y: int) -> Optional[tuple[int, int]]:
    while map[pos_x][pos_y] != "#":
        pos_x += dir_x
        pos_y += dir_y
        if map[pos_x][pos_y] == ".":
            return pos_x, pos_y


def _move(map: list[list[str]], pos_x: int, pos_y: int, move: str) -> tuple[int, int]:
    dir_x, dir_y = MOVE_TO_DIRECTION[move]

    match map[pos_x + dir_x][pos_y + dir_y]:
        case ".":
            return pos_x + dir_x, pos_y + dir_y
        case "#":
            return pos_x, pos_y
        case "O":
            empty_spot = _find_empty_spot(map, pos_x, pos_y, dir_x, dir_y)
            if not empty_spot:
                return pos_x, pos_y
            map[empty_spot[0]][empty_spot[1]] = "O"
            map[pos_x + dir_x][pos_y + dir_y] = "."
            return pos_x + dir_x, pos_y + dir_y


@register_solution(2024, 15, 1)
def part_one(input_file_path: str) -> int:
    line_yielder = yield_lines(input_file_path)
    map = list()
    pos_x, pos_y = -1, -1
    i = 0
    line = next(line_yielder)
    while line.strip():
        if "@" in line:
            pos_x, pos_y = (i, line.index("@"))
            line = line.replace("@", ".")
        i += 1
        map.append(list(line.strip()))
        line = next(line_yielder)

    for line in line_yielder:
        for move in line.strip():
            pos_x, pos_y = _move(map, pos_x, pos_y, move)

    return sum (
        i * 100 + j if c == "O" else 0
        for i, line in enumerate(map)
        for j, c in enumerate(line)
    )


def _move_pt2(map: list[list[str]], pos_x: int, pos_y: int, move: str) -> tuple[int, int]:
    dir_x, dir_y = MOVE_TO_DIRECTION[move]

    match map[pos_x + dir_x][pos_y + dir_y]:
        case ".":
            return pos_x + dir_x, pos_y + dir_y
        case "#":
            return pos_x, pos_y
        case "]" | "[":
            empty_spot = _find_empty_spot(map, pos_x, pos_y, dir_x, dir_y)
            if not empty_spot:
                return pos_x, pos_y
            
            if dir_x == 0:
                left = True
                start, end = tuple(sorted([pos_y + dir_y * 2, empty_spot[1]]))
                for y in range(start, end + 1):
                    map[pos_x][y] = "[" if left else "]"
                    left = not left
                map[pos_x][pos_y + dir_y] = "."
                return pos_x + dir_x, pos_y + dir_y

            new_map = deepcopy(map)
            curr_x = pos_x + dir_x
            if new_map[curr_x][pos_y] == "]":
                start, end = pos_y - 1, pos_y
            else:
                start, end = pos_y, pos_y + 1
            new_map[curr_x][start] = new_map[curr_x][end] = "."
            while start is not None:
                curr_x += dir_x
                if "#" in new_map[curr_x][start: end + 1]:
                    return pos_x, pos_y
                all_to_copy = [i for i in range(start, end + 1) if new_map[curr_x][i] in ("[", "]")]
                new_copy_start, new_copy_end = None, None
                if all_to_copy:
                    new_copy_start, new_copy_end = min(all_to_copy), max(all_to_copy)
                    if new_map[curr_x][new_copy_start] == "]":
                        new_copy_start -= 1
                        new_map[curr_x][new_copy_start] = "."
                    if new_map[curr_x][new_copy_end] == "[":
                        new_copy_end += 1
                        new_map[curr_x][new_copy_end] = "."
                    
                new_map[curr_x][start: end + 1] = map[curr_x - dir_x][start: end + 1]
                start, end = new_copy_start, new_copy_end
            # print("///")
            for i, line in enumerate(map):
                # print("".join(new_map[i]))
                map[i] = new_map[i]
            return pos_x + dir_x, pos_y + dir_y
            
    

@register_solution(2024, 15, 2)
def part_two(input_file_path: str) -> int:
    line_yielder = yield_lines(input_file_path)
    map = list()
    pos_x, pos_y = -1, -1
    i = 0
    line = next(line_yielder)
    while line.strip():
        if "@" in line:
            pos_x, pos_y = (i, line.index("@") * 2)
            line = line.replace("@", ".")
        i += 1
        map.append([o if el == "O" else el for el in line.strip() for o in ("[", "]")])
        line = next(line_yielder)

    for line in line_yielder:
        for move in line.strip():
            pos_x, pos_y = _move_pt2(map, pos_x, pos_y, move)

    return sum (
        i * 100 + j if c == "[" else 0
        for i, line in enumerate(map)
        for j, c in enumerate(line)
    )
            



if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 15)
    part_one(input_file_path)
    part_two(input_file_path)
