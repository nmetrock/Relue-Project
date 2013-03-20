"""
Name: main.py
Purpose: Game loop and variables
Author: Nathaniel R. Metrock
License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
"""

import os.path
import pygame
#import rules


WIDTH = 640
HEIGHT = 400
GRID_X = 120
GRID_Y = 0
TILE_X = 40
TILE_Y = 40
BG_COLOR = [0, 0, 0]
MAX_FPS = 30

#TILE = [slow, defense, siege, food, attack, air]
GRASS = [.6, .5, .75, 1, .4, .5]
DIRT = [.5, .6, .5, .75, 1, .75]
WATER = [float('inf'), 0, 0, 0, 0, 0]
MOUNTAIN = [1, .75, 1, .5, .75, .4]
FORT = [.75, 1, .4, .6, .5, 1]
TILES = [GRASS, DIRT, WATER, MOUNTAIN, FORT]

#UNIT = [attack, defense, group, cost, endurance, morale, health, move, level]
ARCHERS = [.4, .3, .7, .2, .7, .6, .5, .8, .4]
SPEARMEN = [.6, .8, .8, .6, .5, .5, .7, .6, .6]
SELLSWORDS = [.3, .7, .4, .4, .8, .2, .6, .5, .2]
KNIGHTS = [.8, .9, .9, .8, .4, .7, .9, .4, .9]
CALVERY = [.9, .6, .6, .9, .3, .8, .8, .9, .7]
APPRENTICES = [.7, .2, .2, .7, .6, .3, .4, .3, .8]
PRIESTS = [.2, .5, .5, .3, .2, .9, .2, .7, .3]
ACOLYTES = [.5, .4, .3, .5, .9, .3, .3, .2, .5]
ENVOYS = [.1, .1, 1, .1, 1, .1, .1, 1, .1]
KINGS = [1, 1, .1, 1, .1, 1, 1, .1, 1]
UNITS = [ARCHERS, SPEARMEN, SELLSWORDS, KNIGHTS, CALVERY, APPRENTICES, PRIESTS,
         ACOLYTES, ENVOYS, KINGS]


class GenerateMap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None

    def new_map(self, tile_set):
        """Generates a random map"""
        self.tile_set = tile_set

        for i in range(len(tile_set)):
            if tile_set[i] == GRASS:
                for i in range(0,10):
                    for i in range(0,10):
                        screen.blit(self.generate_grass(), (self.x, self.y))
                        self.x += 40
                    self.x = GRID_X
                    self.y += 40

    def tile(self, name):
        """Generate a single tile on the map"""
        self.name = name

        if name == GRASS:
            for i in range(0,10):
                for i in range(0,10):
                    screen.blit(self.generate_grass(), (self.x, self.y))
                    self.x += 40
                self.x = GRID_X
                self.y += 40

    def generate_grass(self):
        """Fill all tiles with grass."""
        grass_tile = pygame.image.load(os.path.join("data", "tiles",
                                                     "grass0.png")).convert()
        return grass_tile

    def unit(self, unit_name):
        """"""
    	unit_name = unit_name.self


#Start pygame & create display
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Relue Project")

#Create & fill background
background = pygame.Surface(screen.get_size())
background.fill((BG_COLOR))
background = background.convert()

#Add text for title
#run title.py

#Generate map & draw to screen
game_map = GenerateMap(GRID_X, GRID_Y)
screen.blit(background, (0, 0))
game_map.new_map(TILES)


clock = pygame.time.Clock()
gameloop = True

while gameloop:
    #Wait for a tick
    time_pass = clock.tick(MAX_FPS)

    #Check for keypress or game close
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameloop = False

    #Update screen
    pygame.display.flip()