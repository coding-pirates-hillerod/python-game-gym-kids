import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (135, 206, 235)

PLAYER_SIZE = 40
PLAYER_COLOR = (0, 180, 0)

PLATFORM_COLOR = (120, 80, 40)

STAR_COLOR = (255, 215, 0)
STAR_SIZE = 20

player_speed = 5
gravity = 0.5
jump_strength = -12

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("11 - Platformer")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Player
# ----------------------------------------

player_x = 100
player_y = 300

velocity_y = 0

on_ground = False

# ----------------------------------------
# Platforms
# ----------------------------------------

platforms = [
    pygame.Rect(0, 550, 800, 50),
    pygame.Rect(150, 450, 200, 20),
    pygame.Rect(450, 350, 200, 20),
    pygame.Rect(250, 250, 150, 20),
]

# ----------------------------------------
# Star
# ----------------------------------------

star_x = 300
star_y = 200

# ----------------------------------------
# Score
# ----------------------------------------

score = 0

# ----------------------------------------
# Functions
# ----------------------------------------

def reset_star():
    return 500, 300

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

            if event.key == pygame.K_UP:

                if on_ground:
                    velocity_y = jump_strength

    # ----------------------------------------
    # Movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # ----------------------------------------
    # Gravity
    # ----------------------------------------

    velocity_y += gravity
    player_y += velocity_y

    player_rect = pygame.Rect(
        player_x,
        player_y,
        PLAYER_SIZE,
        PLAYER_SIZE,
    )

    on_ground = False

    # ----------------------------------------
    # Platform Collisions
    # ----------------------------------------

    for platform in platforms:

        if (
            player_rect.colliderect(platform)
            and velocity_y > 0
        ):

            player_rect.bottom = platform.top

            player_y = player_rect.y

            velocity_y = 0

            on_ground = True

    # ----------------------------------------
    # Keep player on screen
    # ----------------------------------------

    player_x = max(
        0,
        min(player_x, WIDTH - PLAYER_SIZE)
    )

    # ----------------------------------------
    # Star Collision
    # ----------------------------------------

    star_rect = pygame.Rect(
        star_x,
        star_y,
        STAR_SIZE,
        STAR_SIZE,
    )

    if player_rect.colliderect(star_rect):

        score += 1

        star_x, star_y = reset_star()

    # ----------------------------------------
    # Fall off level
    # ----------------------------------------

    if player_y > HEIGHT:
        running = False

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    for platform in platforms:

        pygame.draw.rect(
            screen,
            PLATFORM_COLOR,
            platform,
        )

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
        (0, 0, 0),
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()