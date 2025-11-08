import pygame

class Settings:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font("assets/ThaleahFat.ttf", 40)

    def run(self):
        while True:
            self.screen.fill((25, 25, 35))
            text = self.font.render("Parametres (a venir)", True, (255, 255, 255))
            rect = text.get_rect(center=(250, 375))
            self.screen.blit(text, rect)

            back = self.font.render("Retour", True, (180, 180, 180))
            back_rect = back.get_rect(center=(250, 650))
            self.screen.blit(back, back_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if back_rect.collidepoint(event.pos):
                        return "menu"

            pygame.display.flip()
            