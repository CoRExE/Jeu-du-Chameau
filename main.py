import pygame as game
from Parametres import *


game.init()

game.display.set_mode((largeur, hauteur))

game.display.set_caption(titre)


# Boucle Principale

while True:
    for event in game.event.get():
        if event.type == game.QUIT:
            game.quit()
            exit()
        if event.type == game.KEYDOWN:
            if event.key == game.K_RETURN:
                print("Touche Entrée enfoncée")

        game.display.update()
