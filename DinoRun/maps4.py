from math import*
from time import*
from random import*
import pygame

"""
Création de la quatrième map du jeu, correspondant au niveau 4

Dans cette map les quatre murs créés constituent une prison pour le personnage
qui se retrouve piégé entre eux au début de la partie

"""
class maps4:

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

        #côté droit de la map :
        self.area_droite = pygame.Rect((1300,0,5,700))
        self.area_droite_color = (255,0,0)

        # haut de la map :
        self.area_haut = pygame.Rect((0,-700,1300,700))
        self.area_haut_color = (255,0,0)

        # bas de la map :
        self.area_bas = pygame.Rect((0,700,1300,700))
        self.area_bas_color = (255,0,0)

# diférents murs de la map :

        """
        Crée les différents murs de la map

        Définit les dimensions des murs et leur couleur

        """
        # mur 1 de la map :
        self.area_mur1 = pygame.Rect((495,290,10,70))
        self.area_mur1_color = (41,128,11)

        # mur 2 de la map :
        self.area_mur2 = pygame.Rect((495,290,320,10))
        self.area_mur2_color = (41,128,11)

        # mur 3 de la map :
        self.area_mur3 = pygame.Rect((815,290,10,70))
        self.area_mur3_color = (41,128,11)

        # mur 4 de la map :
        self.area_mur4 = pygame.Rect((495,360,330,10))
        self.area_mur4_color = (41,128,11)

        """
        Création d'un mur qui représente de la lave et donc une menace pour les
        personnages
        (son fonctionnement est expliqué plus tard dans le programme) :

        """
        # initialise la vitesse du mur à 1 :
        self.vitesse_mur = 1

        # initialise la direction du mur à 1 :
        self.direction = 1

        """
        Création de deux boutons qui permettront à l'un des deux personnages de
        changer l'avancement du mur de lave créé auparavant :

        """
        # donne la position du premier bouton et sa couleur :
        self.bouton_up = pygame.Rect(520,320,15,20)
        self.bouton_up_image = pygame.image.load("haut.png")

        # donne la position du second bouton et sa couleur :
        self.bouton_down = pygame.Rect(785,320,15,20)
        self.bouton_down_image = pygame.image.load("bas.png")

# mur final :

        """
        Crée le dernier mur qui correspond à la sortie de la map 4

        Définit les dimensions du mur et sa couleur

        """
        self.area_mur_fin1 = pygame.Rect((1290,250,10,200))
        self.area_mur_fin1_color = (0,0,255)

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
        self.screen.fill((144,90,246))

    def mort(self):

        """
        Gère le cas où un personnage rentre en contact avec le mur de lave

        On suit le schèma suivant :

            si le bas ou le haut de la map et un personnage rentre en contact
            alors on initialise une fenêtre pour l'affichage de la map4

        Ce qui signifie que le personnage meurt s'il touche l'un des murs et que
        le niveau recommence

        """
        if self.area_bas.colliderect(self.player1.rect) or self.area_bas.colliderect(self.player2.rect) or self.area_haut.colliderect(self.player1.rect) or self.area_haut.colliderect(self.player2.rect):
            maps4.__init__(self,pygame.display.set_mode((1300,700)))
            return True

    def update_map(self):

        """
        Réactualise l'image de la map plusieurs fois par seconde

        """
        maps4.deplacement(self)
        maps4.murs(self)
        maps4.items(self)
        maps4.boutons(self)

    def deplacement(self):

        """
        Gère l'avancement du mur de lave

        """
        self.area_bas.move_ip(0, self.direction*self.vitesse_mur)
        self.area_haut.move_ip(0, self.direction*self.vitesse_mur)

    def boutons(self):

        """
        Gère le cas où le personnage appuie sur un des deux boutons pour
        changer l'avancement du mur

        On suit le schèma suivant :

            si la personnage rentre en contact avec un des deux boutons
            alors l'avancement du mur de lave est changé et la lave part dans
            la direction inverse

        """
        # bouton up pour que le mur de lave monte :
        if self.bouton_up.colliderect(self.player1.rect) :
            self.direction = -1

        # bouton down pour que le mur de lave descende :
        if self.bouton_down.colliderect(self.player1.rect) :
            self.direction = 1

    def murs(self):

        """
        Gère le cas où un personnage rentre en contact avec un des murs ou un
        des côtés de la map
        (on ne prend en compte que le côté gauche et le droit de la map car le
        haut et le bas bougent puisqu'ils forment le mur de lave)
        Fait ainsi reculer ce personnage à la place qu'il occupait juste avant
        la collision

        On utilise la vélocité pour savoir quel était le dernier mouvement du
        personnage et ainsi le remettre à la bonne place avant de l'arrêter
        ( avec les : self.player.get_speed() )

        """
