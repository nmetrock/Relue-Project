#generate a screen (640x400)
#make background color of screen (black) 


#generate a grid (10x10)
#each slot in the grid is (40x40)
#starting position of the grid is (120x, 0y)


#tiles are (40x40) .png files that fill the slots of the grid
#the tiles that fill the slots of the grid are (grass, water, dirt, mountain, fort)


#grass goes under all other tiles
#grass fills the all slots of the grid


#water goes under dirt and fort
#water can start on any slot on the edge of the grid
#water travels single file
#water travels in a random direction for any of (2-4) slots at a time
#water travels not in the direction from which it came when it changes direction
#water travels until it finds the edge of the map or travels (16) slots
#water travels not in a random direction that goes outside the grid until (8) slots have been filled

#dirt must fill 2-4 of the following slot selections 1: (160x,0y)   (200x,0y)   (240x,0y)   (280x,0y)   (320x,0y)   (360x,0y)   (400x,0y)   (440x,0y)
#     												 2: (120x,40y)  (120x,80y)  (120x,120y) (120x,160y) (120x,200y) (120x,240y) (120x,280y) (120x,320y)
#													 3:	(480x,40y)  (480x,80y)  (480x,120y) (480x,160y) (480x,200y) (480x,240y) (480x,280y) (480x,320y)
#													 4:	(160x,360y) (200x,360y) (240x,360y) (280x,360y) (320x,360y) (360x,360y) (400x,360y) (440x,360y)
#dirt travels in single file
#dirt travels in a random direction for any of (2-4) slots at a time
#dirt travels not in the direction from which it came when it changes direction
#dirt travels until it finds one of the (2-4) slot selections from rules (26-29)
#dirt travels not across its own path
#dirt travels for 8 slots and then takes the shortest path to one of the (2-4) slot selections from rules (26-29) 