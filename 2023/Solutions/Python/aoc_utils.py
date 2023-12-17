from pathlib import Path
from icecream import ic

BASE = Path(f"C:/Users/raikoug/SyncThing/shared_code_tests/adventOfCode/2023/")
def get_day_input(day: int, test: bool = False) -> list:
    """
    Returns the input as list of rows for the given day.
    input will be in the day folder (day_XX) and filename are
        input.txt
        test_input.txt
    """
    file_name = f"{"test_" if test else ""}input.txt"
    file_path = BASE / f"day_{day:02}" / file_name
    #ic(file_path)
    return file_path.read_text().split("\n")

def get_file_path(day: int, test: bool = False):
    """
    Just returns the full path of the file
    """
    file_name = f"{"test_" if test else ""}input.txt"
    file_path = BASE / f"day_{day:02}" / file_name
    return file_path