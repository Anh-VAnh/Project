import pygame
from random import randint

pygame.init()

# Set screen size
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

running = True

# Set colors use in
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
BROWN = (101, 67, 33)
SKY = (135, 206, 235)
YELLOW = (255, 255, 0)
GREY = (220, 200, 200)

# FPS
clock = pygame.time.Clock()

# Tube sizes 
TUBE_WIDTH = 50

# Choose velocity for tube movement
TUBE_VELOCITY = 3

# Distance between 2 tubes
TUBE_GAP = 150

# Position of three-first tubes (outside the screen)
tube1_x = 600
tube2_x = 800
tube3_x = 1000

# Random tube heights
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

# First bird position
BIRD_X = 50
bird_y = 300

# Bird size
BIRD_WIDTH = 35
BIRD_HEIGHT = 35

# Intial vertical velocity of bird
bird_drop = 0

# Gravitational field
GRAVITY = 0.5

# First score
score = 0

# Choose font for letters in game
font = pygame.font.SysFont('sans', 20)

# First states
tube1_pass = False
tube2_pass = False
tube3_pass = False

# Import music files
sound_die = pygame.mixer.Sound('hit.wav')
sound_point = pygame.mixer.Sound('point.wav')
sound_wing = pygame.mixer.Sound('wing.wav')

pause = False

# Import images files
background_image = pygame.image.load("game-background-png-2.png")
bird_image = pygame.image.load("chim2.png")
icon = pygame.image.load("chim2.png")

# Fit images
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
bird_image = pygame.transform.scale(bird_image, (BIRD_WIDTH, BIRD_HEIGHT))

# Quit button
text = font.render('x', True, BLACK)

# angle = 0
# rotated_image = pygame.transform.rotate(bird_image, angle)

# tube_image = pygame.image.load("Mario_pipe.png")
# tube_image = pygame.transform.scale(tube_image,(TUBE_WIDTH, HEIGHT))

# Set caption and icon in windowbar
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

