import pygame
import sys
from pygame.locals import *

pygame.init()

setDisplay = pygame.display.set_mode((640,480))
pygame.display.set_caption('RGB')

last_direction = 'up'

def collisions():

    global playerx
    global playery
    global redup
    global greenup
    global blup
    global goalx
    global goaly

    if playerx == goalx and playery == goaly:

        playerx = 60
        playery = 60

    for i in range(len(wall_coords)):

        if playerx == wall_coords[i][0] and playery == wall_coords[i][1]:

            if last_direction == 'up':

                playery += cellsize

            elif last_direction == 'down':

                playery -= cellsize

            elif last_direction == 'left':

                playerx += cellsize

            elif last_direction == 'right':

                playerx -= cellsize

    if redup:

        for i in range(len(red_coords)):

            if playerx == red_coords[i][0] and playery == red_coords[i][1]:

                if last_direction == 'up':

                    playery += cellsize

                elif last_direction == 'down':

                    playery -= cellsize

                elif last_direction == 'left':

                    playerx += cellsize

                elif last_direction == 'right':

                    playerx -= cellsize

    if greenup:

        for i in range(len(green_coords)):

            if playerx == green_coords[i][0] and playery == green_coords[i][1]:

                if last_direction == 'up':

                    playery += cellsize

                elif last_direction == 'down':

                    playery -= cellsize

                elif last_direction == 'left':

                    playerx += cellsize

                elif last_direction == 'right':

                    playerx -= cellsize

    if blup:

        for i in range(len(blue_coords)):

            if playerx == blue_coords[i][0] and playery == blue_coords[i][1]:

                if last_direction == 'up':

                    playery += cellsize

                elif last_direction == 'down':

                    playery -= cellsize

                elif last_direction == 'left':

                    playerx += cellsize

                elif last_direction == 'right':

                    playerx -= cellsize

    for i in range(len(red_switch_coords)):

        if playerx == red_switch_coords[i][0] and playery == red_switch_coords[i][1]:

            if redup:

                redup = False
                greenup = True
                blup = True

            else:

                redup = True

    for i in range(len(green_switch_coords)):

        if playerx == green_switch_coords[i][0] and playery == green_switch_coords[i][1]:

            if greenup:

                greenup = False
                redup = True
                blup = True

            else:

                greenup = True

    for i in range(len(blue_switch_coords)):

        if playerx == blue_switch_coords[i][0] and playery == blue_switch_coords[i][1]:

            if blup:

                blup = False
                greenup = True
                redup = True

            else:

                blup = True

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

lgray = (200,200,200)
dgray = (100,100,100)

yellow = (255,255,0)
purple = (255,0,255)
turquoise = (0,255,255)

FPS = 30
fpsTime = pygame.time.Clock()

player = pygame.image.load('assets/Player.png')
goal = pygame.image.load('assets/Goal.png')
wall = pygame.image.load('assets/Wall.png')
red_barrier = pygame.image.load('assets/Red_Barrier.png')
green_barrier = pygame.image.load('assets/Green_Barrier.png')
blue_barrier = pygame.image.load('assets/Blue_Barrier.png')
red_switch = pygame.image.load('assets/Red_Switch.png')
green_switch = pygame.image.load('assets/Green_Switch.png')
blue_switch = pygame.image.load('assets/Blue_Switch.png')

playerx = 60
playery = 60

goalx = 560
goaly = 400

cellsize = 20

wall_coords = [(0,0),(20,0),(40,0),(60,0),(80,0),(100,0),(120,0),(140,0),(160,0),(180,0),(200,0),(220,0),(240,0),(260,0),(280,0),(300,0),(320,0),(340,0),(360,0),(380,0),(400,0),(420,0),(440,0),(460,0),(480,0),(500,0),(520,0),(540,0),(560,0),(580,0),(600,0),(620,0),
               (0,20),(20,20),(40,20),(60,20),(80,20),(100,20),(120,20),(140,20),(160,20),(180,20),(200,20),(220,20),(240,20),(260,20),(280,20),(300,20),(320,20),(340,20),(360,20),(380,20),(400,20),(420,20),(440,20),(460,20),(480,20),(500,20),(520,20),(540,20),(560,20),(580,20),(600,20),(620,20),
               (0,40),(20,40),(100,40),(120,40),(140,40),(240,40),(340,40),(600,40),(620,40),
               (0,60),(20,60),(340,60),(600,60),(620,60),
               (0,80),(20,80),(100,80),(120,80),(140,80),(240,80),(340,80),(600,80),(620,80),
               (0,100),(20,100),(40,100),(60,100),(80,100),(100,100),(120,100),(140,100),(240,100),(340,100),(600,100),(620,100),
               (0,120),(20,120),(140,120),(240,120),(260,120),(280,120),(320,120),(340,120),(600,120),(620,120),
               (0,140),(20,140),(140,140),(340,140),(600,140),(620,140),
               (0,160),(20,160),(140,160),(340,160),(600,160),(620,160),
               (0,180),(20,180),(140,180),(340,180),(600,180),(620,180),
               (0,200),(20,200),(40,200),(120,200),(140,200),(160,200),(200,200),(220,200),(240,200),(260,200),(280,200),(300,200),(320,200),(340,200),(360,200),(420,200),(440,200),(460,200),(500,200),(520,200),(540,200),(560,200),(580,200),(600,200),(620,200),
               (0,220),(20,220),(240,220),(340,220),(340,220),(440,220),(520,220),(600,220),(620,220),
               (0,240),(20,240),(240,240),(440,240),(600,240),(620,240),
               (0,260),(20,260),(240,260),(340,260),(340,260),(440,260),(520,260),(600,260),(620,260),
               (0,280),(20,280),(240,280),(260,280),(300,280),(320,280),(340,280),(360,280),(420,280),(440,280),(460,280),(480,280),(500,280),(520,280),(600,280),(620,280),
               (0,300),(20,300),(240,300),(340,300),(340,300),(440,300),(520,300),(600,300),(620,300),
               (0,320),(20,320),(240,320),(520,320),(600,320),(620,320),
               (0,340),(20,340),(240,340),(340,340),(340,340),(440,340),(520,340),(600,340),(620,340),
               (0,360),(20,360),(40,360),(80,360),(100,360),(120,360),(140,360),(160,360),(180,360),(200,360),(220,360),(240,360),(260,360),(280,360),(300,360),(320,360),(340,360),(360,360),(380,360),(400,360),(420,360),(440,360),(460,360),(500,360),(520,360),(540,360),(580,360),(600,360),(620,360),
               (0,380),(20,380),(520,380),(600,380),(620,380),
               (0,400),(20,400),(520,400),(600,400),(620,400),
               (0,420),(20,420),(520,420),(600,420),(620,420),
               (0,440),(20,440),(40,440),(60,440),(80,440),(100,440),(120,440),(140,440),(160,440),(180,440),(200,440),(220,440),(240,440),(260,440),(280,440),(300,440),(320,440),(340,440),(360,440),(380,440),(400,440),(420,440),(440,440),(460,440),(480,440),(500,440),(520,440),(540,440),(560,440),(580,440),(600,440),(620,440),
               (0,460),(20,460),(40,460),(60,460),(80,460),(100,460),(120,460),(140,460),(160,460),(180,460),(200,460),(220,460),(240,460),(260,460),(280,460),(300,460),(320,460),(340,460),(360,460),(380,460),(400,460),(420,460),(440,460),(460,460),(480,460),(500,460),(520,460),(540,460),(560,460),(580,460),(600,460),(620,460)]

