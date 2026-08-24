import random
import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

PLAYER_SIZE = 40
PLAYER_COLOR = (0, 200, 0)

ENEMY_SIZE = 40
ENEMY_COLOR = (200, 50, 50)

BACKGROUND_COLOR = (30, 30, 30)

player_speed = 5
enemy_speed = 4

enemy_count = 5

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("05 - Multiple Enemies")

font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

# ----------------------------------------
# Player
# ----------------------------------------

player_x = WIDTH // 2
player_y = HEIGHT - 100

# ----------------------------------------
# Enemies
# ----------------------------------------

enemies = []

for _ in range(enemy_count):

    enemy = {
        "x": random.randint(0, WIDTH - ENEMY_SIZE),
        "y": random.randint(-600, 0),
    }

    enemies.append(enemy)

# ----------------------------------------
# Score and Lives
# ----------------------------------------

score = 0
lives = 3

# ----------------------------------------
# Game Loop
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

    # Keep player on screen
    player_x = max(0, min(player_x, WIDTH - PLAYER_SIZE))
    player_y = max(0, min(player_y, HEIGHT - PLAYER_SIZE))

    # Player rectangle
    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    # Update enemies
    for enemy in enemies:

        enemy["y"] += enemy_speed

        if enemy["y"] > HEIGHT:

            enemy["y"] = random.randint(-200, -50)
            enemy["x"] = random.randint(0, WIDTH - ENEMY_SIZE)

            score += 1

        enemy_rect = pygame.Rect(
            enemy["x"],
            enemy["y"],
            ENEMY_SIZE,
            ENEMY_SIZE,
        )

        if player_rect.colliderect(enemy_rect):

            lives -= 1

            enemy["y"] = random.randint(-200, -50)
            enemy["x"] = random.randint(0, WIDTH - ENEMY_SIZE)

    # Game Over
    if lives <= 0:
        running = False

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player_rect,
    )

    for enemy in enemies:

        pygame.draw.rect(
            screen,
            ENEMY_COLOR,
            (
                enemy["x"],
                enemy["y"],
                ENEMY_SIZE,
                ENEMY_SIZE,
            ),
        )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    lives_text = font.render(
        f"Liv: {lives}",
        True,
        (255, 255, 255),
    )

    screen.blit(score_text, (20, 20))
    screen.blit(lives_text, (20, 70))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()