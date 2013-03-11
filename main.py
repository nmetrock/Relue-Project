import sys, pygame

X = 120
Y = 0
SQUARE = [['40px', '40px']]

GRASS = [.6, .5, .75, 1, .4, .5]
DIRT = [.5, .6, .5, .75, 1, .75]
WATER = [float('inf'), 0, 0, 0, 0, 0]
MOUNTAIN = [1, .75, 1, .5, .75, .4]
FORT = [.75, 1, .4, .6, .5, 1]

ARCHERS = [.4, .3, .7, .2, .7, .6, .5, .8, .4]
SPEARMEN = [.6, .8, .8, .6, .5, .5, .7, .6, .6]
SELLSWORDS = [.3, .7, .4, .4, .8, .2, 6, .5, .2]
KNIGHTS = [.8, .9, .9, .8, .4, .7, .9, .4, .9]
CALVERY = [.9, .6, .6, .9, .3, .8, .8, .9, .7]
APPRENTICES = [.7, .2, .2, .7, .6, .3, .4, .3, .8]
PRIESTS = [.2, .5, .5, .3, .2, .9, .2, .7, .3]
ACOLYTES = [.5, .4, .3, .5, .9, .3, .3, .2, .5]
ENVOYS = [.1, .1, 1, .1, 1, .1, .1, 1, .1]
KINGS = [1, 1, .1, 1, .1, 1, 1, .1, 1]

TILES = [GRASS, DIRT, WATER, MOUNTAIN, FORT]
UNITS = [ARCHERS, SPEARMEN, SELLSWORDS, KNIGHTS, CALVERY, APPRENTICES, PRIESTS, ACOLYTES, ENVOYS, KINGS]


def Tile (tile_name, slow, defense, siege, food, attack, air):
	10*(X + 40)
	10*(Y + 40)

def Unit (unit_name, attack, defense, group, cost, endurance, morale, health, move, level):
	unit_name = unit_name.self

def Generate_Map(self):
	for i in range(0, 4):
		Tile(TILES[i])

pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Relue Project")

while 1:

	screen.fill((0, 0, 0))
	pygame.display.flip()
