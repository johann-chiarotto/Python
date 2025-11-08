from math import*
from time import*
from random import*
import pygame

"""
Création de la troisième map du jeu, correspondant au niveau 3

"""
class maps3:

    def __init__(self,screen):

        """
        Crée les objets qui apparaitront dans la « map3 » avec les paramètres
        « self », qui fait référence à l’objet lui-même, et « screen » , créé
        dans « jeu_principal » et qui définit les dimensions de la fenêtre

        On initialise également la variable mort à 0 :

        """
        self.mort=0

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

        # bas de la map :
        self.area_bas = pygame.Rect((0,700,1300,5))
        self.area_bas_color = (255,0,0)

# diférents murs de la map :

        """
        Crée les différents murs de la map

        Définit les dimensions des murs et leur couleur

        """
        # mur 1 de la map :
        self.area_mur1 = pygame.Rect((100,0,90,350))
        self.area_mur1_color = (80,70,70)

        # mur 2 de la map :
        self.area_mur2 = pygame.Rect((100,200,250,200))
        self.area_mur2_color = (80,70,70)

        # mur 3 de la map :
        self.area_mur3 = pygame.Rect((260,70,90,200))
        self.area_mur3_color = (80,70,70)

        # mur 4 de la map :
        self.area_mur4 = pygame.Rect((100,500,1100,110))
        self.area_mur4_color = (80,70,70)

        # mur 5 de la map :
        self.area_mur5 = pygame.Rect((580,70,150,500))
        self.area_mur5_color = (80,70,70)

        # mur 6 de la map :
        self.area_mur6 = pygame.Rect((800,70,600,50))
        self.area_mur6_color = (80,70,70)

        # mur 7 de la map :
        self.area_mur7 = pygame.Rect((600,120,600,80))
        self.area_mur7_color = (80,70,70)

        # mur 8 de la map :
        self.area_mur8 = pygame.Rect((1100,120,100,320))
        self.area_mur8_color = (80,70,70)

        # mur 9 de la map :
        self.area_mur9 = pygame.Rect((800,370,400,70))
        self.area_mur9_color = (80,70,70)

        # mur 10 de la map :
        self.area_mur10 = pygame.Rect((800,260,30,130))
        self.area_mur10_color = (80,70,70)

        # mur 11 de la map :
        self.area_mur11 = pygame.Rect((800,260,240,50))
        self.area_mur11_color = (80,70,70)

# cubes de sorties :

        """
        Crée les cubes qui correspondent à la sortie de la map 2

        Définit les dimensions des cubes et leur couleur

        """

        # cube de sortie 1 :
        self.area_mur_fin1 = pygame.Rect((1280,10,10,10))
        self.area_mur_fin1_color = (0,0,255)

        # cube de sortie 2 :
        self.area_mur_fin2 = pygame.Rect((1280,680,10,10))
        self.area_mur_fin2_color = (0,0,255)

# items :

        """
        Crée les items qui apparaitront dans la map

        Importe l'image de l'item pièce et crée des rectangles correspondant
        à la position des diférentes pièces dans la map

        """
        # initialise le nombre de pièce à 0 :
        self.nb_piece=0

        # importe l'image de l'item pièce :
        self.piece_image=pygame.image.load("piece(1).png")

        # rectangle correspondnat à la position de la pièce 1 :
        self.piece1 = pygame.Rect((10,10,15,15))

        # rectangle correspondnat à la position de la pièce 2 :
        self.piece2 = pygame.Rect((450,150,15,15))

        # rectangle correspondnat à la position de la pièce 3 :
        self.piece3 = pygame.Rect((840,325,15,15))

        # rectangle correspondnat à la position de la pièce 4 :
        self.piece4 = pygame.Rect((750,95,15,15))

        # rectangle correspondnat à la position de la pièce 5 :
        self.piece5 = pygame.Rect((1240,150,15,15))

        # rectangle correspondnat à la position de la pièce 6 :
        self.piece6 = pygame.Rect((400,650,15,15))

        # rectangle correspondnat à la position de la pièce 7 :
        self.piece7 = pygame.Rect((220,150,15,15))

        # rectangle correspondnat à la position de la pièce 8 :
        self.piece8 = pygame.Rect((900,650,15,15))

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
        self.screen.fill((170,170,170))


    def update_map(self):

        """
        Réactualise l'image de la map plusieurs fois par seconde

        """
        maps3.murs(self)
        maps3.items(self)


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

    # bas de la map :
        if self.area_bas.colliderect(self.player1.rect) :
            self.player1.rect.move_ip(0,-self.player1.get_speed())

        if self.area_bas.colliderect(self.player2.rect) :
            self.player2.rect.move_ip(0,-self.player2.get_speed())

