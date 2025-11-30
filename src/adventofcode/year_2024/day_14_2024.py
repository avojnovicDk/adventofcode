from functools import reduce
from time import sleep
from typing import Iterator
from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_file_path, yield_lines


def _points_to_complex(points: Iterator) -> complex:
    real, imag = points
    return real + imag * 1j


def _part_one(input_file_path: str, width: int = 101, height: int = 103) -> int:
    quadrants = [0, 0, 0, 0]
    for line in yield_lines(input_file_path):
        position, velocity = tuple(
            _points_to_complex(map(int, pv.split(",")))
            for pv in line.strip().replace("p=","").replace("v=","").split(" ")
        )

        position += velocity * 100
        if position.real < 0:
            position += (position.real // -width + 1) * width
        if position.imag < 0:
            position += (position.imag // -height + 1) * height * 1j
        position = (position.real % width) + (position.imag % height) * 1j
        
        if position.real <= width // 2 - 1:
            if position.imag <= height // 2 - 1:
                quadrants[0] += 1
            elif position.imag >= height // 2 + 1:
                quadrants[1] += 1
        elif position.real >= width // 2 + 1:
            if position.imag <= height // 2 - 1:
                quadrants[2] += 1
            elif position.imag >= height // 2 + 1:
                quadrants[3] += 1

    return reduce(lambda a, b: a * b, quadrants)


@register_solution(2024, 14, 1)
def part_one(input_file_path: str) -> int:
    return _part_one(input_file_path, 101, 103)


@register_solution(2024, 14, 2)
def part_two(input_file_path: str):
    width, height = 101, 103
    quadrants = [0, 0, 0, 0]
    robots = list()
    for line in yield_lines(input_file_path):
        position, velocity = tuple(
            _points_to_complex(map(int, pv.split(",")))
            for pv in line.strip().replace("p=","").replace("v=","").split(" ")
        )
        robots.append((position, velocity))
    
    seconds = 7709
    if seconds % 100 == 0:
        print(seconds)
    new_positions = set()
    for position, velocity in robots:
        position += velocity * seconds
        if position.real < 0:
            position += (position.real // -width + 1) * width
        if position.imag < 0:
            position += (position.imag // -height + 1) * height * 1j
        position = (position.real % width) + (position.imag % height) * 1j
    
        new_positions.add(position)
    
    for i in range(height):
    #     for j in range(height):
    #         is_candidate = True
    #         for k in range(5):
    #             if not((i + k + j * 1j) in new_positions and (i + j * 1j + k * 1j) in new_positions):
    #                 is_candidate = False
    #                 break
    #         if is_candidate:
    #             print("++++", seconds)
        print("".join("#" if (j + i * 1j) in new_positions else "." for j in range(width)))
        
        # sleep(0.5)

    return reduce(lambda a, b: a * b, quadrants)


if __name__ == '__main__':
    input_file_path = get_input_file_path(2024, 14)
    part_one(input_file_path)
    part_two(input_file_path)
