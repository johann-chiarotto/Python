# Créé par johann.chiarotto, le 20/12/2023 en Python 3.7
from math import*
from time import*
import pygame

class maps5:

    def __init__(self,screen):
        self.apparition_porte1 = True
        self.apparition_porte2 = False
        self.porte1_deja_lever = 0
        self.loquet_image = pygame.image.load("loquet.png")

#contours
        self.area_gauche = pygame.Rect(-5,0,5,700)
        self.area_gauche_color = (255,0,0)
        self.area_droite = pygame.Rect((1300,0,5,700))
        self.area_droite_color = (255,0,0)
        self.area_haut = pygame.Rect((0,-5,1300,5))
        self.area_haut_color = (255,0,0)
        self.area_bas = pygame.Rect((0,700,1300,5))
        self.area_bas_color = (255,0,0)
#murs
        self.area_mur1 = pygame.Rect((0,60,150,20))
        self.area_mur1_color = (158,223,135)
        self.area_mur2 = pygame.Rect((900,470,80,150))
        self.area_mur2_color = (158,223,135)
        self.area_mur3 = pygame.Rect((70,340,1230,20))
        self.area_mur3_color = (255,255,255)
        self.area_mur4 = pygame.Rect((1150,620,150,20))
        self.area_mur4_color = (158,223,135)
        self.area_mur5 = pygame.Rect((800,360,120,40))
        self.area_mur5_color = (158,223,135)
        self.area_mur6 = pygame.Rect((1090,490,60,150))
        self.area_mur6_color = (158,223,135)
        self.area_mur7 = pygame.Rect((80,600,150,30))
        self.area_mur7_color = (158,223,135)
        self.area_mur8 = pygame.Rect((180,630,50,70))
        self.area_mur8_color = (158,223,135)
        self.area_mur9 = pygame.Rect((350,360,120,270))
        self.area_mur9_color = (158,223,135)
        self.area_mur10 = pygame.Rect((470,360,200,80))
        self.area_mur10_color = (158,223,135)
        self.area_mur11 = pygame.Rect((550,580,250,120))
        self.area_mur11_color = (158,223,135)
        self.area_mur12 = pygame.Rect((0,345,70,10))
        self.area_mur12_color = (158,223,135)
#murs mobiles
        self.area_mur_mobile_1 = pygame.Rect((130,0,20,60))
        self.area_mur_mobile_1_color = (83,156,57)
        self.area_mur_mobile_2 = pygame.Rect((1150,360,30,260))
        self.area_mur_mobile_2_color = (83,156,57)
#loquet
        self.area_loquet1 = pygame.Rect((1270,305,15,15))
        self.area_loquet1_color = (255,0,0)
        self.area_loquet2 = pygame.Rect((1270,580,15,15))
        self.area_loquet2_color = (255,0,0)
#pièces
        self.nb_piece=0
        self.piece_image=pygame.image.load("piece(1).png")
        self.piece1 = pygame.Rect((50,100,15,15))
        self.piece2 = pygame.Rect((120,170,15,15))
        self.piece3 = pygame.Rect((350,260,15,15))
        self.piece4 = pygame.Rect((600,300,15,15))
        self.piece5 = pygame.Rect((200,30,15,15))
        self.piece6 = pygame.Rect((140,80,15,15))
        self.piece7 = pygame.Rect((650,160,15,15))
        self.piece8 = pygame.Rect((590,250,15,15))
        self.piece9 = pygame.Rect((1200,50,15,15))
        self.piece10 = pygame.Rect((1000,260,15,15))
        self.piece11 = pygame.Rect((800,300,15,15))
        self.piece12 = pygame.Rect((900,100,15,15))
        self.piece13 = pygame.Rect((750,60,15,15))
        self.piece14 = pygame.Rect((300,150,15,15))
        self.piece15 = pygame.Rect((550,30,15,15))
        self.piece16 = pygame.Rect((1100,20,15,15))
        self.piece17 = pygame.Rect((420,50,15,15))
        self.piece18 = pygame.Rect((90,290,15,15))
        self.piece19 = pygame.Rect((1150,180,15,15))
        self.piece20 = pygame.Rect((870,220,15,15))
#mur fin
        self.mur_fin = pygame.Rect((0,340,70,20))
        self.mur_fin_color = (51,121,187)

    def fond(self):
        self.screen.fill((0,0,0))


    def get_piece(self):
        return self.nb_piece


    def update_map(self):
        maps5.murs(self)
        maps5.items(self)


    def murs(self):
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

#mur1
    #haut
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur2
    #haut
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur3
    #haut
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur4
    #haut
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur5
    #haut
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur6
    #haut
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur7
    #haut
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur8
    #haut
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur9
    #haut
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur10
    #haut
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur11
    #haut
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#mur12
    #haut
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())
    #gauche
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)
    #droite
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)
    #bas
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())
    #haut
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())
    #gauche
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)
    #droite
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)
    #bas
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

