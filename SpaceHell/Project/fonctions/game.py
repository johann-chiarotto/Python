import pygame
from .menu import Menu
from .settings import Settings
from .vaisseau import Vaisseau 
from .map import Map, font_timer, font_level_life
from .comet import Comet
from .coin import Coin
import random


class Game(Map):
    # --- constructeur ---
    def __init__(self, screen, player_name):
        self.__running = True
        self.screen = screen
        self.player_name = player_name
        self.clock = pygame.time.Clock()
        self.current_level = 1  # Niveau actuel (1 à 5)

        self.score = 0
        self.game_start_time = pygame.time.get_ticks()  # Temps de début du jeu

        # Entities
        self.vaisseau = Vaisseau(player_name)

        # --- Pause ---
        self.paused = False
        self.pause_start = 0  # moment où la pause commence
        self.total_pause_time = 0  # total de temps passé en pause

        # Init map/camera, backgrounds, etc.
        Map.__init__(self, screen)

        # Comets (une de plus à chaque niveau)
        self.all_comets = pygame.sprite.Group()
        for _ in range(10 + self.current_level):
            x = random.randint(0, 500)
            y = random.randint(-600, 0)
            comet = Comet(x, y, self.current_level)
            self.all_comets.add(comet)
            
        # Coin
        self.all_coin = pygame.sprite.Group()
        for _ in range(3):
            x = random.randint(0, 500)
            y = random.randint(-600, 0)
            coin = Coin(x, y)
            self.all_coin.add(coin)
        

    # --- GETTER ET SETTER ---
    def get_running(self):
         return self.__running
    
    def set_running(self, valeur):
        self.__running = valeur

    def set_current_level(self):
        self.current_level += 1

    # --- déplacement ---
    def handling_events(self):
        keys = pygame.key.get_pressed()

        # --- détecttion des touches ---
        if keys[pygame.K_LEFT]:
            self.vaisseau.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.vaisseau.velocity[0] = +1
        else:
            self.vaisseau.velocity[0] = 0

        if keys[pygame.K_UP]:
            self.vaisseau.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.vaisseau.velocity[1] = +1
        else:
            self.vaisseau.velocity[1] = 0

        # --- activation du déplacement du vaisseau ---
        self.vaisseau.move()
    
    
    def update(self):
        self.update_map()
        for comet in self.all_comets:
            comet.fall(self, self.current_level)
        for coin in self.all_coin:
            coin.fall_coin(self, self.current_level)
        if self.vaisseau.get_current_life() <= 0:
            # Calcul du temps total de jeu (en secondes)
            current_time = pygame.time.get_ticks()
            total_game_time = (current_time - self.game_start_time - self.total_pause_time) / 1000
            
            # Calcul du score avec bonus de temps
            # Plus le temps est court, moins le score est élevé
            time_bonus = max(0,int(total_game_time * 20))
            
            self.score = (self.current_level - 1) * 1500 + self.vaisseau.current_bonus * 250 + time_bonus
            return "game_over"
        return "continue"
    
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def display_dash_cooldown(self):
        """Affiche l'indicateur de cooldown du dash"""
        cooldown_remaining = self.vaisseau.get_dash_cooldown_remaining()
        
        if cooldown_remaining > 0:
            # Calcul du pourcentage de cooldown restant
            cooldown_percent = cooldown_remaining / self.vaisseau.dash_cooldown_ms
            
            # Affichage du texte de cooldown
            cooldown_text = font_level_life.render("Dash reload", True, (255, 100, 100))
            self.screen.blit(cooldown_text, (10, 60))
            
            # Barre de cooldown
            bar_width = 200
            bar_height = 20
            bar_x = 10
            bar_y = 100
            
            # Fond de la barre (rouge)
            pygame.draw.rect(self.screen, (100, 0, 0), (bar_x, bar_y, bar_width, bar_height))
            
            # Barre de progression (vert)
            progress_width = int(bar_width * (1 - cooldown_percent))
            pygame.draw.rect(self.screen, (0, 255, 0), (bar_x, bar_y, progress_width, bar_height))
            
            # Bordure de la barre
            pygame.draw.rect(self.screen, (255, 255, 255), (bar_x, bar_y, bar_width, bar_height), 2)
        else:
            # Dash disponible
            dash_text = font_level_life.render("Dash: Pret!", True, (100, 255, 100))
            self.screen.blit(dash_text, (10, 60))
    
    def display_game_over(self):
        """Affiche l'écran de fin de jeu"""
        # Fond sombre transparent
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))
        
        # Texte "GAME OVER"
        game_over_text = font_timer.render("GAME OVER", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(250, 300))
        self.screen.blit(game_over_text, game_over_rect)
        
        # Texte d'instruction
        instruction_text = font_level_life.render("Press space to menu", True, (255, 255, 255))
        instruction_rect = instruction_text.get_rect(center=(250, 400))
        self.screen.blit(instruction_text, instruction_rect)
        
        # Affichage du score final
        score_text = font_level_life.render(f"Score: {self.score}", True, (255, 255, 0))
        score_rect = score_text.get_rect(center=(250, 450))
        self.screen.blit(score_text, score_rect)
        
        # Affichage du nom du joueur (si disponible)
        if hasattr(self, 'player_name') and self.player_name:
            player_text = font_level_life.render(f"Joueur: {self.player_name}", True, (200, 200, 200))
            player_rect = player_text.get_rect(center=(250, 500))
            self.screen.blit(player_text, player_rect)

    
    def display(self):
        self.background(self.current_level, self.vaisseau.get_current_life(), self.vaisseau.get_current_bonus())
        self.affiche_map()

        self.vaisseau.draw(self.screen)
        self.all_comets.draw(self.screen)
        self.all_coin.draw(self.screen)
        
        # Affichage du cooldown du dash
        self.display_dash_cooldown()

        # Affichage du nombre de coins (HUD)
        coins_text = font_level_life.render(f"{self.vaisseau.get_coin_count()}c", True, (255, 255, 0))
        self.screen.blit(coins_text, (380, 10))


        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        # Toggle pause
                        if not self.paused:
                            self.paused = True
                            self.pause_start = pygame.time.get_ticks()  # sauvegarde le moment de la pause
                        else:
                            self.paused = False
                            # Ajuste le timer global de Map pour ignorer la pause
                            pause_end = pygame.time.get_ticks()
                            pause_duration = pause_end - self.pause_start
                            # Map.background utilise la variable globale start_ticks du module map
                            from . import map as map_module
                            map_module.start_ticks += pause_duration
                            self.total_pause_time += pause_duration

                    if event.key == pygame.K_m and self.paused:
                        return "menu"
                    
                    if event.key == pygame.K_SPACE:
                        # Dash avec cooldown
                        if self.vaisseau.can_dash():
                            self.vaisseau.dash()

            # --- Si le jeu est en pause ---
            if self.paused:
                # On affiche le fond du jeu figé
                if self.map_layer is not None:
                    self.map_layer.draw(self.screen, self.camera_rect)
                self.affiche_life(self.screen, self.vaisseau.get_current_life())

                pause_overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
                pause_overlay.fill((0, 0, 0, 150))  # voile sombre transparent
                self.screen.blit(pause_overlay, (0, 0))

                pause_text = font_timer.render("PAUSE", True, (255, 255, 255))
                info_text = font_level_life.render("[ESC] Reprendre  |  [M] Menu", True, (180, 180, 180))
                self.screen.blit(pause_text, pause_text.get_rect(center=(250, 350)))
                self.screen.blit(info_text, info_text.get_rect(center=(250, 450)))

                pygame.display.flip()
                self.clock.tick(15)
                continue  # saute le timer et l’update

            # Jeu en cours: input, update, draw
            self.handling_events()
            update_result = self.update()
            
            # Vérifier si le jeu est terminé
            if update_result == "game_over":
                self.display_game_over()
                pygame.display.flip()
                # Attendre un appui sur une touche pour retourner au menu
                waiting_for_input = True
                while waiting_for_input:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return "quit"
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                                waiting_for_input = False
                                return "menu"
                continue
            
            self.display()

            # Petit rappel pour la pause
            back_text = font_level_life.render("[ESC] Pause", True, (200, 200, 200))
            self.screen.blit(back_text, (40, 700))

            pygame.display.flip()
            self.clock.tick(60)