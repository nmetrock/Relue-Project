import os.path
import random
import pygame
import title


WIDTH = 640
HEIGHT = 400
GRID_X = 120
black = (0, 0, 0)

MAX_FPS = 20


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Relue Project")


def draw_map():
	x = GRID_X
	y = 0
	grass = pygame.image.load(os.path.join("data","tiles",
											"grass.png")).convert()
	water = pygame.image.load(os.path.join("data","tiles",
											"water.png")).convert()
	dirt = pygame.image.load(os.path.join("data","tiles",
											"dirt.png")).convert()
	mountain = pygame.image.load(os.path.join("data","tiles",
												"mountain.png")).convert()
	fort = pygame.image.load(os.path.join("data","tiles",
											"fort.png")).convert()

	for row in range(10):
		for col in range(10):
			if grid[row][col] == 'G':
				screen.blit(grass, (x, y))
			elif grid[row][col] == 'W':
				screen.blit(water, (x, y))
			elif grid[row][col] == 'D':
				screen.blit(dirt, (x, y))
			elif grid[row][col] == 'M':
				screen.blit(mountain, (x, y))
			elif grid[row][col] == 'F':
				screen.blit(fort, (x, y))
			x += 40
		x = GRID_X
		y += 40

def off_map(row, col, direction, distance):
 	if direction == 0:
 		if row - distance < 0:
 			return True
 	elif direction == 1:
 		if col + distance > 9:
 			return True
 	elif direction == 2:
 		if row + distance > 9:
 			return True
 	else:
 		if col - distance < 0:
 			return True

def generate_map():
	global grid
	grid = [['G' for row in range(10)] for col in range(10)]

	water_grid = []
	coming_from = None
	gen_water = True
	w_row = random.randint(0,9)
	if w_row==0 or w_row==9:
		w_col = random.randint(0,9)
	else:
		w_col = random.randrange(0,10,9)
	water_grid.append((w_row, w_col))
	while gen_water:
		if len(water_grid)<16:
			next_location = True
		else:
			gen_water = False
		while next_location:
			r_direct = random.randrange(4)
			r_dist = random.randint(2,4)
			if ((r_direct==coming_from) or
				(off_map(w_row,w_col,r_direct,r_dist) and len(water_grid)<8)):
				next_location = False
				break
			elif off_map(w_row,w_col,r_direct,r_dist) and len(water_grid)>=8:
				last_draw = True
			else:
				last_draw = False
			if r_direct == 0:
				for i in range(r_dist):
					w_row -= 1
					if (w_row < 0) or (len(water_grid) == 16):
						gen_water = False
						break
					water_grid.append((w_row, w_col))
					coming_from = 2
					next_location = False
			elif r_direct == 1:
				for i in range(r_dist):
					w_col += 1
					if (w_col > 9) or (len(water_grid) == 16):
						gen_water = False
						break
					water_grid.append((w_row, w_col))
					coming_from = 3
					next_location = False
			elif r_direct == 2:
				for i in range(r_dist):
					w_row += 1
					if (w_row > 9) or (len(water_grid) == 16):
						gen_water = False
						break
					water_grid.append((w_row, w_col))
					coming_from = 0
					next_location = False
			else:
				for i in range(r_dist):
					w_col -= 1
					if (w_col < 0) or (len(water_grid) == 16):
						gen_water = False
						break
					water_grid.append((w_row, w_col))
					coming_from = 1
					next_location = False
			if last_draw:
				gen_water = False
	for row, col in water_grid:
		grid[row][col] = 'W'


done = False
clock = pygame.time.Clock()
first_run = True

while done == False:
	# EVENT PROCESSING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
  
  
    # GAME LOGIC
 

 
    # DRAW CODE
	if first_run:
		screen.fill(black)
		generate_map()
		first_run = False
	draw_map()

	pygame.display.flip()
 
    clock.tick(MAX_FPS)

pygame.quit()