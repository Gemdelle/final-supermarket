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
welcome = pygame.image.load('graphics/welcome.png').convert_alpha()
welcome_rect = welcome.get_rect(center = (960, 120))

glass = pygame.image.load('graphics/glass.png').convert_alpha()
glass_rect = glass.get_rect(center = (960, 550))

chat_container = pygame.image.load('graphics/chat-container.png').convert_alpha()
chat_container_rect = chat_container.get_rect(center = (960, 970))

ticket = pygame.image.load('graphics/ticket.png').convert_alpha()
ticket_rect = ticket.get_rect(center = (250,520))

plates_type = pygame.image.load('graphics/plates-catalogue.png').convert_alpha()
plates_type = pygame.transform.scale(plates_type,(530,380))
plates_type_rect = plates_type.get_rect(center = (1680, 970))

plate1 = pygame.image.load('graphics/plate1.png').convert_alpha()
plate1 = pygame.transform.scale(plate1,(170,210))
plate2 = pygame.image.load('graphics/plate2.png').convert_alpha()
plate2 = pygame.transform.scale(plate2,(170,210))
plate3 = pygame.image.load('graphics/plate3.png').convert_alpha()
plate3 = pygame.transform.scale(plate3,(170,210))
plate4 = pygame.image.load('graphics/plate4.png').convert_alpha()
plate4 = pygame.transform.scale(plate4,(170,210))
plate5 = pygame.image.load('graphics/plate5.png').convert_alpha()
plate5 = pygame.transform.scale(plate5,(170,210))
plate6 = pygame.image.load('graphics/plate6.png').convert_alpha()
plate6 = pygame.transform.scale(plate6,(170,210))

# Plain
plate1_rect = plate1.get_rect(center=(590, 390))
plate2_rect = plate1.get_rect(center=(790, 390))

# Zoo Bread
plate3_rect = plate2.get_rect(center=(990, 390))
plate4_rect = plate2.get_rect(center=(1190, 390))

# Toast
plate5_rect = plate3.get_rect(center=(1390, 390))
plate6_rect = plate3.get_rect(center=(1590, 390))

# Fruit Pie
plate7_rect = plate4.get_rect(center=(1780, 390))
plate8_rect = plate4.get_rect(center=(590, 640))
plate9_rect = plate4.get_rect(center=(790, 640))
plate10_rect = plate4.get_rect(center=(990, 640))
plate11_rect = plate4.get_rect(center=(1190, 640))

# Sandwich
plate12_rect = plate5.get_rect(center=(1390, 640))

# Bread
plate13_rect = plate6.get_rect(center=(1590, 640))
plate14_rect = plate6.get_rect(center=(1780, 640))

# FOOD -----------------------------------------------------------------------------------------------------------------
# Bread
food_baguette = pygame.image.load('graphics/food-baguette.png')
food_baguette = pygame.transform.scale(food_baguette,(170,140))
food_baguette_rect = food_baguette.get_rect(center=(590, 400))

food_roundbread = pygame.image.load('graphics/food-roundbread.png')
food_roundbread = pygame.transform.scale(food_roundbread,(170,140))
food_roundbread_rect = food_roundbread.get_rect(center=(790, 400))

# Zoo Bread
food_bread_turtle = pygame.image.load('graphics/food-breadturtle.png')
food_bread_turtle = pygame.transform.scale(food_bread_turtle,(170,140))
food_bread_turtle_rect = food_bread_turtle.get_rect(center=(990, 400))

food_bread_crocodile = pygame.image.load('graphics/food-breadcrocodile.png')
food_bread_crocodile = pygame.transform.scale(food_bread_crocodile,(170,140))
food_bread_crocodile_rect = food_bread_crocodile.get_rect(center=(1190, 400))

# Toast
food_eggtoast = pygame.image.load('graphics/food-eggtoast.png')
food_eggtoast = pygame.transform.scale(food_eggtoast,(170,140))
food_eggtoast_rect = food_eggtoast.get_rect(center=(1390, 400))

