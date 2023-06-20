import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Set up the ball
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_dx = random.choice([-2, 2])
ball_dy = random.choice([-2, 2])
ball_color = (255, 0, 0)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collision with walls
    if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
        ball_dx *= -1
    if ball_y < ball_radius or ball_y > HEIGHT - ball_radius:
        ball_dy *= -1

    # Fill the background
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()