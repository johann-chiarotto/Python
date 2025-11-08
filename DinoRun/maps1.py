from math import*
from time import*
from random import*
import pygame

"""
Création de la première map du jeu, correspondant au niveau 1

"""
class maps1:

    def __init__(self,screen):

        """
        Crée les objets qui apparaitront dans la « map1 » avec les paramètres
        « self », qui fait référence à l’objet lui-même, et « screen » , créé
        dans « jeu_principal » et qui définit les dimensions de la fenêtre

        """
# contours de la map :

        """
        Définit les contours / limites de la fenêtre

        Définit les dimensions des côté gauche, droit ainsi que du haut et du
        bas de la map et leur couleur mais on ne les voit pas (ce qui
        est fait exprès car il s'agit juste de définir les coutours / limites
        de la map)

        """
        # côté gauche de la map :
        self.area_gauche = pygame.Rect(-5,0,5,700)
        self.area_gauche_color = (255,0,0)

        # côté droit de la map :
        self.area_droite = pygame.Rect((1300,0,5,700))
        self.area_droite_color = (255,0,0)

        # haut de la map :
        self.area_haut = pygame.Rect((0,-5,1300,5))
        self.area_haut_color = (255,0,0)

        #bas de la map :
        self.area_bas = pygame.Rect((0,700,1300,5))
        self.area_bas_color = (255,0,0)

# diférents murs de la map :

        """
        Crée les différents murs de la map

        Définit les dimensions des murs et leur couleur

        """
        # mur 1 de la map :
        self.area_mur1 = pygame.Rect((110,0,1200,40))
        self.area_mur1_color = (41,128,11)

        # mur 2 de la map :
        self.area_mur2 = pygame.Rect((110,40,500,40))
        self.area_mur2_color = (41,128,11)

        # mur 3 de la map :
        self.area_mur3 = pygame.Rect((900,40,400,40))
        self.area_mur3_color = (41,128,11)

        # mur 4 de la map :
        self.area_mur4 = pygame.Rect((0,250,50,450))
        self.area_mur4_color = (41,128,11)

        # mur 5 de la map :
        self.area_mur5 = pygame.Rect((1150,400,150,500))
        self.area_mur5_color = (41,128,11)

        # mur 6 de la map :
        self.area_mur6 = pygame.Rect((1150,200,150,70))
        self.area_mur6_color = (41,128,11)

        # mur 7 de la map :
        self.area_mur7 = pygame.Rect((190,200,300,50))
        self.area_mur7_color = (41,128,11)

        # mur 8 de la map :
        self.area_mur8 = pygame.Rect((690,200,300,50))
        self.area_mur8_color = (41,128,11)

        # mur 9 de la map :
        self.area_mur9 = pygame.Rect((190,250,800,30))
        self.area_mur9_color = (41,128,11)

        # mur 10 de la map :
        self.area_mur10 = pygame.Rect((190,250,150,300))
        self.area_mur10_color = (41,128,11)

        # mur 11 de la map :
        self.area_mur11 = pygame.Rect((800,250,190,300))
        self.area_mur11_color = (41,128,11)

        # mur 12 de la map :
        self.area_mur12 = pygame.Rect((190,550,250,50))
        self.area_mur12_color = (41,128,11)

        # mur 13 de la map :
        self.area_mur13 = pygame.Rect((600,550,390,50))
        self.area_mur13_color = (41,128,11)

# murs finals :

        """
        Crée les derniers murs qui correspondent à la sortie de la map 1

        Définit les dimensions des murs et leur couleur

        """

        # mur final 1 :
        self.area_mur_fin1 = pygame.Rect((1290,0,10,200))
        self.area_mur_fin1_color = (0,0,255)

        # mur final 2 :
        self.area_mur_fin2 = pygame.Rect((1290,250,10,200))
        self.area_mur_fin2_color = (0,0,255)

