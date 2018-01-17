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

#Libraries
import pygame
from pygame.locals import *

#Screen properties
width, height = 800, 600 #pixels

#Colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)



######################################
#Def Main

def main():
    """
    Main components of the program.
    :return:
    """
    pygame.init()
    screen = pygame.display.set_mode((width,height))

    eventsListener(screen)
#END funct main

def eventsListener(screen):
    """
    Using keyboard inputs
    :return:
    """
    running = True
    while running:
        #Quitter
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        #Dessiner
        pygame.draw.rect(screen,white, (100,100,60,20))
        pygame.display.update() #Mettre à jour Pygame

    pygame.quit()#Quit the game
#END funct enventsListener


######################################
#Appel des fonctions
main()

