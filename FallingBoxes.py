import pygame
import random
import sys


pygame.init()

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
WHITE = (255, 255, 255)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BACKGROUND_COLOR = (0,0,0)

player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

enemy_size = 50
enemy_pos = [random.randint(0,WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
def message(text,Display_Surf,size=30,color=BACKGROUND_COLOR):
    pygame.font.init()
    myFont = pygame.font.SysFont('Comic Sans MS', size)
    textSurface = myFont.render(text, False, color)
    rect_text = textSurface.get_rect()
    rect_text.center = (WIDTH/2,HEIGHT/2)

    Display_Surf.blit(textSurface, (rect_text))

SPEED = 10
menu_exit = False
pygame.init()
main_screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Menu Screen")
main_screen.fill(WHITE)
message("PRESS 1 for PONG GAME, 2 for FALLING BOXES", main_screen,30,RED)
pygame.display.update()
while not menu_exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				menu_exit = True
				import Pong
				Pong.mainloop()
			elif event.key == pygame.K_2:
				menu_exit = True
				screen = pygame.display.set_mode((WIDTH, HEIGHT))
				pygame.display.set_caption("Falling Boxes")

				game_over = False

				score = 0

				clock = pygame.time.Clock()

				myFont = pygame.font.SysFont("monospace", 35)

				def message(text,Display_Surf,size=30,color=BACKGROUND_COLOR):
					pygame.font.init()
					myFont = pygame.font.SysFont('Comic Sans MS', size)
					textSurface = myFont.render(text, False, color)
					rect_text = textSurface.get_rect()
					rect_text.center = (WIDTH/2,HEIGHT/2)

					Display_Surf.blit(textSurface, (rect_text))

				def set_level(score, SPEED):
					if score < 20:
						SPEED = 5
					elif score < 40:
						SPEED = 8
					elif score < 60:
						SPEED = 12
					else:
						SPEED = 15
					return SPEED
					# SPEED = score/5 + 1

				def drop_enemies(enemy_list):
					delay = random.random()
					if len(enemy_list) < 10 and delay < 0.1:
						x_pos = random.randint(0,WIDTH-enemy_size)
						y_pos = 0
						enemy_list.append([x_pos, y_pos])

				def draw_enemies(enemy_list):
					for enemy_pos in enemy_list:
						pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

				def update_enemy_positions(enemy_list, score):
					for idx, enemy_pos in enumerate(enemy_list):
						if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
							enemy_pos[1] += SPEED
						else:
							enemy_list.pop(idx)
							score += 1
					return score

				def collision_check(enemy_list, player_pos):
					for enemy_pos in enemy_list:
						if detect_collision(enemy_pos, player_pos):
							return True
					return False

				def detect_collision(player_pos, enemy_pos):
					p_x = player_pos[0]
					p_y = player_pos[1]

					e_x = enemy_pos[0]
					e_y = enemy_pos[1]

					if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x+enemy_size)):
						if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y+enemy_size)):
							return True
					return False

				while not game_over:

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							sys.exit()

						if event.type == pygame.KEYDOWN:

							x = player_pos[0]
							y = player_pos[1]

							if event.key == pygame.K_LEFT:
								x -= player_size
							elif event.key == pygame.K_RIGHT:
								x += player_size

							player_pos = [x,y]

					screen.fill(BACKGROUND_COLOR)

					drop_enemies(enemy_list)
					score = update_enemy_positions(enemy_list, score)
					SPEED = set_level(score, SPEED)

					text = "Score:" + str(score)
					label = myFont.render(text, 1, YELLOW)
					screen.blit(label, (WIDTH-200, HEIGHT-40))

					if collision_check(enemy_list, player_pos):
						game_over = True
						break

					draw_enemies(enemy_list)

					pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

					clock.tick(30)

					pygame.display.update()