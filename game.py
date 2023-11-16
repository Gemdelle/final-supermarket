import pygame

from sys import exit  # to exit the game without having issues with the True loop
from random import randint
import math

# Setup
pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # Create screen. This code ends, so to keep it running we use the while True (is never False).
pygame.display.set_caption('Bakery')
clock = pygame.time.Clock()  # clock object to handle frame rate
test_font = pygame.font.Font('font/Alkhemikal.ttf', 50)
game_active = True
running = True

# Bacgrkound & Store
background = pygame.image.load('graphics/welcome.png').convert_alpha()
background_rect = background.get_rect(center=(960, 120))

plate = pygame.image.load('graphics/plate.png')
plate_rect = plate.get_rect(center=(960, 600))

# Food
# breadturtle, 
food_bread_turtle = pygame.image.load('graphics/food-breadturtle.png')
food_bread_turtle = pygame.transform.scale(food_bread_turtle,(170,140))
food_bread_turtle_rect = food_bread_turtle.get_rect(center=(960, 600))

while running:  # The game will be continuously updated.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if game_active:
        screen.blit(background, background_rect)
        screen.blit(plate, plate_rect)
        screen.blit(food_bread_turtle, food_bread_turtle_rect)

    pygame.display.update() # update the screen
    clock.tick(60) # while True runs 60 times per second