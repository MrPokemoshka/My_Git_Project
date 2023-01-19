import os
import sys
import random

import pygame

size = width, height = 480, 480
FPS = 60
TILE_SIZE = 32

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Player:
    def __init__(self, position):
        self.x, self.y = position

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        center = self.x * TILE_SIZE + TILE_SIZE // 2, self.y * TILE_SIZE + TILE_SIZE // 2
        pygame.draw.rect(screen, (255, 255, 255), center, TILE_SIZE // 2)


class Game:
    def __init__(self, Player):
        self.Player = Player

    def render(self, screen):
        self.Player.render(screen)

    def update_Player(self):
        next_x, next_y = self.Player.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            next_y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            next_y += 1
#class Bomb(pygame.sprite.Sprite):  # enemy
#    image = load_image("bomb.png")
#    image_boom = load_image('boom.png')
#
#    def __init__(self, group):
#        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
#        # Это очень важно!!!
#        super().__init__(group)
#        self.image = Bomb.image
#        self.rect = self.image.get_rect()
#        self.rect.x = 200
#        self.rect.y = 200
#
#    def update(self, *args):
#        self.rect = self.rect.move(random.randrange(21) - 10,
#                                   random.randrange(21) - 10)
#        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
#                self.rect.collidepoint(args[0].pos):
#            self.image = self.image_boom


#all_sprites = pygame.sprite.Group()
#for _ in range(50):
#    Bomb(all_sprites)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #all_sprites.update(event)

    screen.fill(pygame.Color('black'))
    #all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
