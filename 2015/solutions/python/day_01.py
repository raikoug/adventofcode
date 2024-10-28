from starter import AOC, CURRENT_YEAR
from pathlib import Path

CURRENT_DAY = int(Path(__file__).stem.replace('day_',''))
aoc = AOC(CURRENT_YEAR)

def solve_1(test_string = None) -> int:
    inputs_1 = aoc.get_input(CURRENT_DAY, 1) if not test_string else test_string
    up      = inputs_1.count('(')
    down    = inputs_1.count(')')
    result = up - down
    return result
    
    


if __name__ == "__main__":
    print(solve_1())