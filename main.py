import os
import pygame
import random

#initialize the pygame 'always there'
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600)) # 'width' & 'height' respectively in pixels

#background
background = pygame.image.load("background1.png")

#TITLE AND ICON
pygame.display.set_caption("Invasion")
logo = pygame.image.load('pirate.png')
pygame.display.set_icon(logo)

#PLAYER
player_img = pygame.image.load('jet.png')
playerX = 370
playerY = 450
playerX_change = 0.3

#ENEMY
enemy_img = pygame.image.load('alien(1).png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 1
enemyY_change = 32


#BULLET
#'hidden': bullet not visible
#'visible' : bullet is moving
bullet_img = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state = "hidden"


def player(x, y):
    screen.blit(player_img, (x,y)) # 'blit' means to draw

def enemy(x, y):
    screen.blit(enemy_img, (x,y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "visible"
    screen.blit(bullet_img, (x+16, y+10))

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
                playerX_change = -1.5

            if event.key == pygame.K_RIGHT:
                playerX_change = 1.5
            
            if event.key == pygame.K_SPACE:
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
    enemyX += enemyX_change

    if enemyX < 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "hidden"

    if bullet_state is "visible":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()  #always there