# Game loop
while running:
	# FPS = 60
	clock.tick(60)

	# Mouse position
	mouse_x, mouse_y = pygame.mouse.get_pos()
	
	# First bachground
	# screen.fill(BLUE)

	# Beautiful background
	screen.blit(background_image,(0, 0))
	
	# Draw ground
	ground = pygame.draw.rect(screen, BROWN, (0, 600, 400, 0))
	
	# Draw sky
	sky = pygame. draw.rect(screen, SKY, (0, 0, 400, 0))

	# Draw tubes up
	tube1u_rect = pygame.draw.rect(screen, GREEN, (tube1_x, 0, TUBE_WIDTH, tube1_height))
	tube2u_rect = pygame.draw.rect(screen, GREEN, (tube2_x, 0, TUBE_WIDTH, tube2_height))
	tube3u_rect = pygame.draw.rect(screen, GREEN, (tube3_x, 0, TUBE_WIDTH, tube3_height))
	# screen.blit(tube_image, (tube1_x, 0)) 
	
	# Draw tubes down
	tube1d_rect = pygame.draw.rect(screen, GREEN, (tube1_x, tube1_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube1_height - TUBE_GAP))
	tube2d_rect = pygame.draw.rect(screen, GREEN, (tube2_x, tube2_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube2_height - TUBE_GAP))
	tube3d_rect = pygame.draw.rect(screen, GREEN, (tube3_x, tube3_height + TUBE_GAP, TUBE_WIDTH, HEIGHT - tube3_height - TUBE_GAP))
	# screen.blit(tube_image, (tube1_x, tube1_height + TUBE_GAP))
	
	# Draw quit
	quit_button = pygame.draw.rect(screen, GREY, (WIDTH - 20, 10, 10, 10))
	screen.blit(text, (WIDTH - 18, 4))


	# Tube movement
	tube1_x -= TUBE_VELOCITY
	tube2_x -= TUBE_VELOCITY
	tube3_x -= TUBE_VELOCITY

	# Draw bird
	bird_rect = pygame.draw.rect(screen, YELLOW, (BIRD_X, bird_y, BIRD_WIDTH, BIRD_HEIGHT))
	# pygame.Surface.blit(bird_image, screen, bird_rect)
	screen.blit(bird_image, bird_rect)
	
	# Bird drop
	bird_y += bird_drop
	bird_drop += GRAVITY
	
	# New tubes
	if tube1_x < -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(100, 400)
		tube1_pass = False
	if tube2_x < -TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(100, 400)
		tube2_pass = False
	if tube3_x < -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(100, 400)
		tube3_pass = False

	# Instruction
	howtoplay = font.render("Press Space Bar or Click Left Mouse", True, BLACK)
	screen.blit(howtoplay, (80, 10))

	# Death checking
	for tube in [tube1d_rect, tube1u_rect, tube2u_rect, tube2d_rect, tube3d_rect, tube3u_rect, ground, sky]:
		if bird_rect.colliderect(tube):
			if pause == False:
				# Play music
				pygame.mixer.Sound.play(sound_die)
			pause = True
			TUBE_VELOCITY = 0
			# angle += 1 % 360
			# x, y = bird_rect.center
			# bird_rect = bird_rect.get_rect()
			# bird_rect.center = (x, y)

			# bird_drop = 0
			# game_over_txt = font.render("GAME OVER", True, BLACK)
			# bigscore_txt = font.render("SCORE: " + str(score), True, BLACK)
			# press_txt = font.render("Press Enter to Continue", True, BLACK)
			# screen.blit(game_over_txt, (150,300))
			# screen.blit(bigscore_txt, (160, 350))
			# screen.blit(press_txt, (110,400))
			# time.sleep(0.5)
	if bird_y >= HEIGHT:
		# pause = True
		bird_drop = 0
		game_over_txt = font.render("GAME OVER", True, BLACK)
		bigscore_txt = font.render("SCORE: " + str(score), True, BLACK)
		continue_rect = pygame.draw.rect(screen, RED, (115, 295, 185, 35))
		press_txt = font.render("Press Enter to Continue", True, BLACK)
		screen.blit(game_over_txt, (155,200))
		screen.blit(bigscore_txt, (168, 250))
		screen.blit(press_txt, (120, 300))
	
	# Score
	score_txt = font.render("Score: " + str(score), True, BLACK)
	screen.blit(score_txt, (5, 5))
	# for tubee in [tube1_x, tube2_x, tube3_x]:
	# 	for tubeee in [tube1_pass, tube2_pass, tube3_pass]:
	# 		if tubee + TUBE_WIDTH <= BIRD_X and tubeee == False:
	# 			score = score + 1
				# pygame.mixer.Sound.play(sound_point)
	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
		score += 1
		pygame.mixer.Sound.play(sound_point)
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score += 1
		pygame.mixer.Sound.play(sound_point)
		tube2_pass =True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score += 1
		pygame.mixer.Sound.play(sound_point)
		tube3_pass = True

	# Events when pressing from mouse or keyboard
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		# Fly after pressing Space Bar or click button
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and pause == False:
				bird_drop = 0
				bird_drop -= 10
				pygame.mixer.Sound.play(sound_wing)

			# Restart game
			if event.key == pygame.K_RETURN:
				bird_y = 300
				bird_drop = 0
				TUBE_VELOCITY = 3
				tube1_x = 600
				tube2_x = 800
				tube3_x = 1000
				score = 0
				pause = 0

		if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and pause == False:
					bird_drop = 0
					bird_drop -= 10
					pygame.mixer.Sound.play(sound_wing)
				# Restart and Quit game
				if event.button == 1:
					if (115 < mouse_x < 115 + 185) and (295 < mouse_y < 295 + 35) and (bird_y >= HEIGHT):
						bird_y = 300
						bird_drop = 0
						TUBE_VELOCITY = 3
						tube1_x = 600
						tube2_x = 800
						tube3_x = 1000
						score = 0
						pause = 0
					if (WIDTH - 20 < mouse_x < WIDTH - 10) and (10 < mouse_y < 20):
						pygame.quit()
									
	pygame.display.flip()

pygame.quit()