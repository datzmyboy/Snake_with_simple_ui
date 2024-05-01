import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
def run():
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("")

    # Define color (RGB format)
    BLACK = (0, 0, 0)

    # Fill the screen with black color
    screen.fill(BLACK)

    # Update the display
    pygame.display.flip()

    # Pause for a brief moment (e.g., 2 seconds)
    pygame.time.wait(100)


run()
pygame.quit()