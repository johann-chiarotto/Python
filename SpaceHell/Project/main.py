import pygame
from fonctions.game import Game
from fonctions.menu import Menu
from fonctions.settings import Settings
from fonctions.sauvegarde import *


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 750))
pygame.display.set_caption("Timer avec Pygame")

pygame.mixer.music.load("assets/musique_back.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Home 
STATE_MENU = "menu"
STATE_GAME = "game"
STATE_SETTINGS = "settings"
state = STATE_MENU

menu = Menu(screen)
settings = Settings(screen)
player_name = None
game = Game(screen, player_name)
running = True

while running:
    if state == STATE_MENU:
        result = menu.run()
        if result == "quit":
            running = False
        elif result[0] == "play":
            player_name = result[1]
            game = Game(screen, player_name)
            state = STATE_GAME
        elif result[0] == "settings":
            state = STATE_SETTINGS

    elif state == STATE_GAME:
        result = game.run()
        if result == "menu":
            state = STATE_MENU
        elif result == "quit":
            running = False
            
        sauvegarde(player_name, game.score)

    elif state == STATE_SETTINGS:
        result = settings.run()
        if result == "menu":
            state = STATE_MENU

    pygame.display.flip()

pygame.mixer.music.stop()
pygame.quit()

