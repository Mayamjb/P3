import pygame

# Get Items images
playerImg = pygame.image.load('MacGyver.png')
guardianImg = pygame.image.load('guardian.png')
bounderiesImg = pygame.image.load('bounderies.png')
needleImg = pygame.image.load('needle.png')
tubeImg = pygame.image.load('plastic_tube.png')
etherImg = pygame.image.load('ether.png')
syringeImg = pygame.image.load('transparent_syringe.png')
winning = pygame.image.load("winning.png")
loosingImg = pygame.image.load("loosing.png")

# Title and icon
pygame.display.set_caption("MacGyver Labyrinth")
icon = pygame.image.load('MacGyver.png')
pygame.display.set_icon(icon)
