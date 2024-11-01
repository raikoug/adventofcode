from starter import AOC, CURRENT_YEAR
from pathlib import Path

CURRENT_DAY = int(Path(__file__).stem.replace('day_',''))
aoc = AOC(CURRENT_YEAR)

def solve_1(test_string = None, test=False) -> int:
    inputs_1 = aoc.get_input(CURRENT_DAY, 1) if not test_string else test_string
    if test: inputs_1 = aoc.get_input(CURRENT_DAY, 9)
    return 1
    
def solve_2(test_string = None) -> int:
    inputs_1 = aoc.get_input(CURRENT_DAY, 1) if not test_string else test_string
    return 1


if __name__ == "__main__":
    print(solve_1(test=True))