import pygame

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


def player():  # player function
    screen.blit(playerImg, (playerX, playerY))  # this function will draw the icon to the screen


# Game Loop. Anything that is constant will live in this loop
running = True
while running:
    # background color
    screen.fill((0, 0, 0))  # everything should be drawn on top of this screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()  # notice how this icon function is being called after the screen background
    pygame.display.update()  # this will make sure the screen is always updating
