# Main Author: Sarah Haque
# Main Reviewer: Dev Soni

WINNING_SCORE = 1000  # A high value to represent a winning state
LOSING_SCORE = -1000  # A low value to represent a losing state

def evaluate_board(board, player):
    # First, check for winning or losing states
    all_positive = all(cell >= 0 for row in board for cell in row)
    all_negative = all(cell <= 0 for row in board for cell in row)

    if player == 1:
        if all_positive:  # Winning state for player 1
            return WINNING_SCORE
        elif all_negative:  # Losing state for player 1
            return LOSING_SCORE
    else:  # player == -1
        if all_negative:  # Winning state for player 2
            return WINNING_SCORE
        elif all_positive:  # Losing state for player 2
            return LOSING_SCORE

    # If not a winning or losing state, calculate score based on pieces
    score = 0
    for row in board:
        for cell in row:
            if cell * player > 0:
                # This cell belongs to the player
                score += abs(cell)
            elif cell * player < 0:
                # This cell belongs to the opponent
                score -= abs(cell)

    return score