# contours de la map :

        """
        Gère le cas où un personnage rentre en contact avec le bas ou le haut de
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

        """
        On a un cas spécial pour le mur 4, car si le personnage qui n'est pas
        prisonnier a ramassé les huit pièces présentent dans la map, alors le
        personnage prisonnier est libéré par la suppression du quatrième mur

        On gère donc ici le cas où les huit pièces n'ont pas toutes été
        ramassées

        """
    # si le nombre de pièces ramassées n'est pas égal à 8 :
        if self.nb_piece!=8:
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
                self.player4.rect.move_ip(0,-self.player2.get_speed())

        # gauche :
            if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==-1:
                self.player2.rect.move_ip(self.player2.get_speed(),0)

        # droite :
            if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[0]==1:
                self.player2.rect.move_ip(-self.player2.get_speed(),0)

        # bas :
            if self.area_mur4.colliderect(self.player2.rect) and self.player2.velocity[1]==-1:
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


    def fin_jeu(self):

        """
        Définit le moment où le niveau est terminé

        Le niveau est terminé lorsque le nombre de pièces collectées est
        égal à 8 et que chaque personnage est sur le mur final

        """
        if self.nb_piece == 8 and self.area_mur_fin1.colliderect(self.player1.rect) and self.area_mur_fin1.colliderect(self.player2.rect):
            return True

    def affiche_map(self):

        """
        Dessine la map avec, respectivement :

            - la fenêtre
            - la couleur des murs de la map (ou ses contours) ainsi que celle
                des deux boutons
            - les dimensions de chaque murs de la map (ou ses contours) ainsi
                que celles des deux boutons

        On a le cas spécial du mur 4 :

            si le personnage qui n'est pas prisonnier n'a pas ramassé toutes les
            pièces présentent dans la map, alors on dessine le quatrième mur de
            la prison du second personnage

            si le personnage qui n'est pas prisonnier a ramassé les huit pièces
            présentent dans la map, alors on ne dessine pas le quatrième mur de
            la prison du second personnage et celui-ci est donc libéré

        """

        # contours de la map (gauche, droit, haut et bas) :
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_gauche)
        pygame.draw.rect(self.screen, self.area_droite_color, self.area_droite)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_haut)
        pygame.draw.rect(self.screen, self.area_gauche_color, self.area_bas)

        # mur final correspondant à la sortie :
        pygame.draw.rect(self.screen, self.area_mur_fin1_color, self.area_mur_fin1)

        # murs de la prison :
        pygame.draw.rect(self.screen, self.area_mur1_color, self.area_mur1)
        pygame.draw.rect(self.screen, self.area_mur2_color, self.area_mur2)
        pygame.draw.rect(self.screen, self.area_mur3_color, self.area_mur3)

        # quatrième mur de la prison :
        if self.nb_piece !=8:
            pygame.draw.rect(self.screen, self.area_mur4_color, self.area_mur4)

        # boutons qui gèrent le déplacement du mur de lave :
        self.screen.blit(self.bouton_up_image,self.bouton_up)
        self.screen.blit(self.bouton_down_image,self.bouton_down)

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