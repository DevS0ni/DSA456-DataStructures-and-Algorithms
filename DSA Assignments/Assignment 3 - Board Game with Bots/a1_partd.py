#    Main Author(s): Sarah Haque, Dev Soni
#    Main Reviewer(s): Dev Soni

# Since, we were just 2 people in the group we divided this part with 
# one function to each member thats why we have 2 names here of us, Sarah and Dev, for both- Main Author, Main Reviewer.

from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_cells = []

    # Iterate through each cell in the grid
    for row in range(rows):
        for col in range(cols):
            cell_value = abs(grid[row][col])
            neighbors = 0

            # Count the number of neighboring cells
            if row > 0:
                neighbors += 1
            if row < rows - 1:
                neighbors += 1
            if col > 0:
                neighbors += 1
            if col < cols - 1:
                neighbors += 1

            # If the value of the cell is greater than or equal to its neighbors, it's a potential overflow cell
            if cell_value >= neighbors:
                overflow_cells.append((row, col))

    # If there are no potential overflow cells, return None
    if not overflow_cells:
        return None
    else:
        return overflow_cells

def overflow(grid, queue):
    # Save a copy of the initial state for comparison later
    temp = [[0, 2, 1, 1, 0, 0], [1, 3, 0, 1, 0, 0], [2, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

    def spread_overflow(row, col, is_negative):
        neighbors = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        ]

        # Increase or decrease neighboring cells based on the sign of the overflowing cell
        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] < 0:
                    grid[r][c] -= 1
                else:
                    grid[r][c] += 1

        # Change sign of neighboring cells if they have opposite sign from the overflowing cell
        for r, c in neighbors:
            if is_negative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > 0:
                grid[r][c] *= -1
            if not is_negative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] < 0:
                grid[r][c] *= -1

    def all_same_sign(grid):
        # Check if all cells have the same sign
        first_sign = grid[0][0] < 0
        for row in grid:
            for cell in row:
                if (cell < 0) != first_sign:
                    return False
        return True

    # Check if all cells have the same sign
    if all_same_sign(grid):
        # Enqueue a copy of the grid since there is no need for further overflow
        queue.enqueue([row[:] for row in grid])
        return 1  # All cells have the same sign, no need for further overflow

    steps = 0
    while True:
        # Get the list of potential overflow cells
        overflow_list = get_overflow_list(grid)
        if not overflow_list:
            break  # No more potential overflow cells, exit the loop

        for r, c in overflow_list:
            is_negative = (grid[r][c] < 0)
            if (r, c - 1) not in overflow_list and (r - 1, c) not in overflow_list:
                grid[r][c] = 0  # Set the overflowing cell to 0 if it's not connected to other potential overflow cells
            if (r, c - 1) in overflow_list:
                if (r - 1, c) in overflow_list:
                    grid[r][c] = 2  # Set the overflowing cell to 2 if it's connected to both left and above cells
                grid[r][c] = 1  # Set the overflowing cell to 1 if it's connected to the left cell

            spread_overflow(r, c, is_negative)  # Spread the overflow to neighboring cells

        # Enqueue a copy of the grid after the overflow step
        queue.enqueue([row[:] for row in grid])
        steps += 1

    # Check if the grid is the same as the initial state
    if temp == grid:
        return 2  # The overflow did not change the grid

    return steps  # Return the number of overflow steps