food_toast = pygame.image.load('graphics/food-toast.png')
food_toast = pygame.transform.scale(food_toast,(170,140))
food_toast_rect = food_toast.get_rect(center=(1590, 400))

# Fruit Pie
food_pie1 = pygame.image.load('graphics/food-pie1.png')
food_pie1 = pygame.transform.scale(food_pie1,(170,140))
food_pie1_rect = food_pie1.get_rect(center=(1780, 400))

food_pie2 = pygame.image.load('graphics/food-pie2.png')
food_pie2 = pygame.transform.scale(food_pie2,(170,140))
food_pie2_rect = food_pie2.get_rect(center=(590, 650))

food_rectpie = pygame.image.load('graphics/food-rectpie.png')
food_rectpie = pygame.transform.scale(food_rectpie,(170,140))
food_rectpie_rect = food_rectpie.get_rect(center=(790, 650))

food_fruitpie = pygame.image.load('graphics/food-fruitpie.png')
food_fruitpie = pygame.transform.scale(food_fruitpie,(170,140))
food_fruitpie_rect = food_fruitpie.get_rect(center=(990, 650))

food_blueberryfish = pygame.image.load('graphics/food-blueberryfish.png')
food_blueberryfish = pygame.transform.scale(food_blueberryfish,(170,140))
food_blueberryfish_rect = food_blueberryfish.get_rect(center=(1190, 650))

# Sandwich
food_bagel = pygame.image.load('graphics/food-bagel.png')
food_bagel = pygame.transform.scale(food_bagel,(170,140))
food_bagel_rect = food_bagel.get_rect(center=(1390, 650))

# Plain
food_pretzel = pygame.image.load('graphics/food-pretzel.png')
food_pretzel = pygame.transform.scale(food_pretzel,(170,140))
food_pretzel_rect = food_pretzel.get_rect(center=(1590, 650))

food_croissant = pygame.image.load('graphics/food-croissant.png')
food_croissant = pygame.transform.scale(food_croissant,(170,140))
food_croissant_rect = food_croissant.get_rect(center=(1780, 650))

while running:  # The game will be continuously updated.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    if game_active:
        screen.fill((255,255,255))
        screen.blit(glass, glass_rect)
        screen.blit(welcome, welcome_rect)
        screen.blit(chat_container, chat_container_rect)
        screen.blit(plates_type,plates_type_rect)

        # Ticket
        screen.blit(ticket,ticket_rect)

        # Plates
        # Line 1
        screen.blit(plate1, plate1_rect)
        screen.blit(food_baguette, food_baguette_rect)

        screen.blit(plate1, plate2_rect)
        screen.blit(food_roundbread, food_roundbread_rect)

        screen.blit(plate2, plate3_rect)
        screen.blit(food_bread_turtle,food_bread_turtle_rect)

        screen.blit(plate2, plate4_rect)
        screen.blit(food_bread_crocodile,food_bread_crocodile_rect)

        screen.blit(plate3, plate5_rect)
        screen.blit(food_eggtoast,food_eggtoast_rect)

        screen.blit(plate3, plate6_rect)
        screen.blit(food_toast,food_toast_rect)

        screen.blit(plate4, plate7_rect)
        screen.blit(food_pie1,food_pie1_rect)

        # Line 2

        screen.blit(plate4, plate8_rect)
        screen.blit(food_pie2,food_pie2_rect)

        screen.blit(plate4, plate9_rect)
        screen.blit(food_rectpie,food_rectpie_rect)

        screen.blit(plate4, plate10_rect)
        screen.blit(food_fruitpie,food_fruitpie_rect)

        screen.blit(plate4, plate11_rect)
        screen.blit(food_blueberryfish,food_blueberryfish_rect)

        screen.blit(plate5, plate12_rect)
        screen.blit(food_bagel,food_bagel_rect)

        screen.blit(plate6, plate13_rect)
        screen.blit(food_pretzel,food_pretzel_rect)

        screen.blit(plate6, plate14_rect)
        screen.blit(food_croissant,food_croissant_rect) 

    pygame.display.update() # update the screen
    clock.tick(60) # while True runs 60 times per second