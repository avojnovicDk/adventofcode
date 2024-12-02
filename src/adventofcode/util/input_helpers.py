import os
import warnings
from typing import Generator

from adventofcode.config import ROOT_DIR


def get_input_file_path(year: int, day: int) -> str:
    """
    Get the input file path for the year/day.
    """
    return os.path.join(ROOT_DIR, "inputs", str(year), f"day_{day:02}.txt")


def get_input_for_day(year: int, day: int) -> list[str]:
    """
    Get the input for the year/day as list of strings
    """
    return _get_input(get_input_file_path(year, day))


def get_input_for_day_as_str(year: int, day: int) -> str:
    warnings.warn(
        "get_input_for_day_as_str does not work with the registry, better to not use it",
        stacklevel=2,
    )
    return _read_file(get_input_file_path(year, day))


def yield_lines(file_path: str) -> Generator[str, None, None]:
    with open(file_path, 'r') as f:
        yield from f


def _read_lines(file_name) -> list[str]:
    """
    Reads file to list of string
    """
    with open(file_name) as file:
        lines = file.readlines()

    return lines


def _get_input(file_name) -> list[str]:
    """
    Strips new lines from input file and returns it as list of string
    """
    lines = _read_lines(file_name)
    return [line.rstrip() for line in lines]


def _read_file(file_name) -> str:
    """
    Reads file to string
    """
    with open(file_name) as file:
        content = file.read()

    content = content.rstrip("\n")
    return content
