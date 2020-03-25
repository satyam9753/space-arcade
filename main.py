import pygame

#initialize the pygame 'always there'
pygame.init()

#creating the screen
screen = pygame.display.set_mode((800, 600)) # 'width' & 'height' respectively in pixels

#TITLE AND ICON
pygame.display.set_caption("Invasion")
logo = pygame.image.load('pirate.png')
pygame.display.set_icon(logo)

#player
player_img = pygame.image.load('poison.png')
playerX = 370
playerY = 450

def player():
    screen.blit(player_img, (playerX, playerY)) # 'blit' means to draw

# GAME LOOP
flag = True

while flag:

    screen.fill((100,0,210)) #(R, G, B)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    

    player()
    pygame.display.update()  #always there

    #3029