#porte1
        if self.apparition_porte1==True and self.porte1_deja_lever==0:
        #haut
            if self.area_mur_mobile_1.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
                self.player1.rect.move_ip(0,-self.player1.get_speed())
        #gauche
            if self.area_mur_mobile_1.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
                self.player1.rect.move_ip(self.player1.get_speed(),0)
        #droite
            if self.area_mur_mobile_1.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
                self.player1.rect.move_ip(-self.player1.get_speed(),0)
        #bas
            if self.area_mur_mobile_1.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
                self.player1.rect.move_ip(0,self.player1.get_speed())
        #haut
            if self.area_mur_mobile_1.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
                self.player2.rect.move_ip(0,-self.player2.get_speed())
        #gauche
            if self.area_mur_mobile_1.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
                self.player2.rect.move_ip(self.player2.get_speed(),0)
        #droite
            if self.area_mur_mobile_1.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
                self.player2.rect.move_ip(-self.player2.get_speed(),0)
        #bas
            if self.area_mur_mobile_1.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
                self.player2.rect.move_ip(0,self.player2.get_speed())

#porte2
        if self.apparition_porte2==True and self.porte1_deja_lever==0:
        #haut
            if self.area_mur_mobile_2.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
                self.player1.rect.move_ip(0,-self.player1.get_speed())
        #gauche
            if self.area_mur_mobile_2.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
                self.player1.rect.move_ip(self.player1.get_speed(),0)
        #droite
            if self.area_mur_mobile_2.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
                self.player1.rect.move_ip(-self.player1.get_speed(),0)
        #bas
            if self.area_mur_mobile_2.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
                self.player1.rect.move_ip(0,self.player1.get_speed())
        #haut
            if self.area_mur_mobile_2.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
                self.player2.rect.move_ip(0,-self.player2.get_speed())
        #gauche
            if self.area_mur_mobile_2.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
                self.player2.rect.move_ip(self.player2.get_speed(),0)
        #droite
            if self.area_mur_mobile_2.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
                self.player2.rect.move_ip(-self.player2.get_speed(),0)
        #bas
            if self.area_mur_mobile_2.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
                self.player2.rect.move_ip(0,self.player2.get_speed())

#loquet1
        if self.area_loquet1.colliderect(self.player2.rect) and self.porte1_deja_lever==0:
            self.apparition_porte1 = True
            self.apparition_porte2 = False
            self.porte1_deja_lever += 1
