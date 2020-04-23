import pygame  # always import the library
import random  # allows random functionality
import math
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
pygame.mixer.music.set_volume(0.2)  # value between 0.0 and 1.0

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 735))  # this depends on screen size
    enemyY.append(random.randint(50, 150))  # make sure to import random for randomized integers here
    enemyX_change.append(3)  # provides constant movement
    enemyY_change.append(30)  # this will move it down whe it hits border along with conditional statement below

# bullet
# Ready - you cant see the bullet on the screen
# Fire - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0  # this depends on screen size
bulletY = 480  # because spaceship is at 480 pixels
bulletX_change = 0
bulletY_change = 20  # speed of bullet
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10  # screen placement
textY = 10  # screen placement

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (0, 255, 0)) # text, value variable, display yes, color
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 255, 0))  # text, value variable, display yes, color
    screen.blit(over_text, (200, 250))

def player(x, y):  # player function
    screen.blit(playerImg, (x, y))  # this function will draw the icon to the screen


def enemy(x, y, i):  # player function
    screen.blit(enemyImg[i], (x, y))  # this function will draw the icon to the screen


def fire_bullet(x, y):
    global bullet_state  # make sure to write "global" to use the variable
    bullet_state = "fire"  # changes from "ready"
    screen.blit(bulletImg, (x + 16, y + 10))  # to make sure it fires and appears in the center of spaceship


# bullet enemy collision
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
                if bullet_state is "ready":  # checks if bullet is on screen or not
                    # bullet_sound = mixer.sound('')  # add .wav file
                    # bullet_sound.play()
                    bulletX = playerX  # if not it gets x coordinate of spaceship/ bulletX
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

    for i in range(num_of_enemies):
        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # this will make the enemy's disappear off screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]  # key movement functionality
        #  this part will create boundaries for the game
        if enemyX[i] <= 0:  # when the ship reaches boundaries it deletes it and reprints it at 0
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]  # this will move it down when it hits border
        elif enemyX[i] >= 736:  # taking in account for size of spaceship
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # collision_sound = mixer.sound('')  # add .wav file
            # collision_sound.play()
            bulletY = 480
            bulletX_change = 'ready'
            score_value += 1  # make sure score value is increasing by 1
            enemyX[i] = random.randint(0, 735)  # when hit the enemy wil restart at random pos
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:  # allowing multiple bullets to be fired
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)  # notice how this icon function is being called after the screen background
    show_score(textX,textY)  # call score function
    pygame.display.update()  # this will make sure the screen is always updating
