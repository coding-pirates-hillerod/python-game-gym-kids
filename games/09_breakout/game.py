import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (30, 30, 30)

PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_COLOR = (0, 200, 0)

BALL_SIZE = 16
BALL_COLOR = (255, 255, 255)

BRICK_WIDTH = 80
BRICK_HEIGHT = 30
BRICK_COLOR = (200, 50, 50)

ROWS = 4
COLUMNS = 8

PADDLE_SPEED = 7

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("09 - Breakout")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# Paddle
# ----------------------------------------

paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
paddle_y = HEIGHT - 50

# ----------------------------------------
# Ball
# ----------------------------------------

ball_x = WIDTH // 2
ball_y = HEIGHT // 2

ball_speed_x = 4
ball_speed_y = -4

# ----------------------------------------
# Bricks
# ----------------------------------------

bricks = []

start_x = 60
start_y = 60

for row in range(ROWS):
    for column in range(COLUMNS):

        bricks.append(
            pygame.Rect(
                start_x + column * (BRICK_WIDTH + 10),
                start_y + row * (BRICK_HEIGHT + 10),
                BRICK_WIDTH,
                BRICK_HEIGHT,
            )
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

    # ----------------------------------------
    # Paddle movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        paddle_x -= PADDLE_SPEED

    if keys[pygame.K_RIGHT]:
        paddle_x += PADDLE_SPEED

    paddle_x = max(
        0,
        min(paddle_x, WIDTH - PADDLE_WIDTH)
    )

    # ----------------------------------------
    # Ball movement
    # ----------------------------------------

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # ----------------------------------------
    # Wall collision
    # ----------------------------------------

    if ball_x <= 0:
        ball_speed_x *= -1

    if ball_x >= WIDTH - BALL_SIZE:
        ball_speed_x *= -1

    if ball_y <= 0:
        ball_speed_y *= -1

    if ball_y > HEIGHT:
        running = False

    # ----------------------------------------
    # Rectangles
    # ----------------------------------------

    paddle_rect = pygame.Rect(
        paddle_x,
        paddle_y,
        PADDLE_WIDTH,
        PADDLE_HEIGHT,
    )

    ball_rect = pygame.Rect(
        ball_x,
        ball_y,
        BALL_SIZE,
        BALL_SIZE,
    )

    # ----------------------------------------
    # Paddle collision
    # ----------------------------------------

    if ball_rect.colliderect(paddle_rect):
        ball_speed_y *= -1

    # ----------------------------------------
    # Brick collisions
    # ----------------------------------------

    for brick in bricks[:]:

        if ball_rect.colliderect(brick):

            bricks.remove(brick)

            score += 1

            ball_speed_y *= -1

            break

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    pygame.draw.rect(
        screen,
        PADDLE_COLOR,
        paddle_rect,
    )

    pygame.draw.rect(
        screen,
        BALL_COLOR,
        ball_rect,
    )

    for brick in bricks:

        pygame.draw.rect(
            screen,
            BRICK_COLOR,
            brick,
        )

    score_text = font.render(
        f"Score: {score}",
        True,
        (255, 255, 255),
    )

    screen.blit(score_text, (20, 20))

    if not bricks:

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