# murs de la map :

        """
        Gère le cas où un personnage rentre en contact avec un des murs de la
        map

        On suit le schèma suivant :

            si tel mur de la map et un personnage rentre en contact ou si le
            même mur rentre en contact avec le second personnage
            alors on ajoute 1 à "self.mort"

        Ce qui signifie que le personnage meurt s'il touche l'un des murs

        """

        if self.area_mur1.colliderect(self.player1.rect) or self.area_mur1.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur2.colliderect(self.player1.rect) or self.area_mur2.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur3.colliderect(self.player1.rect) or self.area_mur3.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur4.colliderect(self.player1.rect) or self.area_mur4.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur5.colliderect(self.player1.rect) or self.area_mur5.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur6.colliderect(self.player1.rect) or self.area_mur6.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur7.colliderect(self.player1.rect) or self.area_mur7.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur8.colliderect(self.player1.rect) or self.area_mur8.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur9.colliderect(self.player1.rect) or self.area_mur9.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur10.colliderect(self.player1.rect) or self.area_mur10.colliderect(self.player2.rect):
            self.mort+=1
        if self.area_mur11.colliderect(self.player1.rect) or self.area_mur11.colliderect(self.player2.rect):
            self.mort+=1

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
        if self.piece1 !=False:
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

    def __mort(self):

        """
        Gère le cas où un personnage rentre en contact avec un mur, ainsi il
        meurt et le niveau recommence

        """
        if self.area_mur1.colliderect(self.player1.rect) or self.area_mur2.colliderect(self.player1.rect) or self.area_mur3.colliderect(self.player1.rect) or self.area_mur4.colliderect(self.player1.rect) or self.area_mur5.colliderect(self.player1.rect) or self.area_mur6.colliderect(self.player1.rect) or self.area_mur7.colliderect(self.player1.rect) or self.area_mur8.colliderect(self.player1.rect) or self.area_mur9.colliderect(self.player1.rect) or self.area_mur10.colliderect(self.player1.rect) or self.area_mur11.colliderect(self.player1.rect):
            maps3.__init__(self,pygame.display.set_mode((1300,700)))
            return True
        if self.area_mur1.colliderect(self.player2.rect) or self.area_mur2.colliderect(self.player2.rect) or self.area_mur3.colliderect(self.player2.rect) or self.area_mur4.colliderect(self.player2.rect) or self.area_mur5.colliderect(self.player2.rect) or self.area_mur6.colliderect(self.player2.rect) or self.area_mur7.colliderect(self.player2.rect) or self.area_mur8.colliderect(self.player2.rect) or self.area_mur9.colliderect(self.player2.rect) or self.area_mur10.colliderect(self.player2.rect) or self.area_mur11.colliderect(self.player2.rect):
            maps3.__init__(self,pygame.display.set_mode((1300,700)))
            return True


    def fin_jeu(self):

        """
        Définit le moment où le niveau est terminé

        Le niveau est terminé lorsque toute les pièces ont été ramassées
        et lorsque les deux personnages ont atteint leur sortie respective

        """

        if maps3.__mort(self)==True:
            return True
        elif self.nb_piece==8 and self.area_mur_fin1.colliderect(self.player1.rect) and self.area_mur_fin2.colliderect(self.player2.rect):
            return False
        elif self.nb_piece==8 and self.area_mur_fin1.colliderect(self.player2.rect) and self.area_mur_fin2.colliderect(self.player1.rect):
            return False

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

        # cubes de sortie :
        pygame.draw.rect(self.screen, self.area_mur_fin1_color, self.area_mur_fin1)
        pygame.draw.rect(self.screen, self.area_mur_fin2_color, self.area_mur_fin2)


        """
        Affiche les pièces dans la map :

        Suivant le schèma :

            si tel pièce n'est pas égal à "False" c'est-à-dire qu'elle n'a
            pas été ramassée
            alors on affiche l'image de la pièce aux coordonées indiquées

        """
        if self.piece1 !=False:
            self.screen.blit(self.piece_image,(10,10))

        if self.piece2 !=False:
            self.screen.blit(self.piece_image,(450,150))

        if self.piece3 !=False:
            self.screen.blit(self.piece_image,(840,325))

        if self.piece4 !=False:
            self.screen.blit(self.piece_image,(750,95))

        if self.piece5 !=False:
            self.screen.blit(self.piece_image,(1240,150))

        if self.piece6 !=False:
            self.screen.blit(self.piece_image,(400,650))

        if self.piece7 !=False:
            self.screen.blit(self.piece_image,(220,150))

        if self.piece8 !=False:
            self.screen.blit(self.piece_image,(900,650))
