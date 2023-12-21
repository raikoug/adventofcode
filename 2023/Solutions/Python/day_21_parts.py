from collections import deque
from icecream import ic
import heapq

D = {
    "n": (-1, 0),
    "s": (1, 0),
    "e": (0, 1),
    "w": (0, -1),
}

class Tyle:
    type: str
    row: int
    col: int
    neighbors: dict
    feasible_neighbors: list
    best_steps: int
    hashing: int   #have to add an hasing unique for set XD
    is_visited: bool

    def __init__(self, type, row, col, hashing):
        self.type = type
        self.row = row
        self.col = col
        self.neighbors = dict()
        self.best_steps = 1e9
        self.feasible_neighbors = list()
        self.hashing = hashing
        self.is_visited = False

    def add_neighbor(self, direction, neighbor):
        self.neighbors[direction] = neighbor

    def __hash__(self):  # here is the set magic... -.-'
        return self.hashing

    def __lt__(self, other):
        return self.best_steps < other.best_steps
    
    def __gt__(self, other):
        return self.best_steps > other.best_steps
    
    def __eq__(self, other):
        return self.best_steps == other.best_steps
    
    def __le__(self, other):
        return self.best_steps <= other.best_steps
    
    def __ge__(self, other):
        return self.best_steps >= other.best_steps
    
    def __ne__(self, other):
        return self.best_steps != other.best_steps
    

    def is_rock(self):
        return self.type == '#'
    
    def is_garden_plot(self):
        return self.type in ['.', 'S']

    def __str__(self):
        return self.type
    
    def __repr__(self):
        return self.__str__()
    
    def pretty_print(self):
        """
        printed in the form
         ----   N.type    ----
        W.type,self.type,E.type
         ----   S.type    ----
        """
        res =  f" {self.neighbors['n'].type if 'n' in self.neighbors else ""} \n"
        res += f"{self.neighbors['w'].type if 'w' in self.neighbors else " "}{self.type}{self.neighbors['e'].type if 'e' in self.neighbors else " "}\n"
        res += f" {self.neighbors['s'].type if 's' in self.neighbors else " "} \n"
        print(res)

class Grid:
    f: list
    end_tyles: set
    visited: set

    def __init__(self, tf):
        self.f, start = init_grid(tf)
        self.start = self.f[start[0]][start[1]]
        self.end_tyles = set()
        self.visited = set()

    def __str__(self):
        res = ""
        for row in self.f:
            for col in row:
                res += str(col)
            res += "\n"
        return res

    def __repr__(self):
        return self.__str__()

    def print_with_end_tyles(self):
        for row in self.f:
            for col in row:
                if col in self.end_tyles:
                    print("O", end="")
                else:
                    print(col, end="")
            print()

    def add_visited(self, tyle)-> bool:
        """
        return True if tyle has not been visited and add it to list
            else return False, and the code should continue to next step
        """
        self.visited.add(tyle)

def init_grid(tf):
    grid = list()
    i = 0
    for ri,row in enumerate(tf):
        tmp_row = list()
        for ci,col in enumerate(row):
            tmp_tyle = Tyle(col, ri, ci, i)
            i += 1
            tmp_row.append(tmp_tyle)
            if col == "S":
                start = [ri,ci]
        grid.append(tmp_row)
    
    grid = calc_neighbors(grid)

    return grid, start

def calc_neighbors(grid):
    for ri,row in enumerate(grid):
        for ci,col in enumerate(row):
            for r,d in D.items():
                n_row = ri + d[0]
                n_col = ci + d[1]
                if n_row < 0 or n_col < 0:
                    continue
                try:
                    neighbor = grid[n_row][n_col]
                    col.add_neighbor(r, neighbor)
                    if neighbor.is_garden_plot():
                        col.feasible_neighbors.append(neighbor)
                except IndexError:
                    pass
        
    return grid

def part_1(grid: Grid, max_steps: int)-> int:
    Q = [[0, grid.start]]
    total = 0
    while Q:
        step, tyle = heapq.heappop(Q)

        if step > max_steps:
            # I use heapq, then if here the step is > to max_steps
            #   i know all the others do
            break

        if tyle.is_visited:
            continue

        if step%2 == 0:
            total += 1

        tyle.is_visited = True

        for t in tyle.feasible_neighbors:
            heapq.heappush(Q, [step+1, t])
    
    #grid.print_with_end_tyles()
    return total
    

if __name__ == "__main__":
    import aoc_utils
    from pathlib import Path

    day = int(Path(__file__).name.split('_')[1])
    test = False
    tf = aoc_utils.get_day_input(day, test)
    steps_to_take = 6 if test else 64
    grid = Grid(tf)
    part_1_res = part_1(grid, steps_to_take)
    
    ic(part_1_res)

    
    
    
    
    
    
    
    
    
    
    
    
    
        

    