import os
import pygame
from pygame import mixer
import random
from math import sqrt, pow

#initialize the pygame 'always there'
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600)) # 'width' & 'height' respectively in pixels

#background
background = pygame.image.load("images/background1.png")

#music
mixer.music.load('audio/backgroundMusic.wav')
mixer.music.play(-1)


#TITLE AND ICON
pygame.display.set_caption("Invasion")
logo = pygame.image.load('images/pirate.png')
pygame.display.set_icon(logo)

#PLAYER
player_img = pygame.image.load('images/jet.png')
playerX = 370
playerY = 450
playerX_change = 0.3

#player_score
playerScore = 0
fontScore = pygame.font.Font('font/GRNORCH.ttf', 40)
fontGameOver = pygame.font.Font('font/Fidalga-Regular.ttf', 64)
textX = 10
textY =10

#SMALL ENEMY
numberEnemies = 6
enemy_img = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(numberEnemies):
    key = random.randint(1,2)
    enemy_img.append(pygame.image.load('images/alien'+str(key)+'.png'))
    #enemy_img.append(pygame.image.load('alien1.png'))
    enemyX.append(random.randint(0,730))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1)
    enemyY_change.append(32)

#BIG ENEMY
big_enemy_img = pygame.image.load(('images/alien_big.png'))
big_enemyX = random.randint(0,730)
big_enemyY = random.randint(50,90)
big_enemyX_change = 1.5
big_enemyY_change = 32

#BULLET
#'hidden': bullet not visible
#'visible' : bullet is moving
bullet_img = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3.5
bullet_state = "hidden"

def showScore(x, y):
    score = fontScore.render("Your Score:  " + str(playerScore), True, (0,255,25))
    screen.blit(score, (x,y))


def player(x, y):
    screen.blit(player_img, (x,y)) # 'blit' means to draw

def enemy(x, y, i):
    screen.blit(enemy_img[i], (x,y))

def big_enemy(x,y):
    screen.blit(big_enemy_img, (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "visible"
    screen.blit(bullet_img, (x+16, y-40))


def collision(enemyX, enemyY, bulletX, bulletY):
    
    distance_between_enemy_bullet = sqrt(pow((enemyX - bulletX), 2) + pow((enemyY - bulletY), 2))
    if (distance_between_enemy_bullet < 25):
        return True
    else:
        return False

def big_collision(big_enemyX, big_enemyY, bulletX, bulletY):
    
    distance_between_enemy_bullet = sqrt(pow((big_enemyX - bulletX), 2) + pow((big_enemyY - bulletY), 2))
    if (distance_between_enemy_bullet < 40):
        return True
    else:
        return False


def gameOver():
    over = fontGameOver.render("GAME OVER :(" + str(playerScore), True, (0,255,25))
    screen.blit(over, (200,250))

# GAME LOOP
flag = True
while flag:

    screen.fill((75,79,83)) #(R, G, B)
    #background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            flag = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 2.5
            
            if event.key == pygame.K_SPACE:
                if bullet_state == "hidden":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX +=playerX_change

    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


    #ENEMY BOUNDARY CHECK
    for i in range(numberEnemies):

        #GAME---OVER
        if (enemyY[i] > 430) or (big_enemyY > 430) :
            for j in range(1,numberEnemies):
                enemyY[j] = 5000 ##That's all folks :)
            big_enemyY = 5000
            gameOver()
            break

        enemyX[i] += enemyX_change[i]
        
        if enemyX[i] < 0:
            enemyX_change[i] = 1 + (playerScore/50)
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -(1 + (playerScore/50))
            enemyY[i] += enemyY_change[i]

        #collision with small enemy
        collide = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collide == True:
            enemyX[i] = random.randint(0,730)
            enemyY[i] = random.randint(50,150)
            bulletY = 480
            bullet_state = "hidden"
            playerScore += 1
        
        #collision with big enemy
        collide_big = big_collision(big_enemyX, big_enemyY, bulletX, bulletY)
        if collide_big == True:
            bulletY = 480
            bullet_state = "hidden"
            playerScore += 5

        enemy(enemyX[i], enemyY[i], i)
    
    #big enemy motion
    big_enemyX += big_enemyX_change
        
    if big_enemyX < 0:
        big_enemyX_change = 1 + (playerScore/20)
        big_enemyY += big_enemyY_change
    elif big_enemyX >= 736:
        big_enemyX_change = -(1 + (playerScore/20))
        big_enemyY += big_enemyY_change


    if (playerScore > 4):
        if (playerScore % 5 == 0):
            big_enemy(big_enemyX, big_enemyY) 

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "hidden"

    if bullet_state is "visible":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    player(playerX, playerY)
    showScore(textX, textY)
    pygame.display.update()  #always there
