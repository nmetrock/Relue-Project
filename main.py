import os.path
import pygame


WIDTH = 640
HEIGHT = 400
GRID_X = 120
black = (0, 0, 0)

MAX_FPS = 20


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Relue Project")



def generate_map():
	grid = [['G' for x in range(10)] for y in range(10)]
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
		for column in range(10):
			if grid[row][column] == 'G':
				screen.blit(grass, (x, y))
			elif grid[row][column] == 'W':
				screen.blit(water, (x, y))
			elif grid[row][column] == 'D':
				screen.blit(dirt, (x, y))
			elif grid[row][column] == 'M':
				screen.blit(mountain, (x, y))
			elif grid[row][column] == 'F':
				screen.blit(fort, (x, y))
			x += 40
		x = GRID_X
		y += 40
 

done = False
clock = pygame.time.Clock()

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
	screen.fill(black)
	generate_map()

    pygame.display.flip()
 
    clock.tick(MAX_FPS)

pygame.quit()