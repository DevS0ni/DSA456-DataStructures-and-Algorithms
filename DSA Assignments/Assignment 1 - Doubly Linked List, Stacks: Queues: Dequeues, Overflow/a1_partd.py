#    Main Author(s): Sarah Haque, Dev Soni
#    Main Reviewer(s): Dev Soni,Sarah Haque

# Since, we were just 2 people in the group we divided this part with 
# one function to each member thats why we have 2 names here of us, Sarah and Dev, for both- Main Author, Main Reviewer.

from a1_partc import Queue

def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_cells = []

    for row in range(rows):
        for col in range(cols):
            cell_value = abs(grid[row][col])
            neighbors = 0

            if row > 0:
                neighbors += 1
            if row < rows - 1:
                neighbors += 1
            if col > 0:
                neighbors += 1
            if col < cols - 1:
                neighbors += 1

            if cell_value >= neighbors:
                overflow_cells.append((row, col))

    if not overflow_cells:
        return None
    else:
        return overflow_cells

def overflow(grid, queue):
    def spread_overflow(row, col, is_negative):
        neighbors = [
            (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)
        ]

        for r, c in neighbors:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] < 0:
                    grid[r][c] -= 1
                else:
                    grid[r][c] += 1
        for r, c in neighbors:
            if is_negative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > 0:
                grid[r][c] *= -1
            if not is_negative and 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] < 0:
                grid[r][c] *= -1

    steps = 0
    while True:
        overflow_list = get_overflow_list(grid)
        if not overflow_list:
            break

        for r, c in overflow_list:
            is_negative = (grid[r][c] < 0)
            if (r, c - 1) not in overflow_list and (r - 1, c) not in overflow_list:
                grid[r][c] = 0
            if (r, c - 1) in overflow_list:
                if (r - 1, c) in overflow_list:
                    grid[r][c] = 2
                grid[r][c] = 1

            spread_overflow(r, c, is_negative)

        queue.enqueue([row[:] for row in grid])
        steps += 1

    return steps
