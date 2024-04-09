import random
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Direction vectors
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Main function
def main():
    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()

    # Load the apple image and resize it to match the block size
    apple_image = pygame.image.load('apple.jpg').convert_alpha()  # Load image with alpha channel
    apple_image = pygame.transform.scale(apple_image, (BLOCK_SIZE, BLOCK_SIZE))

    # Make white color transparent
    apple_image.set_colorkey(WHITE)

    # Snake properties
    snake_length = 1
    snake_positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    snake_direction = random.choice([UP, DOWN, LEFT, RIGHT])

    # Food position
    food_pos = (random.randint(0, GRID_WIDTH-1) * BLOCK_SIZE, random.randint(0, GRID_HEIGHT-1) * BLOCK_SIZE)

    # Score
    score = 0
    gameover = False

    # Sound effects
    pygame.mixer.init() 
    add_piece_sound = pygame.mixer.Sound('eating-sound-effect-36186.mp3')
    game_over_sound = pygame.mixer.Sound('videogame-death-sound-43894.mp3')

    # Background music
    pygame.mixer.music.load('Future - Solo (Clean Version).mp3')
    pygame.mixer.music.set_volume(0.2)  # Set the volume to 20% of the maximum volume
    pygame.mixer.music.play(-1)  # -1 makes the music loop indefinitely

    # Background color
    background_color = BLACK

    # Blinking eyes
    blink_timer = pygame.time.get_ticks()
    blink_interval = 500  # 1 second
    snake_blink = False  # Initialize snake blink variable

    # Snake speed
    snake_speed = 10  # Update snake position every 10 milliseconds

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not gameover:
                    if event.key == pygame.K_UP and snake_direction != DOWN:
                        snake_direction = UP
                    elif event.key == pygame.K_DOWN and snake_direction != UP:
                        snake_direction = DOWN
                    elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                        snake_direction = LEFT
                    elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                        snake_direction = RIGHT
                if event.key == pygame.K_y and gameover == True:
                    gameover = False
                    snake_length = 1
                    snake_positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
                    snake_direction = random.choice([UP, DOWN, LEFT, RIGHT])
                    score = 0
                    food_pos = (random.randint(0, GRID_WIDTH-1) * BLOCK_SIZE, random.randint(0, GRID_HEIGHT-1) * BLOCK_SIZE)
                    pygame.mixer.music.play(-1)  # Start background music again
                elif event.key == pygame.K_n and gameover == True:
                    running = False

        # Move the snake if the game is not over
        if not gameover:
            new_head = ((snake_positions[0][0] + snake_direction[0] * BLOCK_SIZE),
                        (snake_positions[0][1] + snake_direction[1] * BLOCK_SIZE))

            # Check if snake hits the edge of the window
            if (new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or
                new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT):
                # Game over
                gameover = True
                game_over_sound.play()  # Play game over sound
                pygame.mixer.music.stop()  # Stop the background music

            else:
                # Check if snake eats food
                if new_head == food_pos:
                    snake_length += 1
                    score += 1
                    if score % 5 == 0:  # Check if score is a multiple of 5
                        # Change background color
                        background_color = random.choice([RED, GREEN, BLUE])
                    food_pos = (random.randint(0, GRID_WIDTH - 1) * BLOCK_SIZE,
                                random.randint(0, GRID_HEIGHT - 1) * BLOCK_SIZE)
                    add_piece_sound.play()  # Play sound when new piece added
                else:
                    # Check if snake collides with itself
                    if new_head in snake_positions[1:]:
                        gameover = True
                        game_over_sound.play()
                        pygame.mixer.music.stop()  # Stop the background music
                    else:
                        snake_positions.insert(0, new_head)
                        if len(snake_positions) > snake_length:
                            snake_positions.pop()

        # Check blinking eyes
        if pygame.time.get_ticks() - blink_timer > blink_interval:
            blink_timer = pygame.time.get_ticks()
            snake_blink = not snake_blink

        # Fill the screen with background color
        screen.fill(background_color)

        # Draw the snake
        for index, position in enumerate(snake_positions):
            if index == 0:
                if snake_blink:  # Draw blinking eyes on the snake's head
                    pygame.draw.rect(screen, WHITE, (position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.circle(screen, BLACK, (position[0] + BLOCK_SIZE // 3, position[1] + BLOCK_SIZE // 3), 3)
                    pygame.draw.circle(screen, BLACK, (position[0] + 2 * BLOCK_SIZE // 3, position[1] + BLOCK_SIZE // 3), 3)
                else:
                    pygame.draw.rect(screen, WHITE, (position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))
                    pygame.draw.circle(screen, WHITE, (position[0] + BLOCK_SIZE // 3, position[1] + BLOCK_SIZE // 3), 3)
                    pygame.draw.circle(screen, WHITE, (position[0] + 2 * BLOCK_SIZE // 3, position[1] + BLOCK_SIZE // 3), 3)
            else:
                pygame.draw.rect(screen, WHITE, (position[0], position[1], BLOCK_SIZE, BLOCK_SIZE))

        # Draw the food
        screen.blit(apple_image, food_pos)

        # Draw the score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: {}".format(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        # If game over, display "Game Over" message
        if gameover:
            font = pygame.font.Font(None, 36)
            game_over_text = font.render("Game Over", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20))
            score_display = font.render("Your Score: {}".format(score), True, WHITE)
            score_rect = score_display.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
            play_again_text = font.render("Play Again? (y/n)", True, RED)
            play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
            screen.blit(game_over_text, game_over_rect)
            screen.blit(score_display, score_rect)
            screen.blit(play_again_text, play_again_rect)

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(snake_speed)  # Adjust frame rate for smoother gameplay

    # Quit Pygame
    pygame.quit()

# Call the main function to start the game
main()
