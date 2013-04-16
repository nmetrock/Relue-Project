"""
Name: rules.py
Purpose: Text for the project title.
Author: Nathaniel Metrock & Sean Jackson
License: GNU GPL <http://www.gnu.org/licenses/gpl.html>
"""


#TILE = [terrain, fortify, siege, rations, offence, weather]
GRASS = [.1, .6, .75, .75, .5, .6]
DIRT = [.05, .5, .5, .6, .6, .75]
WATER = [float('inf'), 0, 0, 0, 0, 0]
MOUNTAIN = [.25, .75, 1, 1, 1, .5]
FORT = [.15, 1, .6, .5, .75, 1]


#UNIT = [attack, defense, group, cost, endurance, morale, health, journey, level]
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

########################################################################single map rules#########################################################################



#generate a screen (640x400)
#make background color of screen (black) 


#generate a grid (10x10)
#each slot in the grid is (40x40)
#starting position of the grid is (120x, 0y)


#tiles are (40x40) .png files that fill the slots of the grid
#the tiles that fill the slots of the grid are (grass, water, dirt, mountain, fort)


#grass is placed (1st)
	#grass goes under all other tiles
		#grass will start at all slots of the grid


#water is placed (2nd)
	#water goes under dirt and fort
		#water can start at any (1) slot on the edge of the grid
			#water travels single file
			#water travels in a random direction for any of (2-4) slots at a time
			#water travels until it finds the edge of the map or travels (16) slots
			#water travels not in a random direction that goes outside the grid until (8) slots have been filled
			#water travels not in the direction from which it came when it changes direction


#dirt is placed (3rd)
	#dirt goes under no tiles	
		#dirt can start at (1) of (2-4) of the following slot selections n: (160x,0y)   (200x,0y)   (240x,0y)   (280x,0y)   (320x,0y)   (360x,0y)   (400x,0y)   (440x,0y)
	     												       	   		#w: (120x,40y)  (120x,80y)  (120x,120y) (120x,160y) (120x,200y) (120x,240y) (120x,280y) (120x,320y)
														       	   		#e: (480x,40y)  (480x,80y)  (480x,120y) (480x,160y) (480x,200y) (480x,240y) (480x,280y) (480x,320y)
														           		#s: (160x,360y) (200x,360y) (240x,360y) (280x,360y) (320x,360y) (360x,360y) (400x,360y) (440x,360y)
			#dirt travels in single file
			#dirt travels from an n slot selection (1) slot toward s before line (73)
			#dirt travels from an e slot selection (1) slot toward w before line (73)
			#dirt travels from an s slot selection (1) slot toward n before line (73)
			#dirt travels from an w slot selection (1) slot toward e before line (73)
			#dirt travels in a random direction for any of (2-4) slots at a time toward the opposite dirt slot selection
			#dirt travels until it finds the opposite dirt slot selection from lines (60-63) minus one row
			#dirt travels not across any of the slot selections from lines (60-63) exept for the opposite dirt slot selection 
			#dirt travels not toward the its own starting slot
			#dirt travels not in the direction from which it came when it changes direction
			#dirt travels not across its own path
				#when only three slot selections have been chosen from lines (60-63) the middle selection stops when it encounters the other dirt path


#mountain is placed (4th)
	#mountain goes under fort
	#mountain never crosses water or dirt
		#mountain can start on any slot still covered by grass
			#mountain travels in single and double file
			#mountain travels in a random direction for any of (1-3) slots at a time
			#mountain travels (3-6) slots


#fort is placed (5th)
	#fort goes under no tiles
		#fort can start at any of (1-3) slot/slots inside the grid that is/are next to but not on top of a dirt slot


#this is a complete_grid

################################################################multiple map rules###############################################################################



#generate world_grid (4x4)
	#each complete_grid in the world_grid is (400x400)