#loquet2
        if self.area_loquet2.colliderect(self.player1.rect) and self.porte1_deja_lever==0:
            self.apparition_porte2 = True
            self.apparition_porte1 = False


    def items(self):
        #piece 1
        if self.piece1 !=False:
            if self.piece1.colliderect(self.player1.rect) or self.piece1.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece1=False
        #piece 2
        if self.piece2 !=False:
            if self.piece2.colliderect(self.player1.rect) or self.piece2.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece2=False
        #piece 3
        if self.piece3 !=False:
            if self.piece3.colliderect(self.player1.rect) or self.piece3.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece3=False
        #piece 4
        if self.piece4 !=False:
            if self.piece4.colliderect(self.player1.rect) or self.piece4.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece4=False
        #piece 5
        if self.piece5 !=False:
            if self.piece5.colliderect(self.player1.rect) or self.piece5.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece5=False
        #piece 6
        if self.piece6 !=False:
            if self.piece6.colliderect(self.player1.rect) or self.piece6.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece6=False
        #piece 7
        if self.piece7 !=False:
            if self.piece7.colliderect(self.player1.rect) or self.piece7.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece7=False
        #piece 8
        if self.piece8 !=False:
            if self.piece8.colliderect(self.player1.rect) or self.piece8.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece8=False
        #piece 9
        if self.piece9 !=False:
            if self.piece9.colliderect(self.player1.rect) or self.piece9.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece9=False
        #piece 10
        if self.piece10 !=False:
            if self.piece10.colliderect(self.player1.rect) or self.piece10.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece10=False
        #piece 11
        if self.piece11 !=False:
            if self.piece11.colliderect(self.player1.rect) or self.piece11.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece11=False
        #piece 12
        if self.piece12 !=False:
            if self.piece12.colliderect(self.player1.rect) or self.piece12.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece12=False
        #piece 13
        if self.piece13 !=False:
            if self.piece13.colliderect(self.player1.rect) or self.piece13.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece13=False
        #piece 14
        if self.piece14 !=False:
            if self.piece14.colliderect(self.player1.rect) or self.piece14.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece14=False
        #piece 15
        if self.piece15 !=False:
            if self.piece15.colliderect(self.player1.rect) or self.piece15.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece15=False
        #piece 16
        if self.piece16 !=False:
            if self.piece16.colliderect(self.player1.rect) or self.piece16.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece16=False
        #piece 17
        if self.piece17 !=False:
            if self.piece17.colliderect(self.player1.rect) or self.piece17.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece17=False
        #piece 18
        if self.piece18 !=False:
            if self.piece18.colliderect(self.player1.rect) or self.piece18.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece18=False
        #piece 19
        if self.piece19 !=False:
            if self.piece19.colliderect(self.player1.rect) or self.piece19.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece19=False
        #piece 20
        if self.piece20 !=False:
            if self.piece20.colliderect(self.player1.rect) or self.piece20.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece20=False


    def fin_jeu(self):
        if self.nb_piece == 20 and self.mur_fin.colliderect(self.player1.rect) and self.mur_fin.colliderect(self.player2.rect):
            return True


    def affiche_map(self):
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_gauche)
        pygame.draw.rect(self.screen, self.area_droite_color, self.area_droite)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_haut)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_bas)

        pygame.draw.rect(self.screen, self.area_mur1_color, self.area_mur1)
        pygame.draw.rect(self.screen, self.area_mur2_color, self.area_mur2)
        pygame.draw.rect(self.screen, self.area_mur3_color, self.area_mur3)
        pygame.draw.rect(self.screen, self.area_mur4_color, self.area_mur4)
        pygame.draw.rect(self.screen, self.area_mur5_color, self.area_mur5)
        pygame.draw.rect(self.screen, self.area_mur6_color, self.area_mur6)
        pygame.draw.rect(self.screen, self.area_mur7_color, self.area_mur7)
        pygame.draw.rect(self.screen, self.area_mur8_color, self.area_mur8)
        pygame.draw.rect(self.screen, self.area_mur9_color, self.area_mur9)
        pygame.draw.rect(self.screen, self.area_mur10_color, self.area_mur10)
        pygame.draw.rect(self.screen, self.area_mur11_color, self.area_mur11)
        pygame.draw.rect(self.screen, self.area_mur12_color, self.area_mur12)
        pygame.draw.rect(self.screen, self.mur_fin_color, self.mur_fin)

        if self.apparition_porte1 == True and self.porte1_deja_lever==0:
            pygame.draw.rect(self.screen, self.area_mur_mobile_1_color, self.area_mur_mobile_1)     #celui la il marche pas et ca me casse les couilles
            pygame.draw.rect(self.screen, self.area_loquet2_color, self.area_loquet2)
            self.screen.blit(self.loquet_image,(1270,580))
        if self.apparition_porte2 == True and self.porte1_deja_lever==0:
            pygame.draw.rect(self.screen, self.area_mur_mobile_2_color, self.area_mur_mobile_2)
            if self.nb_piece == 20:
                pygame.draw.rect(self.screen, self.area_loquet1_color, self.area_loquet1)
                self.screen.blit(self.loquet_image,(1270,305))

        if self.piece1 !=False:
            self.screen.blit(self.piece_image,(50,100))
        if self.piece2 !=False:
            self.screen.blit(self.piece_image,(120,170))
        if self.piece3 !=False:
            self.screen.blit(self.piece_image,(350,260))
        if self.piece4 !=False:
            self.screen.blit(self.piece_image,(600,300))
        if self.piece5 !=False:
            self.screen.blit(self.piece_image,(200,30))
        if self.piece6 !=False:
            self.screen.blit(self.piece_image,(140,80))
        if self.piece7 !=False:
            self.screen.blit(self.piece_image,(650,160))
        if self.piece8 !=False:
            self.screen.blit(self.piece_image,(590,250))
        if self.piece9 !=False:
            self.screen.blit(self.piece_image,(1200,50))
        if self.piece10 !=False:
            self.screen.blit(self.piece_image,(1000,260))
        if self.piece11 !=False:
            self.screen.blit(self.piece_image,(800,300))
        if self.piece12 !=False:
            self.screen.blit(self.piece_image,(900,100))
        if self.piece13 !=False:
            self.screen.blit(self.piece_image,(750,60))
        if self.piece14 !=False:
            self.screen.blit(self.piece_image,(300,150))
        if self.piece15 !=False:
            self.screen.blit(self.piece_image,(550,30))
        if self.piece16 !=False:
            self.screen.blit(self.piece_image,(1100,20))
        if self.piece17 !=False:
            self.screen.blit(self.piece_image,(420,50))
        if self.piece18 !=False:
            self.screen.blit(self.piece_image,(90,290))
        if self.piece19 !=False:
            self.screen.blit(self.piece_image,(1150,180))
        if self.piece20 !=False:
            self.screen.blit(self.piece_image,(870,220))
