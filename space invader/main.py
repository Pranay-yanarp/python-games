import pygame
import random
import math

# initialize pygame
pygame.init()


# display screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("space invader")
icon = pygame.image.load("spaceicon.png")
pygame.display.set_icon(icon)

# adding background
background = pygame.image.load('background1.jpg')

# space hero coordinates
playerimg = pygame.image.load('spacehero.png')
spacex = 370
spacey = 480
spacex_change = 0

# space enemy
enemyimg = []
enemyx =[]
enemyy =[]
enemyx_change =[]
enemyy_change =[]
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('enemyship.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(2)
    enemyy_change.append(40)

# bullet
bulletimg = pygame.image.load('bullet.png')
bulletx = 0
bullety = 480
bullety_change = 5
bullet_state = 'ready'

# score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)

textx=10
texty=10

# display score

def show_score(x,y):
    score=font.render('Score : '+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# player display on screen
def player(x, y):
    screen.blit(playerimg, (x, y))


# enemy display on screen

def enemy(x, y,i):
    screen.blit(enemyimg[i], (x, y))

# collision

def iscollision(x1,y1,x2,y2):
    distance= math.sqrt((math.pow(x1-x2,2))+(math.pow(y1-y2,2)))
    if distance<=27:
        return True
    else:
        return False

# bullet display on screen

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimg, (x + 16, y + 10))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))  # adds colour to the screen
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spacex_change = -2
            elif event.key == pygame.K_RIGHT:
                spacex_change = 2
            elif event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletx=spacex
                    fire_bullet(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spacex_change = 0
    spacex += spacex_change
    if spacex <= 0:
        spacex = 0
    elif spacex >= 736:
        spacex = 736

    # enemy movement

    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 2
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -2
            enemyy[i] += enemyy_change[i]

        # collision
        collision = iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullety = 480
            bullet_state = 'ready'
            enemyx[i] = random.randint(0, 735)
            enemyy[i] = random.randint(50, 150)
            score_value += 1

        enemy(enemyx[i],enemyy[i],i)
    # bullet movement
    if bullety<=0:
        bullety=480
        bullet_state='ready'
    if bullet_state is 'fire':
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change




    player(spacex, spacey)  # calling player function
    show_score(textx,texty)
    pygame.display.update()
