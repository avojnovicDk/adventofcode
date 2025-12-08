from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path
from adventofcode.util.input_helpers import yield_lines


@register_solution(2025, 7, 1)
def part_one(input_file_path: str):
    splitters = set()
    for row, line in enumerate(yield_lines(input_file_path)):
        for col, char in enumerate(line.strip()):
            if char == '^':
                splitters.add((row, col))
            elif char == 'S':
                start = (row, col)

    def calc_splitters_hit(pos, row, col, visited):
        if pos in visited:
            return 0
        visited.add(pos)

        x, y = pos
        while True:
            x += 1
            if (x, y) in visited or x >= row or y < 0 or y >= col:
                return 0
            elif (x, y) in splitters:
                return (
                    1
                    + calc_splitters_hit((x, y - 1), row, col, visited)
                    + calc_splitters_hit((x, y + 1), row, col, visited)
                )
            else:
                visited.add((x, y))

    return calc_splitters_hit(start, row, col, set())


@register_solution(2025, 7, 2)
def part_two(input_file_path: str):
    splitters = set()
    row, col = 0, 0
    start = (0,0) # (row, col)
    for line in yield_lines(input_file_path):
        if (col_ := line.find("S")) != -1:
            start = (row, col_)
        else:
            for col_, char in enumerate(line):
                if char == "^":
                    splitters.add((row, col_))
        row += 1
    col = len(line.strip())

    visited = {}
    def calc_splitters_hit(start: tuple):
        if start in visited:
            return visited[start]
        pos = start
        while True:
            new_pos = (pos[0]+1, pos[1])
            if new_pos in visited:
                return visited[new_pos]
            if new_pos[0] == row-1:
                visited[start] = 1
                return 1
            if new_pos[0] > row-1 or new_pos[1] < 0 or new_pos[1] > col-1:
                return 0
            elif new_pos in splitters:
                s = 0
                s += calc_splitters_hit((new_pos[0], new_pos[1]-1))
                s += calc_splitters_hit((new_pos[0], new_pos[1]+1))
                visited[start] = s
                return s
            else:
                pos = new_pos


    return calc_splitters_hit(start)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2025, 7)
    part_one(input_file_path)
    part_two(input_file_path)
