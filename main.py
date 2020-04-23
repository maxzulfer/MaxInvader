import pygame  # always import the library
import random  # allows random functionality
from pygame import mixer  # import if you want music

# initialize the game every time
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))  # x-axis 800 pixels y-axis 600 pixels

# create the background image
background = pygame.image.load('background.png')

# background music
mixer.music.load('Max_Invader.wav')
mixer.music.play(-1)  # Plays the wav in a loop

# Title and Icon
pygame.display.set_caption("Max Invader")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370  # this depends on screen size
playerY = 480  # this depends on screen size
playerX_change = 0  # speed it starts at

# Enemy
enemyImg = pygame.image.load('ufo.png')
enemyX = random.randint(0, 800)  # this depends on screen size
enemyY = random.randint(50, 150)  # make sure to import random for randomized integers here
enemyX_change = 3  # provides constant movement
enemyY_change = 0
enemyY_change = 30  # this will move it down whe it hits border along with conditional statement below

# bullet
# Ready - you cant see the bullet on the screen
# Fire - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0  # this depends on screen size
bulletY = 480  # because spaceship is at 480 pixels
bulletX_change = 0
bulletY_change = 30  # speed of bullet
bullet_state = "ready"


def player(x, y):  # player function
    screen.blit(playerImg, (x, y))  # this function will draw the icon to the screen


def enemy(x, y):  # player function
    screen.blit(enemyImg, (x, y))  # this function will draw the icon to the screen


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"  # changes from "ready"
    screen.blit(bulletImg, (x + 16, y + 10))  # to make sure it appears in the center of spaceship


# Game Loop. Anything that is constant will live in this loop
running = True
while running:
    # background color
    screen.fill((0, 0, 0))  # everything should be drawn on top of this screen
    # background image
    screen.blit(background, (0, 0))  # get background variable and set it to top left corner
    # playerX -= 0  # movement functionality speed constant
    for event in pygame.event.get():  # function which keeps the game running
        if event.type == pygame.QUIT:
            running = False

        # if a key stroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:  # looks for any key being pressed down
            if event.key == pygame.K_LEFT:  # looks for which key
                playerX_change = -4  # how fast the spaceship will move left/right
            if event.key == pygame.K_RIGHT:
                playerX_change = 4  # how fast the spaceship will move from left/right
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)  # calls fire bullet function

        if event.type == pygame.KEYUP:  # when a key stroke has been released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # when the key is released, the spaceship stops moving

    playerX += playerX_change  # key movement functionality

    #  this part will create boundaries for the game
    if playerX <= 0:  # when the ship reaches boundaries it deletes it and reprints it at 0
        playerX = 0
    elif playerX >= 736:  # taking in account for size of spaceship
        playerX = 736

    enemyX += enemyX_change  # key movement functionality

    #  this part will create boundaries for the game
    if enemyX <= 0:  # when the ship reaches boundaries it deletes it and reprints it at 0
        enemyX_change = 3
        enemyY += enemyY_change  # this will move it down when it hits border
    elif enemyX >= 736:  # taking in account for size of spaceship
        enemyX_change = -3
        enemyY += enemyY_change

    # Bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletX -= bulletY_change

    player(playerX, playerY)  # notice how this icon function is being called after the screen background
    enemy(enemyX, enemyY)
    pygame.display.update()  # this will make sure the screen is always updating
