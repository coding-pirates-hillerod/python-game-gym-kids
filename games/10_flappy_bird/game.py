import random
import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (135, 206, 235)

BIRD_SIZE = 30
BIRD_COLOR = (255, 255, 0)

PIPE_WIDTH = 80
PIPE_COLOR = (0, 180, 0)

PIPE_GAP = 180

gravity = 0.5
jump_strength = -8

pipe_speed = 3

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("10 - Flappy Bird")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Bird
# ----------------------------------------

bird_x = 150
bird_y = HEIGHT // 2

velocity = 0

# ----------------------------------------
# Pipes
# ----------------------------------------

pipes = []

for i in range(3):

    gap_y = random.randint(150, 450)

    pipes.append(
        {
            "x": WIDTH + i * 300,
            "gap_y": gap_y,
            "scored": False,
        }
    )

# ----------------------------------------
# Score
# ----------------------------------------

score = 0

# ----------------------------------------
# Game Loop
# ----------------------------------------

running = True

while running:

    # ----------------------------------------
    # Events
    # ----------------------------------------

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                velocity = jump_strength

    # ----------------------------------------
    # Bird physics
    # ----------------------------------------

    velocity += gravity
    bird_y += velocity

    bird_rect = pygame.Rect(
        bird_x,
        bird_y,
        BIRD_SIZE,
        BIRD_SIZE,
    )

    # ----------------------------------------
    # Pipes
    # ----------------------------------------

    for pipe in pipes:

        pipe["x"] -= pipe_speed

        if not pipe["scored"] and pipe["x"] < bird_x:

            score += 1
            pipe["scored"] = True

        if pipe["x"] < -PIPE_WIDTH:

            pipe["x"] = WIDTH

            pipe["gap_y"] = random.randint(
                150,
                450,
            )

            pipe["scored"] = False

        top_pipe = pygame.Rect(
            pipe["x"],
            0,
            PIPE_WIDTH,
            pipe["gap_y"] - PIPE_GAP // 2,
        )

        bottom_pipe = pygame.Rect(
            pipe["x"],
            pipe["gap_y"] + PIPE_GAP // 2,
            PIPE_WIDTH,
            HEIGHT,
        )

        if bird_rect.colliderect(top_pipe):
            running = False

        if bird_rect.colliderect(bottom_pipe):
            running = False

    # ----------------------------------------
    # Ground / Ceiling
    # ----------------------------------------

    if bird_y < 0:
        running = False

    if bird_y > HEIGHT:
        running = False

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        BIRD_COLOR,
        bird_rect,
    )

    for pipe in pipes:

        pygame.draw.rect(
            screen,
            PIPE_COLOR,
            (
                pipe["x"],
                0,
                PIPE_WIDTH,
                pipe["gap_y"] - PIPE_GAP // 2,
            ),
        )

        pygame.draw.rect(
            screen,
            PIPE_COLOR,
            (
                pipe["x"],
                pipe["gap_y"] + PIPE_GAP // 2,
                PIPE_WIDTH,
                HEIGHT,
            ),
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