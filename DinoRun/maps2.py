from math import*
from time import*
from random import*
import pygame

"""
Création de la deuxième map du jeu, correspondant au niveau 2

"""
class maps2:

    def __init__(self,screen):

        """
        Crée les objets qui apparaitront dans la « map2 » avec les paramètres
        « self », qui fait référence à l’objet lui-même, et « screen » , créé
        dans « jeu_principal » et qui définit les dimensions de la fenêtre

        Lorsque le mauvais cube est touché, autrement dit le cube piégeur, les
        deux personnages sont renvoyés au début de la map 2

        On choisi donc un nombre au hasard entre un et deux, pour déterminer
        quel cube sera le mauvais :

        """
        self.mauvais_cube = mauvais_cube = randint(1,2)

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
        self.area_mur1 = pygame.Rect((0,0,40,700))
        self.area_mur1_color = (80,70,70)

        # mur 2 de la map :
        self.area_mur2 = pygame.Rect((1260,0,40,700))
        self.area_mur2_color = (80,70,70)

        # mur 3 de la map :
        self.area_mur3 = pygame.Rect((0,0,1300,25))
        self.area_mur3_color = (80,70,70)

        # mur 4 de la map :
        self.area_mur4 = pygame.Rect((0,680,1300,25))
        self.area_mur4_color = (80,70,70)

        # mur 5 de la map :
        self.area_mur5 = pygame.Rect((0,85,1150,25))
        self.area_mur5_color = (80,70,70)

        # mur 6 de la map :
        self.area_mur6 = pygame.Rect((150,170,1300,25))
        self.area_mur6_color = (80,70,70)

        # mur 7 de la map :
        self.area_mur7 = pygame.Rect((0,255,1150,25))
        self.area_mur7_color = (80,70,70)

        # mur 8 de la map :
        self.area_mur8 = pygame.Rect((0,340,1300,25))
        self.area_mur8_color = (80,70,70)

        # mur 9 de la map :
        self.area_mur9 = pygame.Rect((0,425,1150,25))
        self.area_mur9_color = (80,70,70)

        # mur 10 de la map :
        self.area_mur10 = pygame.Rect((150,510,1300,25))
        self.area_mur10_color = (80,70,70)

        # mur 11 de la map :
        self.area_mur11 = pygame.Rect((0,595,1150,25))
        self.area_mur11_color = (80,70,70)

# cubes de sorties :

        """
        Crée les cubes qui correspondent à la sortie de la map 2

        Définit les dimensions des cubes et leur couleur

        """

        # cube de sortie 1 :
        self.area_mur_fin1 = pygame.Rect((80,300,20,20))
        self.area_mur_fin1_color = (0,0,255)

        # cube de sortie 2 :
        self.area_mur_fin2 = pygame.Rect((80,380,20,20))
        self.area_mur_fin2_color = (0,0,255)

        # remet le nombre de pièces à 0
        self.nb_piece=0

    def fond(self):

        """
        Définit la couleur du fond de la map

        """
        self.screen.fill((170,170,170))

    def update_map(self):

        """
        Réactualise l'image de la map plusieurs fois par seconde

        """
        maps2.murs(self)

    def murs(self):

        """
        Gère le cas où un personnage rentre en contact avec un des murs de la
        map
        Fait ainsi reculer ce personnage à la place qu'il occupait juste avant
        la collision

        On utilise la vélocité pour savoir quel était le dernier mouvement du
        personnage et ainsi le remettre à la bonne place avant de l'arrêter
        ( avec les : self.player.get_speed() )

        On suit le schéma suivant :

            si tel côté de tel mur de la map et tel personnage rentre en contact
            et si la vélocité du personnage est égal à 1 ou -1 (cela dépend du
            côté que touche le personnage)
            alors le personnage retourne à la place qu'il occupait avant

        """
# mur 1 :
    # haut :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur1.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur1.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 2 :
    # haut :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur2.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur2.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

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
    # haut :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur3.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur3.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

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

    # droite :
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur4.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 5 :
    # haut :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur5.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur5.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 6 :
    # haut :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur6.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur6.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
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

    # bas :
        if self.area_mur7.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur7.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

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

    # bas :
        if self.area_mur8.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur8.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

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
    # haut :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur10.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur10.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

# mur 11 :
    # haut :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[1]==1:
            self.player1.rect.move_ip(0,-self.player1.get_speed())

    # gauche :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==-1:
            self.player1.rect.move_ip(self.player1.get_speed(),0)

    # droite :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[0]==1:
            self.player1.rect.move_ip(-self.player1.get_speed(),0)

    # bas :
        if self.area_mur11.colliderect(self.player1.rect) and self.player1.velocity[1]==-1:
            self.player1.rect.move_ip(0,self.player1.get_speed())

    # haut :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[1]==1:
            self.player2.rect.move_ip(0,-self.player2.get_speed())

    # gauche :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
            self.player2.rect.move_ip(self.player2.get_speed(),0)

    # droite :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
            self.player2.rect.move_ip(-self.player2.get_speed(),0)

    # bas :
        if self.area_mur11.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
            self.player2.rect.move_ip(0,self.player2.get_speed())

    def fin_jeu(self):

        """
        Définit le moment où le niveau est terminé, c'est-à-dire lorsque
        les deux personnages ont atteint leur sortie respective

        Pour cela on regarde également si le personnage est sur la bonne
        ou s'il se trouve sur la mauvais cube / cube piégeur

        """

        if self.mauvais_cube==1:
            if self.area_mur_fin1.colliderect(self.player2.rect):
                return True
            elif self.area_mur_fin2.colliderect(self.player1.rect):
                return False

        elif self.mauvais_cube==2:
            if self.area_mur_fin2.colliderect(self.player1.rect):
                return True
            elif self.area_mur_fin1.colliderect(self.player2.rect):
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

        # mur final correspondant à la sortie :
        pygame.draw.rect(self.screen, self.area_mur_fin1_color, self.area_mur_fin1)
        pygame.draw.rect(self.screen, self.area_mur_fin2_color, self.area_mur_fin2)


