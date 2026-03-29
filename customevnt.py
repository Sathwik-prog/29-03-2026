import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Custom Event - Change Sprite Colors")

# Define a custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # every 2 seconds

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)

# Create sprites
sprite1 = MySprite(200, 200)
sprite2 = MySprite(400, 200)

# Group sprites
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    # Draw
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()