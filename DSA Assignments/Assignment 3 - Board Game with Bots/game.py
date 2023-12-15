#   Author: Catherine Leung
#   This is the game that you will code the bots to play.  You can also play against your bot
#   To run the game you will need pygames installed.  See: https://pypi.org/project/pygame/
#   Once you have pygames, you can run the game by using the command:
#   python game.py
#   
#   the gem images used are from opengameart.org by qubodup
#   https://opengameart.org/content/rotating-crystal-animation-8-step,
#   https://creativecommons.org/licenses/by/3.0/

# LINK PART C FUNCTION EXPLANATION (YOUTUBE) - https://youtu.be/8P7K_g-BOTw?feature=shared
# NOTE: Because of the video limit of 3 minutes, I did manage to explain the main functions I have added but
# I still added other small extra functions which were not explained in video because of time limit.

# Import necessary libraries and modules
import pygame
import sys
import math

# Importing functions and classes from other modules
from a1_partd import overflow
from a1_partc import Queue
from player1 import PlayerOne
from player2 import PlayerTwo

# Define the Dropdown class for the player selection menu
class Dropdown:
    def __init__(self, x, y, width, height, options):
        # Initialize Dropdown properties
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = options
        self.current_option = 0

    def draw(self, window):
        # Draw the dropdown menu on the window
        pygame.draw.rect(window, BLACK, (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(self.options[self.current_option], 1, BLACK)
        window.blit(text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        # Handle mouse clicks to change the selected option
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                self.current_option = (self.current_option + 1) % len(self.options)

    def get_choice(self):
        # Get the currently selected option
        return self.current_option

# Define the Game class for managing the game state
class Game:
    def __init__(self):
        # Initialize Game properties
        self.smartness_slider_value = 1
    
    def reset(self):
        # Reset the game state
        self.smartness_slider_value = 1
        self.has_winner = False
        self.overflowing = False
        self.numsteps = 0
        self.current_player = 0
        self.grid_row = -1
        self.grid_col = -1
        self.choice = [None, None]
        self.board = Board(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)
        self.overflow_boards = Queue()

    def draw_slider(self, window, x, y, value, max_value):
        # Draw the smartness slider on the window
        pygame.draw.rect(window, BLACK, (x, y, 150, 20), 2)  # Slider background
        pygame.draw.rect(
            window,
            BLACK,
            (x + 150 * (value / max_value), y, 2, 20),
        )  # Slider handle

        font = pygame.font.Font(None, 24)
        text = font.render("Smartness: {}".format(value), True, BLACK)
        window.blit(text, (x, y - 25))

    def update_smartness(self, event):
        # Update smartness based on mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if 850 <= x <= 1000 and 300 <= y <= 320:
                self.smartness_slider_value += 1
                if self.smartness_slider_value > 10:
                    self.smartness_slider_value = 1

    def animate_overflow(self, window, current_pos, target_pos, sprite, frame):
        # Animate the overflow with smooth movement
        current_pos = (
            current_pos[0] + (target_pos[0] - current_pos[0]) * 0.1,
            current_pos[1] + (target_pos[1] - current_pos[1]) * 0.1,
        )

        window.blit(sprite[math.floor(frame)], current_pos)

# Define the Board class for managing the game board
class Board:
    def __init__(self, width, height, p1_sprites, p2_sprites):
        # Initialize Board properties
        self.last_moves = []  # Keeping track of the last moves.
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.p1_sprites = p1_sprites
        self.p2_sprites = p2_sprites
        self.board[0][0] = 1
        self.board[self.height-1][self.width-1] = -1
        self.turn = 0
    
    def get_board(self):
        current_board = []
        for i in range(self.height):
            current_board.append(self.board[i].copy())
        return current_board

    def valid_move(self, row,col,player):
        if row >= 0  and row < self.height and col >= 0 and col < self.width and (self.board[row][col]==0 or self.board[row][col]/abs(self.board[row][col]) == player):
            return True
        return False

    def add_piece(self, row, col, player):
        if self.valid_move(row, col, player):
            self.last_moves.append((row, col, player))  # Storing the move
            self.board[row][col] += player
            self.turn += 1
            return True
        return False

    def undo_last_move(self):
        if self.turn > 0 and self.last_moves:
            row, col, player = self.last_moves.pop()
            self.board[row][col] = 0
            self.turn -= 1
            return True
        return False

    def check_win(self):
        if(self.turn > 0):
            num_p1 = 0
            num_p2 = 0
            for i in range(self.height):
                for j in range(self.width):
                    if(self.board[i][j] > 0):
                        if num_p2 > 0:
                            return 0
                        num_p1 += 1
                    elif(self.board[i][j] < 0):
                        if num_p1 > 0:
                            return 0
                        num_p2 += 1
            if(num_p1 == 0):
                return -1
            if(num_p2== 0):
                return 1
        return 0

    def do_overflow(self,q):
        oldboard = []
        for i in range(self.height):
            oldboard.append(self.board[i].copy())
        numsteps = overflow(self.board, q)
        if(numsteps != 0):
            self.set(oldboard)
        return numsteps
    
    def set(self, newboard):
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col] = newboard[row][col]

    def draw(self, window, frame):
        for row in range(GRID_SIZE[0]):
            for col in range(GRID_SIZE[1]):
                rect = pygame.Rect(col * CELL_SIZE + X_OFFSET, row * CELL_SIZE+Y_OFFSET, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, BLACK, rect, 1)
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] != 0:
                    rpos = row * CELL_SIZE + Y_OFFSET
                    cpos = col * CELL_SIZE + X_OFFSET

                    if self.board[row][col] > 0:
                        sprite = p1_sprites
                    else:
                        sprite = p2_sprites
                    if abs(self.board[row][col]) == 1:
                        cpos += CELL_SIZE //2 - 16
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 2:
                        cpos += CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))

                    elif abs(self.board[row][col]) == 3:
                        cpos += CELL_SIZE //2 - 16
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos = col * CELL_SIZE + X_OFFSET + CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 4:
                        cpos += CELL_SIZE //2 - 32
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos -= CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))




