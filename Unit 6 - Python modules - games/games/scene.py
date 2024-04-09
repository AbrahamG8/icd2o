import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Bowl Still Life")

# Define colors
WHITE = (255, 255, 255)
BLUE = (65, 105, 225)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BROWN = (139, 69, 19)
GREEN = (34, 139, 34)
PINK = (255, 20, 147)  # Very hot pink
PURPLE = (128, 0, 128)

# Set up clock
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill background with blue
    screen.fill(BLUE)
    
    # Draw table
    pygame.draw.rect(screen, PINK, (0, 262, WIDTH, HEIGHT - 450))
    
    # Draw bowl
    pygame.draw.ellipse(screen, BROWN, (300, 300, 200, 100))
    pygame.draw.arc(screen, BROWN, (300, 275, 200, 100), 0, 3.14, 5)
    pygame.draw.line(screen, BROWN, (300, 325), (500, 325), 5)
    
    # Draw fruits
    pygame.draw.circle(screen, RED, (350, 325), 30)  # Apple
    pygame.draw.circle(screen, YELLOW, (400, 350), 25)  # Lemon
    pygame.draw.circle(screen, ORANGE, (450, 325), 30)  # Orange
    pygame.draw.circle(screen, GREEN, (375, 375), 20)  # Pear
    pygame.draw.circle(screen, PURPLE, (425, 375), 20)  # Plum
    
    # Update display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
