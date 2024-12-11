import sys
from adventofcode import config
from adventofcode.registry import autodetect, registry
from adventofcode.registry.util import get_info_from_registry_key
from adventofcode.scripts.add_day import _parse_args
from adventofcode.util.input_helpers import get_input_file_path


def run_all() -> None:
    """
    Gathers all year_*.day_* files and executes the
    part_one and part_two functions in those files.

    If input file is not found, or a function is not found, it will be printed to console
    """
    config.RUNNING_ALL = True
    autodetect()

    for key, solution in registry.items():
        year, day, part, version = get_info_from_registry_key(key)
        data = get_input_file_path(year, day)

        solution(data)

    config.RUNNING_ALL = False


def run_day():
    """
    Runs all solutions in the given day
    """
    config.RUNNING_ALL = True
    input_year, input_day = _parse_args(sys.argv[1:])
    
    autodetect()
    
    data = get_input_file_path(input_year, input_day)
    for key, solution in registry.items():
        year, day, part, version = get_info_from_registry_key(key)
        if year == input_year and day == input_day:
            solution(data)
    config.RUNNING_ALL = False
