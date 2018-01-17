#!/usr/bin/enb python
# coding: utf-8
###################################
# Jeu Python
# Version Py : python3
# Derrière Mise à jour 17/01/2017
###################################

__author__ = "Renaud BERNARD"
__copyright__ = "Copyright 2018"
__license__ = "Free"
__version__ = "1.0.1"
__email__ = "renaud.bernard@p59production.com"
__status__ = "Production"

######################################
#Initialise project
import pygame, sys, time, random from pygame.locals import *
pygame.init()
fpsClock = pygame.time.Clock()

######################################
#Graphisme de ouf NVIDIA Geforce 2160Ti
playSurface = pygame.display.set_mode((800, 600)) #La surface de jeu
pygame.display.set_caption("Python Snake Basic") #Le nom du jeu
#Définition des couleurs
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)

######################################
#Let's moove
snakePosition = [100, 100]
snakeSegments[(100, 100), (80, 100), (60, 100)]
raspeberryPosition = [300, 300] #Pas trop utile
raspberry Spawned = 1
direction = "right"
changeDirection = direction

######################################
#Functions

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 100) #Vérifer police
    gameOverSurf = gameOverFont.render("Game over \n Le serpent s'est mordu la queue", True, greyColor)
    gameOverRect = gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop=(400, 30)
    play.Surface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()
#END func gameOver

while True:
    for even in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==KEYDOWN: #Vérifier AZRETY-QUERTY
            #Direction quand on appuie sur les touches
            if event.key == K_RIGHT or event.key == ord('d'):
                changeDirection = "right"
            if event.key == K_LEFT or event.key == ord('q'):
                changeDirection = "left"
            if event.key == K_UP or event.key == ord('z'):
                changeDirection = "up"
            if event.key == K_DOWN or event.key == ord('s'):
                changeDirection = "down"
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            #Eviter que le serpet ne revienne pas sur ses pas du genre 360
            if changeDirection == "right" and not direction == "left":
                direction = changeDirection
            if changeDirection == "left" and not direction == "right":
                direction = changeDirection
            if changeDirection == "up" and not direction == "down":
                direction = changeDirection
            if changeDirection == "down" and not direction == "up":
                direction = changeDirection
            #gestion des distances
            if direction == "right":
                snakePosition[0] +=20
            if direction == "right":
                snakePosition[0] -=20
            if direction == "right":
                snakePosition[1] -=20
            if direction == "right":
                snakePosition[1] +=20
            #BodySnake
            snakeSegments.insert(0, list(snakePosition))
            #Toujours plus long
                    

















    



