import pygame

# ----------------------------------------
# Settings
# ----------------------------------------

WIDTH = 800
HEIGHT = 600

BACKGROUND_COLOR = (100, 180, 100)

PLAYER_COLOR = (0, 120, 255)
NPC_COLOR = (255, 120, 0)
ITEM_COLOR = (255, 255, 0)

PLAYER_SIZE = 40
NPC_SIZE = 40
ITEM_SIZE = 20

PLAYER_SPEED = 5

# ----------------------------------------
# Classes
# ----------------------------------------

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            PLAYER_SIZE,
            PLAYER_SIZE,
        )


class NPC:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            NPC_SIZE,
            NPC_SIZE,
        )


class Item:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rect(self):
        return pygame.Rect(
            self.x,
            self.y,
            ITEM_SIZE,
            ITEM_SIZE,
        )

# ----------------------------------------
# Setup
# ----------------------------------------

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("12 - Pokemon World")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 48)

# ----------------------------------------
# World
# ----------------------------------------

player = Player(100, 100)

npcs = [
    NPC(400, 200),
]

items = [
    Item(200, 200),
    Item(600, 400),
    Item(500, 150),
]

score = 0

message = ""

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

    # ----------------------------------------
    # Movement
    # ----------------------------------------

    keys = pygame.key.get_pressed()

    dx = 0
    dy = 0

    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED

    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED

    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED

    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED

    player.move(dx, dy)

    # Hold spilleren på skærmen
    player.x = max(
        0,
        min(player.x, WIDTH - PLAYER_SIZE)
    )

    player.y = max(
        0,
        min(player.y, HEIGHT - PLAYER_SIZE)
    )

    player_rect = player.rect()

    # ----------------------------------------
    # NPC Collision
    # ----------------------------------------

    message = ""

    for npc in npcs:

        if player_rect.colliderect(npc.rect()):
            message = "Hej træner!"

    # ----------------------------------------
    # Item Collection
    # ----------------------------------------

    for item in items[:]:

        if player_rect.colliderect(item.rect()):

            items.remove(item)

            score += 1

    # ----------------------------------------
    # Draw
    # ----------------------------------------

    screen.fill(BACKGROUND_COLOR)

    # Player
    pygame.draw.rect(
        screen,
        PLAYER_COLOR,
        player.rect(),
    )

    # NPCs
    for npc in npcs:

        pygame.draw.rect(
            screen,
            NPC_COLOR,
            npc.rect(),
        )

    # Items
    for item in items:

        pygame.draw.circle(
            screen,
            ITEM_COLOR,
            (
                item.x + ITEM_SIZE // 2,
                item.y + ITEM_SIZE // 2,
            ),
            ITEM_SIZE,
        )

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        (0, 0, 0),
    )

    screen.blit(score_text, (20, 20))

    # Message
    if message:

        text = font.render(
            message,
            True,
            (0, 0, 0),
        )

        screen.blit(
            text,
            (250, 20),
        )

    pygame.display.flip()

    clock.tick(60)

pygame.quit()