# Constants
GRID_SIZE = (5, 6)
CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X_OFFSET = 0
Y_OFFSET = 100
FULL_DELAY = 5

# Load sprite images
# hate the colours?  there are other options.  Just change the lines below to another colour's file name.  
# the following are available blue, pink, yellow, orange, grey, green
p1spritesheet = pygame.image.load('blue.png')
p2spritesheet = pygame.image.load('pink.png')
p1_sprites = []
p2_sprites = []


player_id = [1 , -1]

# Create sprite images
for i in range(8):
    curr_sprite = pygame.Rect(32*i,0,32,32)
    p1_sprites.append(p1spritesheet.subsurface(curr_sprite))
    p2_sprites.append(p2spritesheet.subsurface(curr_sprite))    


frame = 0

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((1200,800))

pygame.font.init()
font = pygame.font.Font(None, 36)  # Change the size as needed
bigfont = pygame.font.Font(None, 108)
# Create the game board
# board = [[0 for _ in range(GRID_SIZE[0])] for _ in range(GRID_SIZE[1])]
player1_dropdown = Dropdown(900, 50, 200, 50, ['Human', 'AI'])
player2_dropdown = Dropdown(900, 110, 200, 50, ['Human', 'AI'])

status=["",""]
current_player = 0
board = Board(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)
# Game loop

game = Game()  # Create an instance of the Game class
reset_button_rect = pygame.Rect(850, 250, 100, 50)  # Define the reset button rectangle

running = True
overflow_boards = Queue()
overflowing = False
numsteps = 0
has_winner = False
bots = [PlayerOne(), PlayerTwo()]
grid_col = -1
grid_row = -1
choice = [None, None]
while running:
    # Handling Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            player1_dropdown.handle_event(event)
            player2_dropdown.handle_event(event)
            game.update_smartness(event)  # Update smartness with slider
            choice[0] = player1_dropdown.get_choice()
            choice[1] = player2_dropdown.get_choice()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if 850 < x < 950 and 180 < y < 230:  # Checking the case when the undo button is pressed!!
                    board.undo_last_move()
                    current_player = (current_player + 1) % 2
                row = y - Y_OFFSET
                col = x - X_OFFSET    
                grid_row, grid_col = row // CELL_SIZE, col // CELL_SIZE
    # Checking for a winner
    win = board.check_win()
    if win != 0:
        winner = 1
        if win == -1:
            winner = 2
        has_winner = True

    if not has_winner:
        if overflowing:
            status[0] = "Overflowing"
            if not overflow_boards.is_empty():
                if repeat_step == FULL_DELAY:
                    next = overflow_boards.dequeue()
                    board.set(next)
                    repeat_step = 0
                else:
                    repeat_step += 1
            else:
                overflowing = False

                # goes between 0 and 1
                current_player = (current_player + 1) % 2

        else:
            status[0] = "Player " + str(current_player + 1) + "'s turn"
            make_move = False
            if choice[current_player] == 1:
                (grid_row,grid_col) = bots[current_player].get_play(board.get_board(), game.smartness_slider_value)
                status[1] = "Bot chose row {}, col {}".format(grid_row, grid_col)
                if not board.valid_move(grid_row, grid_col, player_id[current_player]):
                       has_winner = True
                       # if p1 makes an invalid move, p2 wins.  if p2 makes an invalid move p1 wins
                       winner = ((current_player + 1) % 2) + 1 
                else:
                    make_move = True
            else:
                if board.valid_move(grid_row, grid_col, player_id[current_player]):
                    make_move = True

            if make_move:
                board.add_piece(grid_row, grid_col, player_id[current_player])
                numsteps = board.do_overflow(overflow_boards)
                if numsteps != 0:
                    overflowing = True
                    repeat_step = 0
                else:
                    current_player = (current_player + 1) % 2
                grid_row = -1
                grid_col = -1   

    # Drawing the game board
    window.fill(WHITE)
    board.draw(window,frame)
    window.blit(p1_sprites[math.floor(frame)], (850, 60))
    window.blit(p2_sprites[math.floor(frame)], (850, 120))
    frame = (frame + 0.5) % 8
    player1_dropdown.draw(window)
    player2_dropdown.draw(window)

    pygame.draw.rect(window, BLACK, (850, 180, 100, 50), 2)  # Making the undo button
    text = font.render("Undo", True, BLACK)
    window.blit(text, (870, 190))

    if not has_winner:  
        text = font.render(status[0], True, (0, 0, 0))  # Black color
        window.blit(text, (X_OFFSET, 750 ))
        text = font.render(status[1], True, (0, 0, 0))  # Black color
        window.blit(text, (X_OFFSET,  700 ))
    else:
        text = bigfont.render("Player " + str(winner)  + " wins!", True, (0, 0, 0))  # Black color
        window.blit(text, (300, 250))

    game.draw_slider(window, 850, 300, game.smartness_slider_value, 10)  # Draw the smartness slider

    pygame.display.update()
    pygame.time.delay(100)

    # Validate if the game is over
    if has_winner:
        # Reset the game after a delay
        pygame.time.delay(2000)  # 2 seconds delay after game over
        game.reset()

pygame.quit()
sys.exit()
