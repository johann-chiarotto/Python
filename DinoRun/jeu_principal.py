from math import*
from time import*
from random import*
import pygame
from maps1 import*
from maps2 import*
from maps3 import*
from maps4 import*
from maps5 import*

class Player1:

    """
    Création de la classe du premier personnage

    """
    def __init__(self,x,y):

        """
        Définit l'image à choisir lorsque le personnage se dirige vers la
        droite et lorsqu'il se dirige vers la gauche

        Définit la vitesse et la vélocité du personnage

        """
        self.image_droite = image_ch_droitej1
        self.image_gauche = image_ch_gauchej1
        self.__image = self.image_droite
        self.rect = self.__image.get_rect(x=x,y=y)
        self.__speed = 5
        self.velocity = [0,0]

    def move(self):

        """
        Gère le mouvement du personnage :

        """
        self.rect.move_ip(self.velocity[0]*self.get_speed(), self.velocity[1]*self.get_speed())

    def draw(self, screen):

        """
        Gère l'affichage du personnage :

        """
        screen.blit(self.__image,self.rect)

    """
    getter et setter pour la vitesse du personnage :

    """
    def get_speed(self):
         return self.__speed

    def set_speed(self, valeur):
        self.__speed = valeur

    """
    getter et setter pour l'image du personnage :

    """
    def get_image(self):
         return self.__image

    def set_image(self, valeur):
        self.__image = valeur


class Player2:

    """
    Création de la classe du second personnage

    """
    def __init__(self,x,y):

        """
        Définit l'image à choisir lorsque le personnage se dirige vers la
        droite et lorsqu'il se dirige vers la gauche

        Définit la vitesse et la vélocité du personnage

        """
        self.image_droite = image_ch_droitej2
        self.image_gauche = image_ch_gauchej2
        self.__image = self.image_droite
        self.rect = self.__image.get_rect(x=x,y=y)
        self.__speed=5
        self.velocity = [0,0]

    def move(self):
        self.rect.move_ip(self.velocity[0]*self.get_speed(), self.velocity[1]*self.get_speed())

    def draw(self, screen):
        screen.blit(self.__image,self.rect)

    """
    getter et setter pour la vitesse du personnage :

    """
    def get_speed(self):
         return self.__speed

    def set_speed(self, valeur):
        self.__speed = valeur

    """
    getter et setter pour l'image du personnage :

    """
    def get_image(self):
         return self.__image

    def set_image(self, valeur):
        self.__image = valeur

