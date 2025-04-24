import pygame
from button import Button
from menu import Menu
import time
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Puissance 4 Menu")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

font = pygame.font.Font("assets/NotoSans-Bold.ttf", SCREEN_WIDTH // 40)
# Create a font object for the title
menu = Menu(screen,font, SCREEN_WIDTH, SCREEN_HEIGHT)
current_menu = menu  # Initialize the current menu
# Initialize the menu


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        current_menu.handle_event(event)  # Handle button click
        # Check which button was clicked and perform the corresponding action

    # Draw the menu
    current_menu.draw()

    # Update the display
    pygame.display.flip()

pygame.quit()