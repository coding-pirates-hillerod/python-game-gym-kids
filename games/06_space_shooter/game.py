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

BULLET_WIDTH = 8
BULLET_HEIGHT = 16
BULLET_COLOR = (255, 255, 0)

BACKGROUND_COLOR = (20, 20, 30)

player_speed = 5
enemy_speed = 3
bullet_speed = 8

enemy_count = 5

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("06 - Space Shooter")

font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

# ----------------------------------------
# Player
# ----------------------------------------

player_x = WIDTH // 2
player_y = HEIGHT - 80

# ----------------------------------------
# Enemies
# ----------------------------------------

enemies = []

for _ in range(enemy_count):
    enemies.append(
        {
            "x": random.randint(0, WIDTH - ENEMY_SIZE),
            "y": random.randint(-600, -50),
        }
    )

# ----------------------------------------
# Bullets
# ----------------------------------------

bullets = []

# ----------------------------------------
# Score
# ----------------------------------------

score = 0

# ----------------------------------------
# Game Loop
# ----------------------------------------

running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:

                bullets.append(
                    {
                        "x": player_x + PLAYER_SIZE // 2,
                        "y": player_y,
                    }
                )

    # ----------------------------------------
    # Movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    player_x = max(0, min(player_x, WIDTH - PLAYER_SIZE))
    player_y = max(0, min(player_y, HEIGHT - PLAYER_SIZE))

    # ----------------------------------------
    # Player rectangle
    # ----------------------------------------

    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    # ----------------------------------------
    # Update bullets
    # ----------------------------------------

    for bullet in bullets[:]:

        bullet["y"] -= bullet_speed

        if bullet["y"] < 0:
            bullets.remove(bullet)

    # ----------------------------------------
    # Update enemies
    # ----------------------------------------

    for enemy in enemies:

        enemy["y"] += enemy_speed

        if enemy["y"] > HEIGHT:

            enemy["y"] = random.randint(-300, -50)
            enemy["x"] = random.randint(0, WIDTH - ENEMY_SIZE)

    # ----------------------------------------
    # Bullet collisions
    # ----------------------------------------

    for bullet in bullets[:]:

        bullet_rect = pygame.Rect(
            bullet["x"],
            bullet["y"],
            BULLET_WIDTH,
            BULLET_HEIGHT,
        )

        for enemy in enemies:

            enemy_rect = pygame.Rect(
                enemy["x"],
                enemy["y"],
                ENEMY_SIZE,
                ENEMY_SIZE,
            )

            if bullet_rect.colliderect(enemy_rect):

                score += 1

                enemy["y"] = random.randint(-300, -50)
                enemy["x"] = random.randint(0, WIDTH - ENEMY_SIZE)

                if bullet in bullets:
                    bullets.remove(bullet)

                break

    # ----------------------------------------
    # Drawing
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

    for bullet in bullets:

        pygame.draw.rect(
            screen,
            BULLET_COLOR,
            (
                bullet["x"],
                bullet["y"],
                BULLET_WIDTH,
                BULLET_HEIGHT,
            ),
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