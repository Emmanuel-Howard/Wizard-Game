# A flying wizard game with spells

# Importing necessary modules
import pygame
import time
pygame.init()

# Create Window
WIDTH, HEIGHT = 900, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mystic Grove")

# Set Wizard Width / Height / Velocity
WIZARD_WIDTH = 100
WIZARD_HEIGHT = 150
WIZARD_VEL = 7.5

# Set Wizard image
WIZARD_IMAGE = pygame.image.load("resources/Idle.png")
WIZARD_IMAGE = pygame.transform.scale(WIZARD_IMAGE, (WIZARD_WIDTH, WIZARD_HEIGHT))

# Set background image
BG = pygame.image.load("resources/forest_background.jpg")
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# Function that "draws" elements on the window
def draw(wizard):
    WIN.blit(BG, (0,0))   # Draws background on Window
    WIN.blit(WIZARD_IMAGE, (wizard.x, wizard.y))

    pygame.display.update()   # Updates the display

# Main Game Loop
def main():
    run = True

# Create player variable as a rectangle
    wizard = pygame.Rect(400, HEIGHT - WIZARD_HEIGHT, WIZARD_WIDTH, WIZARD_HEIGHT)

# Set clock for frame rate control
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(60) # Sets max frame rate at 60 fps
        elapsed_time = time.time() - start_time

# Break game loop if User exits the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

# Guard Clause that skips loop if wizard becomes invalid
        if not wizard:
            continue

# Sets player movement based on keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and wizard.x - WIZARD_VEL >= 0: # If "a" is pressed and player is more than 0 (edge)
            wizard.x -= WIZARD_VEL   # Move left by velocity
        if keys[pygame.K_d] and wizard.x + WIZARD_VEL + WIZARD_WIDTH<= WIDTH: # If "d" is pressed and player is more than WIDTH
            wizard.x += WIZARD_VEL   # Move right by velocity

        draw(wizard)   # Uses the draw function to draw on WIN

    pygame.quit()   # Quits pygame

# Guard Clause
if __name__ == "__main__":
    main()