import random
import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

PLAYER_SIZE = 40
PLAYER_COLOR = (0, 200, 0)

STAR_SIZE = 25
STAR_COLOR = (255, 215, 0)

BACKGROUND_COLOR = (30, 30, 30)

player_speed = 5

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("03 - Score Counter")

font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

# ----------------------------------------
# Player
# ----------------------------------------

player_x = WIDTH // 2
player_y = HEIGHT // 2

# ----------------------------------------
# Star
# ----------------------------------------

star_x = random.randint(50, WIDTH - 50)
star_y = random.randint(50, HEIGHT - 50)

# ----------------------------------------
# Score
# ----------------------------------------

score = 0

# ----------------------------------------
# Game loop
# ----------------------------------------

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Collision
    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    star_rect = pygame.Rect(
        star_x,
        star_y,
        STAR_SIZE,
        STAR_SIZE,
    )

    if player_rect.colliderect(star_rect):
        score += 1

        star_x = random.randint(50, WIDTH - 50)
        star_y = random.randint(50, HEIGHT - 50)

    # Drawing
    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player_rect,
    )

    pygame.draw.circle(
        screen,
        STAR_COLOR,
        (star_x, star_y),
        STAR_SIZE,
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()