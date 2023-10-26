import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display dimensions
display_width = 800
display_height = 600

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Set up the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Obstacle Warrior')

# Clock for managing frames per second
clock = pygame.time.Clock()

# Set up the player
player_width = 50
player_height = 50
player_x = display_width * 0.45
player_y = display_height * 0.8
player_speed = 5

# Set up the obstacle
obstacle_width = 100
obstacle_height = 100
obstacle_x = random.randrange(0, display_width - obstacle_width)
obstacle_y = -600
obstacle_speed = 7

# Functions to draw the player and obstacle
def draw_player(x, y):
    pygame.draw.rect(game_display, black, [x, y, player_width, player_height])

def draw_obstacle(x, y):
    pygame.draw.rect(game_display, red, [x, y, obstacle_width, obstacle_height])

# Game loop
game_exit = False
while not game_exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < display_width - player_width:
        player_x += player_speed

    # Move the obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > display_height:
        obstacle_y = 0
        obstacle_x = random.randrange(0, display_width - obstacle_width)

    # Check for collision
    if player_y < obstacle_y + obstacle_height:
        if player_x > obstacle_x and player_x < obstacle_x + obstacle_width or \
           player_x + player_width > obstacle_x and player_x + player_width < obstacle_x + obstacle_width:
            print("Game Over!")

    # Update display
    game_display.fill(white)
    draw_player(player_x, player_y)
    draw_obstacle(obstacle_x, obstacle_y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
