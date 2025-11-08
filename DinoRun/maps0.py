# Créé par chiar, le 24/12/2023 en Python 3.7
import pygame

class maps0:

    def __init__(self,screen):
#contours
        self.area_gauche = pygame.Rect(-5,0,5,700)
        self.area_gauche_color = (255,0,0)
        self.area_droite = pygame.Rect((1300,0,5,700))
        self.area_droite_color = (255,0,0)
        self.area_haut = pygame.Rect((0,-5,1300,5))
        self.area_haut_color = (255,0,0)
        self.area_bas = pygame.Rect((0,700,1300,5))
        self.area_bas_color = (255,0,0)
#emplacement maps
        self.area_maps1 = pygame.Rect(100,20,200,107)
        self.area_maps1_color = (255,0,0)
        self.area_maps2 = pygame.Rect(550,20,200,107)
        self.area_maps2_color = (255,0,0)
        self.area_maps3 = pygame.Rect(1000,20,200,107)
        self.area_maps3_color = (255,0,0)
        self.area_maps4 = pygame.Rect(1000,572,200,107)
        self.area_maps4_color = (255,0,0)
        self.area_maps5 = pygame.Rect(550,572,200,107)
        self.area_maps5_color = (255,0,0)
        self.area_maps6 = pygame.Rect(100,572,200,107)
        self.area_maps6_color = (255,0,0)
#mur fin
        self.area_mur_fin = pygame.Rect(1260,300,40,100)
        self.area_mur_fin_color = (0,0,255)

#image des maps
        self.image_maps1 = pygame.image.load("maps1_image.jpg")


    def fond(self):
        self.screen.fill((0,0,0))


    def get_piece(self):
        pass


    def update_map(self):
    #coter gauche
        if self.area_gauche.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(self.player1.get_speed(),0)

        if self.area_gauche.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #coter droite
        if self.area_droite.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

        if self.area_droite.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #haut
        if self.area_haut.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(0,self.player1.get_speed())

        if self.area_haut.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(0,self.player2.get_speed())
    #bas
        if self.area_bas.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(0,-self.player1.get_speed())

        if self.area_bas.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(0,-self.player2.get_speed())


    def fin_jeu(self):
        if self.area_maps1.colliderect(self.player1.rect) or self.area_maps1.colliderect(self.player2.rect):
            return 1
        if self.area_maps2.colliderect(self.player1.rect) or self.area_maps2.colliderect(self.player2.rect):
            return 2
        if self.area_maps3.colliderect(self.player1.rect) or self.area_maps3.colliderect(self.player2.rect):
            return 3
        if self.area_maps4.colliderect(self.player1.rect) or self.area_maps4.colliderect(self.player2.rect):
            return 4
        if self.area_maps5.colliderect(self.player1.rect) or self.area_maps5.colliderect(self.player2.rect):
            return 5
        if self.area_maps6.colliderect(self.player1.rect) or self.area_maps6.colliderect(self.player2.rect):
            return 6
        if self.area_mur_fin.colliderect(self.player1.rect) or self.area_mur_fin.colliderect(self.player2.rect):
            return False


    def affiche_map(self):
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_gauche)
        pygame.draw.rect(self.screen, self.area_droite_color, self.area_droite)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_haut)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_bas)

        pygame.draw.rect(self.screen, self.area_maps1_color, self.area_maps1)
        pygame.draw.rect(self.screen, self.area_maps2_color, self.area_maps2)
        pygame.draw.rect(self.screen, self.area_maps3_color, self.area_maps3)
        pygame.draw.rect(self.screen, self.area_maps4_color, self.area_maps4)
        pygame.draw.rect(self.screen, self.area_maps5_color, self.area_maps5)
        pygame.draw.rect(self.screen, self.area_maps6_color, self.area_maps6)
        pygame.draw.rect(self.screen, self.area_mur_fin_color, self.area_mur_fin)

        if self.area_maps1 !=False:
            self.screen.blit(self.image_maps1,(100,20))