# items :

        """
        Crée les items qui apparaitront dans la map

        Importe l'image de l'item pièce et crée des rectangles correspondant
        à la position des diférentes pièces dans la map

        """
        # initialise le nombre de pièce à 0 :
        self.nb_piece = 0

        # importe l'image de l'item pièce :
        self.piece_image = pygame.image.load("piece(1).png")

        # rectangle correspondnat à la position de la pièce 1 :
        self.piece1 = pygame.Rect((200,150,15,15))

        # rectangle correspondnat à la position de la pièce 2 :
        self.piece2 = pygame.Rect((450,150,15,15))

        # rectangle correspondnat à la position de la pièce 3 :
        self.piece3 = pygame.Rect((900,150,15,15))

        # rectangle correspondnat à la position de la pièce 4 :
        self.piece4 = pygame.Rect((400,350,15,15))

        # rectangle correspondnat à la position de la pièce 5 :
        self.piece5 = pygame.Rect((600,350,15,15))

        # rectangle correspondnat à la position de la pièce 6 :
        self.piece6 = pygame.Rect((350,650,15,15))

        # rectangle correspondnat à la position de la pièce 7 :
        self.piece7 = pygame.Rect((800,650,15,15))

        # rectangle correspondnat à la position de la pièce 8 :
        self.piece8 = pygame.Rect((0,0,15,15))

    def get_piece(self):

        """
        Comptabilise le nombre de pièces ramassées par le personnage et renvoie
        ce nombre

        """
        return self.nb_piece

    def fond(self):

        """
        Définit la couleur du fond de la map

        """
        self.screen.fill((127,79,5))


    def update_map(self):

        """
        Réactualise l'image de la map plusieurs fois par seconde

        """
        maps1.murs(self)
        maps1.items(self)

    def murs(self):

        """
        Gère le cas où un personnage rentre en contact avec un des murs ou un
        des contours de la map
        Fait ainsi reculer ce personnage à la place qu'il occupait juste avant
        la collision

        On utilise la vélocité pour savoir quel était le dernier mouvement du
        personnage et ainsi le remettre à la bonne place avant de l'arrêter
        ( avec les : self.player.get_speed() )

        """
# contours de la map :

        """
        Gère le cas où un personnage rentre en contact avec un des contours de
        la map

        On suit le schéma suivant :

            si tel côté de la map et tel personnage rentre en contact
            alors le personnage retourne à la place qu'il occupait avant

        """

    # côté gauche de la map :
        if self.area_gauche.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(self.player1.get_speed(),0)

        if self.area_gauche.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # côté droit de la map :
        if self.area_droite.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

        if self.area_droite.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # haut de la map :
        if self.area_haut.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(0,self.player1.get_speed())

        if self.area_haut.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(0,self.player2.get_speed())

    # bas de la map:
        if self.area_bas.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(0,-self.player1.get_speed())

        if self.area_bas.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(0,-self.player2.get_speed())

# murs de la map :

        """
        Gère le cas où un personnage rentre en contact avec un des murs de la
        map

        On suit le schéma suivant :

            si tel côté de tel mur de la map et tel personnage rentre en contact
            et si la vélocité du personnage est égal à 1 ou -1 (cela dépend du
            côté que touche le personnage)
            alors le personnage retourne à la place qu'il occupait avant

        """

# mur 1 :
    # gauche :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # bas :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # gauche :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # bas :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 2 :
    # gauche :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # gauche :
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 3 :
    # gauche :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # gauche :
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 4 :
    # haut :
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # haut :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

# mur 5 :
    # haut :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # haut :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

# mur 6 :
    # haut :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 7 :
    # haut :
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # haut :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

# mur 8 :
    # haut :
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # haut :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

# mur 9 :
    # haut :
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur9.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur9.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 10 :
    # gauche :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # gauche :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

# mur 11 :
    # gauche :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # gauche :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

