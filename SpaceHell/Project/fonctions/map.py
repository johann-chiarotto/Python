from pytmx.util_pygame import load_pygame
import pyscroll
import pygame
from pathlib import Path

# Ensure font module is initialized before creating fonts
if not pygame.font.get_init():
    pygame.font.init()

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR.parent / "assets"
TMX_PATH = ASSETS_DIR / "background1.tmx"

# --- Police ---
try:
    font_timer = pygame.font.Font(str(ASSETS_DIR / "ThaleahFat.ttf"), 70)
    font_level_life = pygame.font.Font(str(ASSETS_DIR / "ThaleahFat.ttf"), 35)
except Exception:
    font_timer = pygame.font.SysFont(None, 70)
    font_level_life = pygame.font.SysFont(None, 35)

# --- Horloge ---
clock = pygame.time.Clock()

level_duration = 60    # 60 secondes pour chaque niveau sauf le niveau 6
start_ticks = pygame.time.get_ticks()

class Map:
    def __init__(self,screen):
        self.screen = screen
        # --- map / camera state ---
        # Load TMX once and keep renderer + camera
        try:
            tmx_file = TMX_PATH if TMX_PATH.exists() else (BASE_DIR / "background1.tmx")
            self.tmx_data = load_pygame(str(tmx_file))
            self.map_data = pyscroll.TiledMapData(self.tmx_data)
            self.map_layer = pyscroll.BufferedRenderer(self.map_data, self.screen.get_size())
            self.map_width = self.tmx_data.width * self.tmx_data.tilewidth
            self.map_height = self.tmx_data.height * self.tmx_data.tileheight
        except Exception:
            # Fallback values if TMX fails to load
            self.tmx_data = None
            self.map_data = None
            self.map_layer = None
            self.map_width = 500
            self.map_height = 3000

        self.camera_rect = pygame.Rect(0, 0, self.screen.get_width(), self.screen.get_height())
        self.camera_y = 0
        # Positive value scrolls downward over time (space flies by)
        self.scroll_speed = 2

        # Optional: direct PNG background to enable perfect wrap scrolling
        self.bg_image = None
        self.bg_rect = None
        try:
            img_path = ASSETS_DIR / "background1.png"
            if img_path.exists():
                self.bg_image = pygame.image.load(str(img_path)).convert()
                self.bg_rect = self.bg_image.get_rect()
        except Exception:
            self.bg_image = None
            self.bg_rect = None
        self.scroll_offset = 0
        # --- limites de l'écran ---

        # côté gauche de la map :
        self.area_gauche = pygame.Rect(-5,0,5,760)
        self.area_gauche_color = (255,0,0)

        # côté droit de la map :
        self.area_droite = pygame.Rect((500,0,5,760))
        self.area_droite_color = (255,0,0)

        # haut de la map :
        self.area_haut = pygame.Rect((0,-5,500,5))
        self.area_haut_color = (255,0,0)

        #bas de la map :
        self.area_bas = pygame.Rect((0,755,500,5))
        self.area_bas_color = (255,0,0)


    def background(self, current_level ,current_life,current_bonus):
        global start_ticks
        # --- Gestion du timer ---
        if current_level < 6:
            # Temps écoulé depuis le début du niveau
            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            remaining_seconds = max(level_duration - elapsed_seconds, 0)
            minutes = remaining_seconds // 60
            seconds = remaining_seconds % 60
            timer_str = f"{minutes:02}:{seconds:02}"
            
            # Quand le temps est écoulé, passer au niveau suivant
            if remaining_seconds == 0:
                self.set_current_level()
                start_ticks = pygame.time.get_ticks()  # reset timer pour le nouveau niveau
        else:
            #--- Timer ---
            elapsed_seconds = (pygame.time.get_ticks() - start_ticks) // 1000
            minutes = elapsed_seconds // 60
            seconds = elapsed_seconds % 60
            # Bon format d'affichage 
            timer_str = f"{minutes:02}:{seconds:02}"
            timer_text = font_timer.render(timer_str, True, (255, 255, 255))
            
        # --- background ---
        if self.bg_image is not None and self.bg_rect is not None:
            # Seamless vertical wrap using the PNG directly
            self.scroll_offset = (self.scroll_offset - self.scroll_speed) % self.bg_rect.height
            top = int(self.scroll_offset)
            view_h = self.screen.get_height()
            view_w = self.screen.get_width()

            # First slice from current offset to bottom of image
            first_h = min(view_h, self.bg_rect.height - top)
            if first_h > 0:
                src1 = pygame.Rect(0, top, view_w, first_h)
                self.screen.blit(self.bg_image, (0, 0), src1)

            # If needed, wrap from the top of the image for the remaining height
            if first_h < view_h:
                remaining = view_h - first_h
                src2 = pygame.Rect(0, 0, view_w, remaining)
                self.screen.blit(self.bg_image, (0, first_h), src2)

        elif self.map_layer is not None:
            # Scroll TMX view (non-wrapping)
            self.camera_y -= self.scroll_speed
            max_top = max(self.map_height - self.camera_rect.height, 0)
            if self.camera_y < 0:
                self.camera_y = max_top
            if self.camera_y > max_top:
                self.camera_y = max_top

            self.camera_rect.top = int(self.camera_y)
            self.screen.fill((0, 0, 0))
            self.map_layer.draw(self.screen, self.camera_rect)
        else:
            # Fallback background
            self.screen.fill((0, 0, 0))

        # Texte du niveau
        level_text = font_level_life.render(f"Level {current_level}", True, (255, 255, 255))
        self.screen.blit(level_text, (10, 15))

        # Texte du timer
        timer_text = font_timer.render(timer_str, True, (255, 255, 255))
        self.screen.blit(timer_text, (175, 0)) 

        # Barre de bonus
        self.affiche_bonus(self.screen,current_bonus)

        # Barre de vies
        self.affiche_life(self.screen,current_life)


    def affiche_life(self,screen,nb):
        try:
            life_full = pygame.image.load(str(ASSETS_DIR / "life_full.png")).convert_alpha()
            life_empty = pygame.image.load(str(ASSETS_DIR / "life_empty.png")).convert_alpha()
            for i in range(5):
                if i < nb:
                    screen.blit(life_full, (460, 15+i*20))
                else:
                    screen.blit(life_empty, (460, 15+i*20))
        except Exception:
            # Fallback: draw simple life bars
            for i in range(5):
                color = (255, 0, 0) if i < nb else (100, 100, 100)
                pygame.draw.rect(screen, color, pygame.Rect(460, 15+i*20, 24, 16))


    def affiche_bonus(self,screen,nb):
        try:
            bonus = pygame.image.load(str(ASSETS_DIR / "bonus.png")).convert_alpha()

            for i in range(nb):
                screen.blit(bonus, (420, 15+i*20))

        except Exception:
            # Fallback: draw simple bonus bars
            for i in range(5):
                color = (0, 255, 0) if i < nb else (100, 100, 100)
                pygame.draw.rect(screen, color, pygame.Rect(420, 15+i*20, 24, 16))

    def update_map(self):
        self.murs()

    def murs(self):
        # Clamp the ship fully inside the visible screen to prevent leaving bounds
        screen_rect = self.screen.get_rect()  # (0,0,500,750)
        self.vaisseau.rect.clamp_ip(screen_rect)

    def fin_jeu(self):
        pass

    def affiche_map(self):
        # contours de la map (gauche, droit, haut et bas) :
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_gauche)
        pygame.draw.rect(self.screen, self.area_droite_color, self.area_droite)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_haut)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_bas)

    