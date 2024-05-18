import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,0,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

solutions = set()

def possible(row, column, number):
    global grid
    # Number in row?
    for i in range(0, 9):
        if grid[row][i] == number:
            return False

    # Number in column?
    for i in range(0, 9):
        if grid[i][column] == number:
            return False
    
    # Number in 3x3 square?
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False

    return True

def solve():
    global grid, solutions
    for row in range(0, 9):
        for column in range(0, 9):
            if grid[row][column] == 0:
                for number in range(1, 10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return

    # Convert the grid to a tuple of tuples so it can be added to a set
    grid_tuple = tuple(tuple(row) for row in grid)
    solutions.add(grid_tuple)

# Find all solutions
solve()

# Output the number of solutions found
num_solutions = len(solutions)
print(f"Number of solutions: {num_solutions}")

if num_solutions > 0:
    for solution in solutions:
        print(np.matrix(solution))
        input('Hit Enter for more solutions: ')
else:
    print("All solutions are provided to you")