# mur 12 :
    # haut :
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur12.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur12.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 13 :
    # haut :
        if self.area_mur13.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur13.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur13.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur13.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur13.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur13.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur13.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur13.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

    def items(self):

        """
        Gère le cas où un personnage rentre en contact avec une pièce,
        c'est-à-dire lorsqu'il la ramasse

        On suit le schéma suivant :

            si la pièce n'a pas été ramassé
            on regarde s'il y a une collision entre la pièce et un des deux joueurs
            si c'est le cas alors on rajoute 1 au compte des pièces
            et la pièce devient "False" car elle a été ramassé

        """

    # pièce 1 :
        if self.piece1 != False:
            if self.piece1.colliderect(self.player1.rect) or self.piece1.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece1=False

    # pièce 2 :
        if self.piece2 !=False:
            if self.piece2.colliderect(self.player1.rect) or self.piece2.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece2=False

    # pièce 3 :
        if self.piece3 !=False:
            if self.piece3.colliderect(self.player1.rect) or self.piece3.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece3=False

    # pièce 4 :
        if self.piece4 !=False:
            if self.piece4.colliderect(self.player1.rect) or self.piece4.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece4=False

    # pièce 5 :
        if self.piece5 !=False:
            if self.piece5.colliderect(self.player1.rect) or self.piece5.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece5=False

    # pièce 6 :
        if self.piece6 !=False:
            if self.piece6.colliderect(self.player1.rect) or self.piece6.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece6=False

    # pièce 7 :
        if self.piece7 !=False:
            if self.piece7.colliderect(self.player1.rect) or self.piece7.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece7=False

    # pièce 8 :
        if self.piece8 !=False:
            if self.piece8.colliderect(self.player1.rect) or self.piece8.colliderect(self.player2.rect):
                self.nb_piece+=1
                self.piece8=False

    def fin_jeu(self):

        """
        Définit le moment où le niveau est terminé

        Le niveau est terminé lorsque le nombre de pièces collectées est
        égal à 8 et que chaque personnage est sur un des deux murs finals

        Le nombre de pièce collectées par chaque personnages importe peu,
        il suffit que toutes les pièces est étaient ramassées

        Le mur final sur le quel se trouve chque personnage importe peu,
        il suffit que chacun soit sur l'un des deux murs, mais il faut que
        chaque personnage soit sur un mur différent

        """
        if self.nb_piece == 8 and self.area_mur_fin1.colliderect(self.player1.rect) and self.area_mur_fin2.colliderect(self.player2.rect):
            return True
        if self.nb_piece == 8 and self.area_mur_fin1.colliderect(self.player2.rect) and self.area_mur_fin2.colliderect(self.player1.rect):
            return True

    def affiche_map(self):

        """
        Dessine la map avec, respectivement :

            - la fenêtre
            - la couleur des murs de la map (ou ses contours)
            - les dimensions de chaque murs de la map (ou ses contours)

        """
        # contours de la map (gauche, droit, haut et bas) :
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_gauche)
        pygame.draw.rect(self.screen, self.area_droite_color, self.area_droite)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_haut)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_bas)

        # murs finals correspondant à la sortie :
        pygame.draw.rect(self.screen, self.area_mur_fin1_color, self.area_mur_fin1)
        pygame.draw.rect(self.screen, self.area_mur_fin2_color, self.area_mur_fin2)

        # murs de la map :
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
        pygame.draw.rect(self.screen, self.area_mur13_color, self.area_mur13)

        """
        Affiche les pièces dans la map :

        Suivant le schèma :

            si tel pièce n'est pas égal à "False" c'est-à-dire qu'elle n'a
            pas été ramassée
            alors on affiche l'image de la pièce aux coordonées indiquées

        """
        if self.piece1 !=False:
            self.screen.blit(self.piece_image,(200,150))

        if self.piece2 !=False:
            self.screen.blit(self.piece_image,(450,150))

        if self.piece3 !=False:
            self.screen.blit(self.piece_image,(900,150))

        if self.piece4 !=False:
            self.screen.blit(self.piece_image,(400,350))

        if self.piece5 !=False:
            self.screen.blit(self.piece_image,(600,350))

        if self.piece6 !=False:
            self.screen.blit(self.piece_image,(350,650))

        if self.piece7 !=False:
            self.screen.blit(self.piece_image,(800,650))

        if self.piece8 !=False:
            self.screen.blit(self.piece_image,(0,0))