class Game:

    """
    Création de la classe du le jeu lui-même

    """
    def __init__(self, screen):

        """
        Choisit le placement du joueur sur la map en fonction du niveau

        """

        self.screen = screen
        self.quitte = False

        # booléen la boucle principale
        self.__running = True

        # bloque la boucle pour quelle ne s'exécute qu'un certain nombre de fois par secondes :
        self.clock = pygame.time.Clock()

        # place le personnage sur la map :
        if niveau==1:
            self.player1 = Player1(40,170)
            self.player2 = Player2(40,100)
        elif niveau==2:
            self.player1 = Player1(50,625)
            self.player2 = Player2(50,30)
        elif niveau==3:
            self.player1 = Player1(30,625)
            self.player2 = Player2(30,30)
        elif niveau==4:
            self.player1 = Player1(560,305)
            self.player2 = Player2(200,305)
        elif niveau==5:
            self.player1 = Player1(1245,645)
            self.player2 = Player2(5,5)


        # initialise la map du bon niveau :
        if niveau == 1:
            maps1.__init__(self,screen)
        elif niveau == 2:
            maps2.__init__(self,screen)
        elif niveau == 3:
            maps3.__init__(self,screen)
        elif niveau == 4:
            maps4.__init__(self,screen)
        elif niveau == 5:
            maps5.__init__(self,screen)

    """
    getters et setters de running :

    """
    def get_running(self):
         return self.__running
    def set_running(self, valeur):
        self.__running = valeur

    def handling_events(self):

        """
        Gère la mise à jour de l'emplacement des personnages

        """
        for event in pygame.event.get():
            # si l'action effectuée est celle de quitter :
            if event.type == pygame.QUIT:
                # alors on quitte la boucle
                self.quitte=True
                self.set_running (False)

        # touche pressée pour le premier personnage :
        keys = pygame.key.get_pressed()

        # on regarde quelle touche a été touché et on agit en conéquence :
        if keys[pygame.K_RSHIFT]:
            self.player1.set_speed(7)
        else:
            self.player1.set_speed(5)
        if keys[pygame.K_LEFT]:
            self.player1.velocity[0] = -1
            self.player1.set_image(self.player1.image_gauche)
        elif keys[pygame.K_RIGHT]:
            self.player1.set_image(self.player1.image_droite)
            self.player1.velocity[0] = +1
        else:
            self.player1.velocity[0] = 0
        if keys[pygame.K_UP]:
            self.player1.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player1.velocity[1] = +1
        else:
            self.player1.velocity[1] = 0


        # touche pressée pour le deuxième personnage :
        keys = pygame.key.get_pressed()

        # on regarde quelle touche a été touché et on agit en conéquence :
        if keys[pygame.K_LSHIFT]:
            self.player2.set_speed(7)
        else:
            self.player2.set_speed(5)
        if keys[pygame.K_q]:
            self.player2.set_image (self.player2.image_gauche)
            self.player2.velocity[0] = -1
        elif keys[pygame.K_d]:
            self.player2.set_image(self.player2.image_droite)
            self.player2.velocity[0] = +1
        else:
            self.player2.velocity[0] = 0
        if keys[pygame.K_z]:
            self.player2.velocity[1] = -1
        elif keys[pygame.K_s]:
            self.player2.velocity[1] = +1
        else:
            self.player2.velocity[1] = 0

    def update(self):
        """
        Permet de bien placer les personnage et de mettre à jour
        les maps
        Vérifie également si le niveau est terminé ou si un personnage est mort

        """

        # gère le mouvement des personnage :
        self.player1.move()
        self.player2.move()

        # regarde si la map est finie ou si un personnage est mort
        if niveau==1:
            if maps1.fin_jeu(self)==True:
                self.set_running (False)
        if niveau==2:
            if maps2.fin_jeu(self)==True:
                self.player1 = Player1(50,625)
                self.player2 = Player2(50,30)
            elif maps2.fin_jeu(self)==False:
                self.set_running(False)
        if niveau==3:
            if maps3.fin_jeu(self)==True:
                self.player1 = Player1(30,625)
                self.player2 = Player2(30,30)
                print("Vous n'avez pas réusi le niveau 3... Recommencer pour un sans fautes !!!")
            elif maps3.fin_jeu(self)==False:
                self.set_running (False)
        if niveau==4:
            if maps4.mort(self)==True:
                self.player1 = Player1(560,305)
                self.player2 = Player2(200,305)
                print("Aaaa la lave ça brûle !!!!!")
            if maps4.fin_jeu(self)==True:
                self.set_running (False)
        if niveau == 5:
            if maps5.fin_jeu(self)==True:
                self.set_running(False)

        # mettre à jour les maps :
        if niveau == 1:
            maps1.update_map(self)
        elif niveau == 2:
            maps2.update_map(self)
        elif niveau == 3:
            maps3.update_map(self)
        elif niveau == 4:
            maps4.update_map(self)
        elif niveau == 5:
            maps5.update_map(self)

    def display(self):
        """
        Gère le côté visuel avec l'affichage des maps, les fond
        ainsi que l'image des joueurs

        """

        # affiche les maps et le fond de chaque map :
        if niveau == 1:
            maps1.fond(self)
            maps1.affiche_map(self)
        elif niveau ==2:
            maps2.fond(self)
            maps2.affiche_map(self)
        elif niveau == 3:
            maps3.fond(self)
            maps3.affiche_map(self)
        elif niveau == 4:
            maps4.fond(self)
            maps4.affiche_map(self)
        elif niveau == 5:
            maps5.fond(self)
            maps5.affiche_map(self)

        # affiche les images pour chaque personnage :
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

        # mise à jour de l'écran :
        pygame.display.flip()

    def run(self):

        """
        Boucle principale qui fait tourner le jeu

        """
        while self.__running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(50)

# défini le nombre de niveaux :
nb_niveaux = 5

def color():
    """
    Définit la couleur de chaque personnage en fonction du choix
    de chaque joueur

    """
    # demande à chaque joueur la couleur qu'il souhaite pour son personnage :
    couleur=str(input("De qu'elle couleur voulez-vous être ? (V = vert ; R = rose ; B = bleu ; O = orange)"))

    # met le nom de la couleur choisie en minuscule :
    couleur=couleur.lower()

    """
    On suit le schéma suivant :

        si la couleur est " (nom de la couleur) "
        alors on importe les images correspondantes pour le personnage

        sinon on informe le joueur qu'il a mal saisit la couleur
        et on importe les images correspondantes au personnage vert

    """
    if couleur=="v" or couleur =="vert" or couleur =="verte":
        return  pygame.image.load("Dinosaure vert_droite.png"),pygame.image.load("Dinosaure vert_gauche.png")
    elif couleur=="r" or couleur =="rose":
        return  pygame.image.load("Dinosaure rose_droite.png"),pygame.image.load("Dinosaure rose_gauche.png")
    elif couleur=="b" or couleur =="bleu":
        return  pygame.image.load("Dinosaure bleu_droite.png"),pygame.image.load("Dinosaure bleu_gauche.png")
    elif couleur=="o" or couleur =="orange":
        return  pygame.image.load("Dinosaure orange_droite.png"),pygame.image.load("Dinosaure orange_gauche.png")
    else:
        print("Vous avez mal choisit votre couleur, le personnage sera donc vert")
        return  pygame.image.load("Dinosaure vert_droite.png"),pygame.image.load("Dinosaure vert_gauche.png")

# défiit une image du personnage en fonction de la couleur choisie :
image_ch_droitej1,image_ch_gauchej1 = color()
image_ch_droitej2,image_ch_gauchej2 = color()

for i in range(nb_niveaux):

        """
        Définit les action du jeu en fonction du nombre de niveau

        """
        pygame.init()
        niveau=i+1
        screen = pygame.display.set_mode((1300,700))
        game= Game(screen)
        game.run()
        if game.quitte==True:
            pygame.quit()
            break
        pygame.quit()

# Fin
print("")
print("Merci d'avoir joué :)")
print("Clémence")
print("Anaïs")
print("Johann")
print("Icare :)")