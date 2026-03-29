import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Color")

# Custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)  # Trigger every 1 second

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        # Change to a random color
        self.color = (random.randint(0,255),
                      random.randint(0,255),
                      random.randint(0,255))
        self.image.fill(self.color)

# Create two sprites
sprite1 = MySprite(100, 150, (255, 0, 0))  # Red
sprite2 = MySprite(300, 150, (0, 0, 255))  # Blue

# Group sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event handling
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    # Draw
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()