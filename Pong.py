import pygame
import time
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
FPS = 60
clock = pygame.time.Clock()
width = 900
height = 600
border = 7
rect_breadth = 25
rect_height = 80
vel = 10
ball_vel = 5
radius = 15
direction = "rightdown"
x = 150
y = 150


def pause(Display_Surf):
        paused = True
        while paused:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            Display_Surf.fill(white)

            message("Press Q for Exit ,Press C to Continue",Display_Surf)
            pygame.display.update()
            clock.tick(FPS)


def message(text,Display_Surf,size=30,color=black):
    pygame.font.init()
    myFont = pygame.font.SysFont('Comic Sans MS', size)
    textSurface = myFont.render(text, False, color)
    rect_text = textSurface.get_rect()
    rect_text.center = (width/2,height/2)
    Display_Surf.blit(textSurface, (rect_text))


def circle(radius, height, width,Display_Surf,lead_y1,lead_y2):

    global x
    global y
    global direction
    global game_over
    if direction == "rightdown":
        x += ball_vel
        y += ball_vel
        if y >= height-radius:
            direction = "rightup"
        else:
            if x >=width-rect_breadth-border-radius and (y<=lead_y2+rect_height and y>=lead_y2):

                direction = "leftdown"
            elif x == width-radius or x > width-radius:
                game_over = True

    elif direction == "rightup":
        x += ball_vel
        y -= ball_vel

        if y <= radius:
            direction = "rightdown"
        else:
            if x >= width - rect_breadth - border - radius and (y <= lead_y2 + rect_height and y >= lead_y2):
                direction = "leftup"
            elif x == width-radius or x > width-radius:
                game_over = True


    elif direction == "leftup":
        x -= ball_vel
        y -= ball_vel
        if y <= radius:
            direction = "leftdown"
        else:
            if x <= border + rect_breadth + radius and (y<=lead_y1+rect_height and y>=lead_y1):
                direction = "rightup"
            elif x == radius or x < radius:
                game_over = True
                x = 400
                y = 400
    elif direction == "leftdown":
        x -= ball_vel
        y += ball_vel
        if y >= height-radius:
            direction = "leftup"
        else:
            if x <= border + rect_breadth + radius and (y <= lead_y1 + rect_height and y >= lead_y1):
                direction = "rightdown"
            elif x == radius or x < radius:
                game_over = True
                x = 400
                y = 400
    pygame.draw.circle(Display_Surf, white, (x,y), radius)


def mainloop():
    lead_y1 = height/2 - rect_height
    lead_y2 = height / 2 - rect_height
    pygame.init()
    Display_Surf = pygame.display.set_mode((width,height))
    pygame.display.set_caption("PONG")
    Display_Surf.fill(white)
    message("WELCOME TO PONG GAME", Display_Surf,60,red)
    pygame.display.update()
    time.sleep(2)
    global gameExit
    global game_over
    game_over = False
    gameExit = False
    while not gameExit:
        while game_over == True:
            Display_Surf.fill(white)
            message("Press S to start again or Q to quit",Display_Surf)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    gameExit = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        mainloop()
                    elif event.key == pygame.K_q:
                        game_over  = False
                        gameExit = True
                        pygame.quit()

                        quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and lead_y1!=0:
                lead_y1 -= vel
        elif keys[pygame.K_DOWN] and lead_y1!=height-rect_height:
                lead_y1 += vel

        if keys[pygame.K_w] and lead_y2!=0:
                lead_y2 -= vel
        elif keys[pygame.K_s] and lead_y2!=height-rect_height:
                lead_y2 += vel
        elif keys[pygame.K_p]:
             pause(Display_Surf)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        Display_Surf.fill(blue)
        pygame.draw.rect(Display_Surf, black, (border, lead_y1, rect_breadth, rect_height))
        pygame.draw.rect(Display_Surf, black, (width - rect_breadth-border, lead_y2,
                                               rect_breadth,
                                               rect_height))
        circle(radius, height, width,  Display_Surf, lead_y1,lead_y2)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit
    quit()


mainloop()