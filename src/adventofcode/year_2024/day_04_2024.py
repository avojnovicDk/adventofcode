from adventofcode.registry.decorators import register_solution
from adventofcode.util.input_helpers import get_input_file_path, get_input
from adventofcode.util.string_matrix import StringMatrix


@register_solution(2024, 4, 1)
def part_one(input_file_path: str) -> int:
    frame = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    )

    count = lambda lines, x, y: sum(
        1
        for dir_x, dir_y in frame
        if (lines.get_char_in_dir(x, y, dir_x, dir_y, 3) == "S"
            and lines.get_char_in_dir(x, y, dir_x, dir_y, 2) == "A"
            and lines.get_char_in_dir(x, y, dir_x, dir_y) == "M"
        )
    )
    
    return StringMatrix(get_input(input_file_path)).count_from_starting("X", count)


@register_solution(2024, 4, 2)
def part_two(input_file_path: str) -> int:
    crosses = (
        ((-1, -1), (1,  1),),
        ((-1,  1), (1, -1),),
    )

    count = lambda lines, x, y: 1 if all(
        set(lines.get_char_in_dir(x, y, dir_x, dir_y) for dir_x, dir_y in cross) == {"M", "S"}
        for cross in crosses
    ) else 0
    
    return StringMatrix(get_input(input_file_path)).count_from_starting("A", count)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 4)
    part_one(input_file_path)
    part_two(input_file_path)
