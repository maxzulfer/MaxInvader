import pygame  # always import the library

# initialize the game every time
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))  # x-axis 800 pixels y-axis 600 pixels

# Title and Icon
pygame.display.set_caption("Max Invader")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370  # this depends on screen size
playerY = 480  # this depends on screen size
playerX_change = 0

def player(x, y):  # player function
    screen.blit(playerImg, (x, y))  # this function will draw the icon to the screen


# Game Loop. Anything that is constant will live in this loop
running = True
while running:
    # background color
    screen.fill((0, 0, 0))  # everything should be drawn on top of this screen
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
        if event.type == pygame.KEYUP:  # when a key stroke has been released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # when the key is released, the spaceship stops moving

    playerX += playerX_change
    player(playerX, playerY)  # notice how this icon function is being called after the screen background
    pygame.display.update()  # this will make sure the screen is always updating
