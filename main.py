import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Player settings
player_width, player_height = 50, 50
player_x = 100
player_y = HEIGHT - player_height
player_y_vel = 0
gravity = 0.8
jump_strength = -15
is_jumping = False

# Obstacle settings
obstacle_width = 50
obstacle_height = 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height
obstacle_speed = 6

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_y_vel = jump_strength
        is_jumping = True

    # Apply gravity
    player_y_vel += gravity
    player_y += player_y_vel

    # Check if player hits the ground
    if player_y >= HEIGHT - player_height:
        player_y = HEIGHT - player_height
        is_jumping = False

    # Move obstacle
    obstacle_x -= obstacle_speed
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH + random.randint(0, 200)
        score += 1

    # Collision detection
    if (
        player_x < obstacle_x + obstacle_width
        and player_x + player_width > obstacle_x
        and player_y + player_height > obstacle_y
    ):
        running = False  # End game on collision

    # Draw player and obstacle
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
 
 