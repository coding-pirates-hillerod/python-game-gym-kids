import pygame

pygame.init()

# Vindue
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Move Square")

# Spiller
player_x = 100
player_y = 100

player_size = 50

player_speed = 5

player_color = (0, 100, 255)

clock = pygame.time.Clock()

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

    # Tegn
    screen.fill((30, 30, 30))

    pygame.draw.rect(
        screen,
        player_color,
        (player_x, player_y, player_size, player_size),
    )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()