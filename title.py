"""
Name: title.py
Purpose: Text for the project title.
Author: Nathaniel Metrock & Sean Jackson
License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
"""


import pygame, sys
from pygame.locals import *


# set up pygame
pygame.init()


# set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Relue World!')


# set up the colors
black = (0, 0, 0)
white = (255, 255, 255)


# set up fonts
basicFont = pygame.font.SysFont(None, 48)


# set up the text
text = basicFont.render("Relue...     Of War.",True,white,black)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery


# draw the white background onto the surface
windowSurface.fill(black)


# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = black
del pixArray


# draw the text onto the surface
windowSurface.blit(text,textRect)


# draw the window onto the screen
pygame.display.update()


# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

