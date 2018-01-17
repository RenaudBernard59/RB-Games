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
from ramdom import randint
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

#Moves
up = (0, -1)
down = (0, +1)
left = (-1, 0)
right = (+1, 0)

#TimeSet
fps = 15

######################################5
#Def Main

def main():
    """
    Main components of the program.
    :return:
    """
    pygame.init()
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    eventsListener(screen, clock)
#END funct main

def eventsListener(screen, clock):
    """
    Using keyboard inputs
    :return:
    """
    running = True
    snakeParts = [(14,10),(13,10),(12,10),(11,10),(10,10)]
    snakeSize = 4
    orientation = left
    while running:
        #Horloge
        clock.tick(fps)
        for event in pygame.event.get():
            #Exit
            if event.type == QUIT:
                running = False
            #MooveOn
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == ord("w"):
                    orientation = up
                if event.key == K_DOWN or event.key == ord("s"):
                    orientation = down
                if event.key == K_LEFT or event.key == ord("a"):
                    orientation = left
                if event.key == K_RIGHT or event.key == ord("d"):
                    orientation = right
        update(snakeParts, orientation, snakeSize)
        #Dessiner
        render(screen, fruit, snakeParts)
        pygame.display.update() #Mettre à jour Pygame
     #END boucle while
    pygame.quit()#Quit the game
#END funct enventsListener

def render(screen, snakeParts):
    """

    :param screen:
    :param fruit:
    :param snakeParts:
    :return:
    """
    screen.fill(grey)
    drawCell(screen, fruit, red)
    for partie in snakeParts:
        drawCell(screen, partie, white)
#END funct render

def update(snakeParts, orientation, snakeSize):
    """

    :param snakeParts:
    :param orientation:
    :return:
    """
    global fruit
    x, y = snakeParts[-1]
    x += orientation[0]
    y += orientation[1]
    newPart = (x,y)
    snakeParts.append(newPart)
    if newPart == fruit:
        snakeSize += 1

    if len(snakeParts) > snakeSize:
        del snakeParts[0]
#END funct update

def drawCell(screen, cell, color):
    """

    :param screen:
    :param cell:
    :param color:
    :return:
    """
    pygame.draw.rect(screen, color, (cell[0]*cellSize, cell[1]*cellSize, cellSize, cellSize))
#END funct drawCell

def newFruit():
    """

    :return:
    """
    global fruit
    x = randint(0, cellX-1)
    y = randint(0, cellY-1)
    fruit = (x,y)
# END funct newFruit




######################################
#Appel des fonctions
main()

