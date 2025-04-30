import pygame
from menu import Menu
from game import Menu_Puissance4
import time
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

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
        action = current_menu.handle_event(event)
        if action is not None:  # Ensure action is not None before proceeding
            if action == "quit": # Check if the quit action was triggered
                running = False
            elif action == "single_player":
                current_menu = Menu_Puissance4(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)
            elif action == "lan":
                print("LAN mode selected")
            elif action == "options":
                print("Options mode selected")
                # You can implement an options menu here to allow the user to adjust settings like sound, difficulty, or controls.

    # Draw the menu
    current_menu.draw()
    if current_menu != "self":
        if current_menu.menu == "main":
            current_menu = menu
    # Update the display
    pygame.display.flip()

pygame.quit()