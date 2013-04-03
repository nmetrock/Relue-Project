"""
Name: title.py
Purpose: Text for the project title.
Author: Nathaniel Metrock & Sean Jackson
License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
"""


import pygame
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


# draw the black background onto the surface
windowSurface.fill(black)


# get a pixel array of the surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = black
del pixArray


# draw the text onto the surface
windowSurface.blit(text,textRect)


# draw the window onto the screen
pygame.display.update()
texta = basicFont.render("PRESS THE SPACE BAR",True,white,black)
textRecta = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

windowSurface.blit(texta,textRecta)

pygame.display.update()



# turn it off
done = False
clock = pygame.time.Clock()
first_run = True

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                done = True
                # run the game loop

pygame.quit()

