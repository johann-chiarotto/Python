import pygame
import random
from .vaisseau import Vaisseau

class Comet(pygame.sprite.Sprite):
    def __init__(self, x, y, current_level):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

        #  Vitesse verticale — accélération forte selon le niveau
        # (croît de façon exponentielle pour bien sentir la différence)
        self.speed_y = 3 + (current_level ** 1.6)

        #  Vitesse horizontale légère dérive
        self.speed_x = random.uniform(-1.0, 1.0) * (1 + current_level * 0.05)

    def fall(self, game, current_level):
        # mouvement diagonal léger
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        #  rebond sur les bords gauche/droite
        if self.rect.left <= 0:
            self.rect.left = 0
            self.speed_x = abs(self.speed_x)  # repart vers la droite
        elif self.rect.right >= 750:
            self.rect.right = 750
            self.speed_x = -abs(self.speed_x)  # repart vers la gauche

        #  repositionnement en haut
        if self.rect.top > 750:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, 750)
            # recalcul de la vitesse avec augmentation par niveau
            self.speed_y = 3 + (current_level ** 1.6)
            self.speed_x = random.uniform(-1.0, 1.0) * (1 + current_level * 0.05)

        # collision avec le vaisseau
        if game.check_collision(self, pygame.sprite.Group(game.vaisseau)):
            game.vaisseau.set_life()
