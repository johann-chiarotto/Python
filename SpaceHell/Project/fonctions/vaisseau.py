import pygame 
from pathlib import Path

class Vaisseau(pygame.sprite.Sprite):
    # --- constructeur --- 
    def __init__(self, nom):
        super().__init__()
        self.vies = 5
        self.current_bonus = 0     # Nombre de bonnus (0 à 5)
        self.__speed=3
        self.velocity = [0,0]
        self.coin = 0

        try:
            assets_dir = Path(__file__).resolve().parent.parent / "assets"
            self.__image = pygame.image.load(str(assets_dir / "vaisseau.png")).convert_alpha()
        except Exception:
            self.__image = pygame.Surface((32, 32), pygame.SRCALPHA)
            self.__image.fill((200, 200, 255, 255))
        self.rect = self.__image.get_rect(x=235,y=600)
        self.mask = pygame.mask.from_surface(self.__image) 

        # Invincibility window after a hit to avoid losing multiple lives in one contact
        self.invincibility_ms = 800
        self.last_hit_ms = -self.invincibility_ms
        
        # Dash system with cooldown
        self.dash_cooldown_ms = 500  # 0.5 seconds
        self.last_dash_ms = -self.dash_cooldown_ms
        self.is_dashing = False
        self.dash_distance = 75  # Distance du dash en pixels


    # --- fonction de déplacement du vaisseau ---
    def move(self):
        self.rect.move_ip(self.velocity[0]*self.get_speed(), self.velocity[1]*self.get_speed())

    def draw(self, screen):
        screen.blit(self.__image,self.rect)


    # --- GETTER ET SETTER ---
    def get_speed(self):
        return self.__speed
    
    def set_life(self):
        now = pygame.time.get_ticks()
        if now - self.last_hit_ms >= self.invincibility_ms and self.vies > 0:
            self.vies -= 1
            self.last_hit_ms = now

    def set_speed(self, speed):
        self.__speed = speed
    
    def get_image(self):
        return self.__image
    
    def get_current_life(self):
        return self.vies
    
    def get_current_bonus(self):
        return self.current_bonus
    
    def can_dash(self):
        """Vérifie si le dash est disponible (cooldown terminé)"""
        now = pygame.time.get_ticks()
        return now - self.last_dash_ms >= self.dash_cooldown_ms
    
    def dash(self):
        """Active le dash si le cooldown est terminé"""
        if self.can_dash():
            self.last_dash_ms = pygame.time.get_ticks()
            self.is_dashing = True
            
            # Calcul de la direction du dash basée sur la vélocité actuelle
            dash_x = 0
            dash_y = 0
            
            if self.velocity[0] != 0:  # Mouvement horizontal
                dash_x = self.velocity[0] * self.dash_distance
            if self.velocity[1] != 0:  # Mouvement vertical
                dash_y = self.velocity[1] * self.dash_distance
            
            # Si aucune direction n'est pressée, dash vers le haut par défaut
            if dash_x == 0 and dash_y == 0:
                dash_y = -self.dash_distance
            
            # Appliquer le dash
            self.rect.move_ip(dash_x, dash_y)
            
            # S'assurer que le vaisseau reste dans les limites de l'écran
            screen_width = 500  # Largeur de l'écran
            screen_height = 750  # Hauteur de l'écran
            
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > screen_width:
                self.rect.right = screen_width
                
            if self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > screen_height:
                self.rect.bottom = screen_height
            
            return True
        return False
    
    def get_dash_cooldown_remaining(self):
        """Retourne le temps restant avant le prochain dash en millisecondes"""
        now = pygame.time.get_ticks()
        remaining = self.dash_cooldown_ms - (now - self.last_dash_ms)
        return max(0, remaining)
    

    def recup_coin(self):
        self.coin += 1

    def get_coin_count(self):
        return self.coin


