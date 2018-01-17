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
grey = (128,128,128)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

#Cells
cellSize = 20 #Cise of one Cell
#Number of Cells in X and Y
cellX = 40
cellY = 30


######################################5
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
    fruit = (10,10)
    myParties = [(3,8),(2,9),(4,3),(12,10),(5,3)]
    while running:
        #Quitter
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        #Dessiner
        render(screen, fruit, myParties)
        pygame.display.update() #Mettre à jour Pygame
     #END boucle while
    pygame.quit()#Quit the game
#END funct enventsListener

def render(screen, fruit, myParties):
    screen.fill(grey)
    #x, y = fruit
    drawCell(screen, fruit, red)
    for partie in myParties:
        drawCell(screen, partie, blue)
#END funct render


def drawCell(screen, cell, color):
    pygame.draw.rect(screen, color, (cell[0]*cellSize, cell[1]*cellSize, cellSize, cellSize))









######################################
#Appel des fonctions
main()

