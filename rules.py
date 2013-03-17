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
#anywhere along the path where water travels 
#water travels 1 slot adjacent for any of (2-3) slots at a time

#dirt