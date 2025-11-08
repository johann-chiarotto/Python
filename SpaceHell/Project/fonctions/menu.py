import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font("assets/ThaleahFat.ttf", 80)
        self.font_button = pygame.font.Font("assets/ThaleahFat.ttf", 40)
        self.font_small = pygame.font.Font("assets/ThaleahFat.ttf", 25)
        self.font_input = pygame.font.Font("assets/ThaleahFat.ttf", 50)

        self.play_rect = None
        self.settings_rect = None
        self.first_time = True  #  pour demander le pseudo une fois
        self.player_name = ""   #  pseudo du joueur

    def draw_text(self, text, font, color, center):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=center)
        self.screen.blit(surf, rect)
        return rect

    def run(self):
        asking_name = False  #  état d'entrée du pseudo
        while True:
            self.screen.fill((20, 20, 30))

            # --- Titre ---
            self.draw_text("Space Hell", self.font_title, (255, 80, 80), (250, 150))

            # --- Bouton Play ---
            self.play_rect = self.draw_text("Play", self.font_button, (255, 255, 255), (250, 375))

            # --- Bouton Paramètres ---
            self.settings_rect = self.draw_text("⚙", self.font_small, (200, 200, 200), (30, 30))

            # --- Si on est en train de demander le pseudo ---
            if asking_name:
                self.screen.fill((20, 20, 30))
                self.draw_text("Enter Name (max 4 chars):", self.font_button, (255,255,255), (250, 300))
                self.draw_text(self.player_name, self.font_input, (255, 255, 0), (250, 400))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if asking_name:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and len(self.player_name) > 0:
                            # pseudo valide -> lancer le jeu
                            asking_name = False
                            self.first_time = False
                            return "play", self.player_name
                        elif event.key == pygame.K_BACKSPACE:
                            self.player_name = self.player_name[:-1]
                        else:
                            if len(self.player_name) < 4:
                                if event.unicode.isalnum():
                                    self.player_name += event.unicode.upper()
                    continue  #  on ne gère pas les boutons pendant la saisie

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.play_rect.collidepoint(event.pos):
                        if self.first_time:
                            asking_name = True
                            self.player_name = ""
                        else:
                            return "play", self.player_name
                    if self.settings_rect.collidepoint(event.pos):
                        return "settings", None