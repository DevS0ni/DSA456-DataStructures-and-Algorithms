# Main Author: Sarah Haque, Dev Soni
# Main Reviewer: Dev Soni

# Import necessary functions
from a3_parta import evaluate_board
from a1_partd import overflow
from a1_partc import Queue

# Copy Board Function
# This function duplicates a given board and returns the duplicate
def copy_board(board):
    return [row[:] for row in board]

# Get Possible Moves Function
# Determines and returns a list of all possible moves for a given player on the given board
def get_possible_moves(board, player):
    moves = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                moves.append((row, col))
    return moves

# Make Move Function
# Applies a given move for a player on the board and triggers the overflow process
def make_move(board, move, player):
    new_board = copy_board(board)
    new_board[move[0]][move[1]] = player
    overflow(new_board, Queue())  # Call overflow with the updated board
    return new_board

# GameTree Class
# Represents the game tree for evaluating the best moves in a board game
class GameTree:
    # Node Class
    # Represents a node in the game tree, containing the game state at a certain move
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.score = 0

        # Has Won Function
        # Checks if the given player has won in the current board state
        def has_won(self, player):
             # Check rows
            for row in self.board:
                if all(cell == player for cell in row):
                    return True

        # Evaluate Function
        # Evaluates and assigns a score to the node based on the game state
        def evaluate(self):
            if self.depth == self.tree_height - 1 or self.has_won(self.player):
                self.score = evaluate_board(self.board, self.player)
            else:
                for move in get_possible_moves(self.board, self.player):
                    new_board = make_move(self.board, move, self.player)
                    child = GameTree.Node(new_board, self.depth + 1, -self.player, self.tree_height)
                    child.evaluate()
                    self.children.append((move, child))
                if self.depth % 2 == 0:
                    self.score = max(child[1].score for child in self.children)
                else:
                    self.score = min(child[1].score for child in self.children)

    # Constructor for GameTree
    # Initializes the game tree with the root node
    def __init__(self, board, player, tree_height=4):
        self.root = self.Node(board, 0, player, tree_height)
    
    # Get Move Function
    # Determines and returns the best move based on the current game state
    def get_move(self):
        self.root.evaluate()

        # For the first move, simply return the middle position
        if self.root.depth == 0 and not self.root.children:
            return len(self.root.board) // 2, len(self.root.board[0]) // 2

        # Choose the best move based on the score
        best_move = max(self.root.children, key=lambda x: x[1].score)

        # Avoid obvious losing moves
        if self.root.depth % 2 == 0 and best_move[0] in [(0, 0), (0, len(self.root.board[0]) - 1), (len(self.root.board) - 1, 0), (len(self.root.board) - 1, len(self.root.board[0]) - 1)]:
            return (best_move[0][0], best_move[0][1] + 1)  # Move one step away from the corner

        return best_move[0]

    # Clear Tree Function
    # Clears the game tree, resetting it to its initial state
    def clear_tree(self):
        self.root = None
