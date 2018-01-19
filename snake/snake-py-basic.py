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
from random import randint
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
    global orientation, over
    running = True
    reset()
    while running:
        #Horloge
        clock.tick(fps)
        for event in pygame.event.get():
            #Exit
            if event.type == QUIT:
                running = False
            #MClavier
            if event.type == KEYDOWN:
                #Reset
                if event.key == K_r or event.key == ord("r"):
                    reset()
                #MooveOn
                if event.key == K_UP or event.key == ord("w"):
                    if orientation != down:
                        orientation = up
                if event.key == K_DOWN or event.key == ord("s"):
                    if orientation != up:
                        orientation = down
                if event.key == K_LEFT or event.key == ord("a"):
                    if orientation != right:
                        orientation = left
                if event.key == K_RIGHT or event.key == ord("d"):
                    if orientation != left:
                        orientation = right
        if not over:
            update()
        #Dessiner
        render(screen)
        pygame.display.update() #Mettre à jour Pygame
     #END boucle while
    pygame.quit()#Quit the game
#END funct enventsListener

def render(screen):
    """

    :param screen:
    :param fruit:
    :param snakeParts:
    :return:
    """
    global snakeParts, fruit
    screen.fill(grey)
    drawCell(screen, fruit, red)
    for partie in snakeParts:
        drawCell(screen, partie, white)
#END funct render

def update():
    """

    :param snakeParts:
    :param orientation:
    :return:
    """
    global fruit, snakeParts, snakeSize, orientation, over, score
    x, y = snakeParts[-1]
    x += orientation[0]
    y += orientation[1]
    newPart = (x,y)
    # Collisions avec lui même
    if newPart in snakeParts:
        over = True
    #Collisions avec le bord
    if not 0 <= x < cellX:
        over = True
    if not 0 <= y < cellY:
        over = True
    # Il grandit quand il touche le fruit
    if newPart == fruit:
        snakeSize += 1
        score += 1
        newFruit()
    if over:
        print("Game over !", "Score : ", score)
    snakeParts.append(newPart)
    if not over:
        #Il avance
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
    x = randint(0, cellX - 1)
    y = randint(0, cellY - 1)
    fruit = (x,y)
# END funct newFruit

def reset():
    """

    :return:
    """
    global snakeParts, snakeSize, orientation, over, score
    newFruit()
    snakeParts = [(40,0)]
    score = 0
    snakeSize = 4
    orientation = left
    over = False


######################################
#Appel des fonctions
main()

