import pygame
import random
import math
from pygame import mixer

pygame.init()

# Creating a screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('space_bg.jpg')

# Title and Icon
pygame.display.set_caption('Bob Invaders')
icon = pygame.image.load('bob_player.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('bob_player.png')
playerX = 370
playerY = 450
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('golden_enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(10, 150))
    enemyX_change.append(4)
    enemyY_change.append(30)

# Laser
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 430
laserX_change = 0
laserY_change = 7
laser_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 24)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text(x, y):
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_laser(x, y):
    global laser_state
    laser_state = 'fire'
    screen.blit(laserImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, laserX, laserY):
    distance = math.sqrt(math.pow((enemyX - laserX), 2) + math.pow(enemyY - laserY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:
    screen.fill((52, 151, 162))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check the direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if laser_state is 'ready':
                    laser_sound = mixer.Sound('laser_sound.wav')
                    laser_sound.play()
                    laserX = playerX
                    fire_laser(playerX, laserY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Making sure bob doesn't pass the window limit
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Making sure enemies doesn't pass the window limit
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text(200, 250)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], laserX, laserY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            laserY = 480
            laser_state = 'ready'
            score_value += 1
            print('Score: ', score_value)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(64, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Laser movement
    if laserY <= 0:
        laserY = 430
        laser_state = 'ready'
    if laser_state is 'fire':
        fire_laser(laserX, laserY)
        laserY -= laserY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()