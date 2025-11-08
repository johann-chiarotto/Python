import pygame
import random
from .vaisseau import Vaisseau 

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('assets/coin.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2.5

    def fall_coin(self, game, current_level):
        self.rect.y += self.speed
        if self.rect.top > 750: 
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, 750)
            self.speed = 2.5

        if game.check_collision(self, pygame.sprite.Group(game.vaisseau)):
            game.vaisseau.recup_coin()
            self.rect.y = random.randint(-200, -60)
            self.rect.x = random.randint(0, 750)
            self.speed = 2.5