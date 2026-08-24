import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

PLAYER_SIZE = 40
PLAYER_COLOR = (0, 200, 0)

ENEMY_SIZE = 35
ENEMY_COLOR = (200, 50, 50)

BULLET_WIDTH = 6
BULLET_HEIGHT = 16
BULLET_COLOR = (255, 255, 0)

BACKGROUND_COLOR = (20, 20, 30)

player_speed = 6
enemy_speed = 2
bullet_speed = 8

ROWS = 3
COLUMNS = 6

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("07 - Space Invaders")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Player
# ----------------------------------------

player_x = WIDTH // 2
player_y = HEIGHT - 80

# ----------------------------------------
# Bullets
# ----------------------------------------

bullets = []

# ----------------------------------------
# Invaders
# ----------------------------------------

enemies = []

start_x = 120
start_y = 80

spacing_x = 80
spacing_y = 60

for row in range(ROWS):
    for column in range(COLUMNS):

        enemies.append(
            {
                "x": start_x + column * spacing_x,
                "y": start_y + row * spacing_y,
            }
        )

enemy_direction = 1

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
    # Player movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    player_x = max(
        0,
        min(player_x, WIDTH - PLAYER_SIZE)
    )

    # ----------------------------------------
    # Bullets
    # ----------------------------------------

    for bullet in bullets[:]:

        bullet["y"] -= bullet_speed

        if bullet["y"] < 0:
            bullets.remove(bullet)

    # ----------------------------------------
    # Enemy formation movement
    # ----------------------------------------

    move_down = False

    for enemy in enemies:

        enemy["x"] += enemy_speed * enemy_direction

        if enemy["x"] <= 0:
            move_down = True

        if enemy["x"] >= WIDTH - ENEMY_SIZE:
            move_down = True

    if move_down:

        enemy_direction *= -1

        for enemy in enemies:
            enemy["y"] += 20

    # ----------------------------------------
    # Collision
    # ----------------------------------------

    for bullet in bullets[:]:

        bullet_rect = pygame.Rect(
            bullet["x"],
            bullet["y"],
            BULLET_WIDTH,
            BULLET_HEIGHT,
        )

        for enemy in enemies[:]:

            enemy_rect = pygame.Rect(
                enemy["x"],
                enemy["y"],
                ENEMY_SIZE,
                ENEMY_SIZE,
            )

            if bullet_rect.colliderect(enemy_rect):

                score += 1

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy in enemies:
                    enemies.remove(enemy)

                break

    # ----------------------------------------
    # Game Over
    # ----------------------------------------

    for enemy in enemies:

        if enemy["y"] > HEIGHT - 120:
            running = False

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

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

    if not enemies:

        win_text = font.render(
            "DU VANDT!",
            True,
            (0, 255, 0),
        )

        screen.blit(
            win_text,
            (WIDTH // 2 - 100, HEIGHT // 2),
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()