red_coords = [(240,60),(480,140),(380,200),(400,200),(480,200),(340,240),(440,320),(540,260),(540,280),(540,300),(560,320),(80,240),(80,260),(80,280),(80,300),(80,320),(100,240),(120,240),(140,240),   (40,400),(60,400),(80,400),(100,400),(120,400),(140,400),(160,400),(180,400),(200,400),(220,400),(240,400),(260,400),(280,400),(300,400),(320,400),(340,400),(360,400),(380,400),(400,400),(420,400),(440,400)]
green_coords = [(300,120),(440,160),(440,180),(520,160),(520,180),(100,200),(180,200),(40,240),(60,240),(60,320),(60,360),(280,280),(380,280),(400,280),(560,260),(560,280),(560,300),(580,300),(580,320),  (100,380),(120,380),(140,380),(160,380),(180,380),(200,380),(220,380),(240,380),(260,380),(280,380),(300,380),(320,380),(340,380),(360,380),(380,380),(400,380),(420,380),(440,380)]
blue_coords = [(400,80),(420,80),(440,80),(460,80),(480,80),(500,80),(520,80),(540,80),(560,80),(580,80),(400,100),(520,100),(400,120),(520,120),(400,140),(420,140),(440,140),(460,140),(500,140),(520,140),(540,140),(60,200),(80,200),(140,220),(520,240),(580,260),(580,280),(40,320),(80,340),(340,320),(540,320),(480,360),(560,360),   (100,420),(120,420),(140,420),(160,420),(180,420),(200,420),(220,420),(240,420),(260,420),(280,420),(300,420),(320,420),(340,420),(360,420),(380,420),(400,420),(420,420),(440,420)]

red_switch_coords = [(420,100),(300,160),(580,220),(280,240),(200,320),(480,320),(480,400)]
green_switch_coords = [(580,40),(300,60),(80,140),(540,220),(300,240),(380,240),(300,320),(380,320)]
blue_switch_coords = [(560,120),(560,220),(480,240),(40,280),(60,420),(280,320),(400,320),(540,340)]

redup = True
greenup = True
blup = True

while True:

    setDisplay.fill(lgray)

    for i in range(len(wall_coords)):

        setDisplay.blit(wall,(wall_coords[i]))

    if redup:
        for i in range(len(red_coords)):

            setDisplay.blit(red_barrier,(red_coords[i]))

    if greenup:
        for i in range(len(green_coords)):

            setDisplay.blit(green_barrier,(green_coords[i]))

    if blup:
        for i in range(len(blue_coords)):

            setDisplay.blit(blue_barrier,(blue_coords[i]))

    for i in range(len(red_switch_coords)):

        setDisplay.blit(red_switch,(red_switch_coords[i]))

    for i in range(len(green_switch_coords)):

        setDisplay.blit(green_switch,(green_switch_coords[i]))

    for i in range(len(blue_switch_coords)):

        setDisplay.blit(blue_switch,(blue_switch_coords[i]))

    setDisplay.blit(goal,(goalx,goaly))

    setDisplay.blit(player,(playerx,playery))

    for event in pygame.event.get():

        print(event)

        if event.type == QUIT:

            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN:

            if event.key == K_UP:

                last_direction = 'up'
                playery -= cellsize
                collisions()

            elif event.key == K_DOWN:

                last_direction = 'down'
                playery += cellsize
                collisions()

            elif event.key == K_LEFT:

                last_direction = 'left'
                playerx -= cellsize
                collisions()

            elif event.key == K_RIGHT:

                last_direction = 'right'
                playerx += cellsize
                collisions()



    pygame.display.update()
    fpsTime.tick(FPS)

