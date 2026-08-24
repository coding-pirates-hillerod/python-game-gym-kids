import random
import pygame

pygame.init()

# Vindue
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect Star")

clock = pygame.time.Clock()

# Spiller
player_x = 100
player_y = 100

player_size = 50
player_speed = 5

player_color = (0, 100, 255)

# Stjerne
star_x = 500
star_y = 300

star_size = 30

star_color = (255, 255, 0)

running = True

while running:
    # Luk spillet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tastatur
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    if keys[pygame.K_UP]:
        player_y -= player_speed

    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Kollision
    player_rect = pygame.Rect(
        player_x,
        player_y,
        player_size,
        player_size,
    )

    star_rect = pygame.Rect(
        star_x,
        star_y,
        star_size,
        star_size,
    )

    if player_rect.colliderect(star_rect):
        star_x = random.randint(50, WIDTH - 50)
        star_y = random.randint(50, HEIGHT - 50)

    # Tegn
    screen.fill((30, 30, 30))

    pygame.draw.rect(
        screen,
        player_color,
        (
            player_x,
            player_y,
            player_size,
            player_size,
        ),
    )

    pygame.draw.circle(
        screen,
        star_color,
        (star_x, star_y),
        star_size,
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()