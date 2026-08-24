import random
import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

GRID_SIZE = 20

BACKGROUND_COLOR = (30, 30, 30)

SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (255, 50, 50)

GAME_SPEED = 10

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("08 - Snake")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Snake
# ----------------------------------------

snake = [
    [200, 200],
    [180, 200],
    [160, 200],
]

direction_x = GRID_SIZE
direction_y = 0

# ----------------------------------------
# Food
# ----------------------------------------

food_x = random.randrange(
    0,
    WIDTH,
    GRID_SIZE,
)

food_y = random.randrange(
    0,
    HEIGHT,
    GRID_SIZE,
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

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and direction_x == 0:
                direction_x = -GRID_SIZE
                direction_y = 0

            if event.key == pygame.K_RIGHT and direction_x == 0:
                direction_x = GRID_SIZE
                direction_y = 0

            if event.key == pygame.K_UP and direction_y == 0:
                direction_x = 0
                direction_y = -GRID_SIZE

            if event.key == pygame.K_DOWN and direction_y == 0:
                direction_x = 0
                direction_y = GRID_SIZE

    # ----------------------------------------
    # Move snake
    # ----------------------------------------

    head_x = snake[0][0] + direction_x
    head_y = snake[0][1] + direction_y

    new_head = [head_x, head_y]

    snake.insert(0, new_head)

    # ----------------------------------------
    # Eat food
    # ----------------------------------------

    if head_x == food_x and head_y == food_y:

        score += 1

        food_x = random.randrange(
            0,
            WIDTH,
            GRID_SIZE,
        )

        food_y = random.randrange(
            0,
            HEIGHT,
            GRID_SIZE,
        )

    else:
        snake.pop()

    # ----------------------------------------
    # Wall collision
    # ----------------------------------------

    if (
        head_x < 0
        or head_x >= WIDTH
        or head_y < 0
        or head_y >= HEIGHT
    ):
        running = False

    # ----------------------------------------
    # Self collision
    # ----------------------------------------

    if new_head in snake[1:]:
        running = False

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    # Draw snake
    for segment in snake:

        pygame.draw.rect(
            screen,
            SNAKE_COLOR,
            (
                segment[0],
                segment[1],
                GRID_SIZE,
                GRID_SIZE,
            ),
        )

    # Draw food
    pygame.draw.rect(
        screen,
        FOOD_COLOR,
        (
            food_x,
            food_y,
            GRID_SIZE,
            GRID_SIZE,
        ),
    )

    # Draw score
    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    screen.blit(score_text, (20, 20))

    pygame.display.flip()

    clock.tick(GAME_SPEED)

pygame.quit()