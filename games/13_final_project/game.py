import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (30, 30, 30)

PLAYER_SIZE = 40
PLAYER_COLOR = (0, 200, 0)

PLAYER_SPEED = 5

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("13 - My Own Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Player
# ----------------------------------------

player_x = WIDTH // 2
player_y = HEIGHT // 2

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

    # ----------------------------------------
    # Movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED

    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED

    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED

    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        (
            player_x,
            player_y,
            PLAYER_SIZE,
            PLAYER_SIZE,
        ),
    )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    screen.blit(score_text, (20, 20))

    info_text = font.render(
        "Build your own game!",
        True,
        (255, 255, 0),
    )

    screen.blit(info_text, (180, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()