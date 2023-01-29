import pygame

# Initialize pygame
pygame.init()

# Set the size of the Tic-Tac-Toe board
board_size = (300, 300)

# Set the size of the cells on the Tic-Tac-Toe board
cell_size = (100, 100)

# Create the Tic-Tac-Toe board as a 2D list
board = [[None for _ in range(3)] for _ in range(3)]

# Create the window for the game
screen = pygame.display.set_mode(board_size)

# Set the caption of the window
pygame.display.set_caption("Tic-Tac-Toe")

# Set the current player (X or O)
current_player = "X"

# Set the font for displaying the player's move
font = pygame.font.Font(None, 50)

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the cell that was clicked
            x, y = event.pos
            row, col = y // cell_size[1], x // cell_size[0]
            # Check if the cell is empty
            if board[row][col] is None:
                # Make the move
                board[row][col] = current_player
                # Switch the current player
                current_player = "O" if current_player == "X" else "X"
    # Draw the Tic-Tac-Toe board
    screen.fill((255, 255, 255))
    for r in range(3):
        for c in range(3):
            pygame.draw.rect(screen, (0, 0, 0), (c * cell_size[0], r * cell_size[1], cell_size[0], cell_size[1]), 2)
            if board[r][c] is not None:
                text = font.render(board[r][c], True, (0, 0, 0))
                screen.blit(text, (c * cell_size[0] + 35, r * cell_size[1] + 20))
    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()
