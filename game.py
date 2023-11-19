from datetime import datetime

import pygame

from sys import exit  # to exit the game without having issues with the True loop
from random import randint
import math

from pygame import font

from supermercado import buy_with_code, createStock, bakery_products, return_product, discountItem


def update_ticket():
    global current_y, total_price, products_text
    keys_list = list(cart.keys())
    aux_total_prize = 0
    for product_code, product in product_list.items():
        try:
            if product['description'] in cart and cart[product['description']]['quantity'] > 0:
                index = keys_list.index(product['description'])
                products_text[product['description']] = {
                    'quantity': cart[product['description']]['quantity'],
                    'price': product['price'],
                    'position_y': current_y + (PRODUCT_HEIGHT * index)
                }
                aux_total_prize += cart[product['description']]['pay']
            else:
                del products_text[product['description']]

        except KeyError as e:
            pass

    total_price = aux_total_prize

def render_plate1():
    screen.blit(plate1, plate1_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['107']['stock']}",
        True, 'Black'
    ), (plate1_rect.centerx - 16, plate1_rect.centery + 80))


def render_plate2():
    screen.blit(plate1, plate2_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['108']['stock']}",
        True, 'Black'
    ), (plate2_rect.centerx - 16, plate2_rect.centery + 80))


def render_plate3():
    screen.blit(plate2, plate3_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['105']['stock']}",
        True, 'Black'
    ), (plate3_rect.centerx - 16, plate3_rect.centery + 80))


def render_plate4():
    screen.blit(plate2, plate4_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['106']['stock']}",
        True, 'Black'
    ), (plate4_rect.centerx - 16, plate4_rect.centery + 80))


def render_plate5():
    screen.blit(plate3, plate5_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['109']['stock']}",
        True, 'Black'
    ), (plate5_rect.centerx - 16, plate5_rect.centery + 80))


def render_plate6():
    screen.blit(plate3, plate6_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['110']['stock']}",
        True, 'Black'
    ), (plate6_rect.centerx - 16, plate6_rect.centery + 80))


def render_plate7():
    screen.blit(plate4, plate7_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['100']['stock']}",
        True, 'Black'
    ), (plate7_rect.centerx - 16, plate7_rect.centery + 80))


def render_plate8():
    screen.blit(plate4, plate8_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['101']['stock']}",
        True, 'Black'
    ), (plate8_rect.centerx - 16, plate8_rect.centery + 80))


def render_plate9():
    screen.blit(plate4, plate9_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['102']['stock']}",
        True, 'Black'
    ), (plate9_rect.centerx - 16, plate9_rect.centery + 80))


def render_plate10():
    screen.blit(plate4, plate10_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['103']['stock']}",
        True, 'Black'
    ), (plate10_rect.centerx - 16, plate10_rect.centery + 80))


def render_plate11():
    screen.blit(plate4, plate11_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['104']['stock']}",
        True, 'Black'
    ), (plate11_rect.centerx - 16, plate11_rect.centery + 80))


def render_plate12():
    screen.blit(plate5, plate12_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['113']['stock']}",
        True, 'Black'
    ), (plate12_rect.centerx - 16, plate12_rect.centery + 80))


def render_plate13():
    screen.blit(plate6, plate13_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['111']['stock']}",
        True, 'Black'
    ), (plate13_rect.centerx - 16, plate13_rect.centery + 80))


def render_plate14():
    screen.blit(plate6, plate14_rect)
    screen.blit(ticket_products_font.render(
        f"{product_list['112']['stock']}",
        True, 'Black'
    ), (plate14_rect.centerx - 16, plate14_rect.centery + 80))

def check_add_product():
    if food_pie1_rect.collidepoint(event.pos) and product_list['100']['stock'] > 0:
        buy_with_code(product_list, cart, '100')
        update_ticket()
    elif food_pie2_rect.collidepoint(event.pos) and product_list['101']['stock'] > 0:
        buy_with_code(product_list, cart, '101')
        update_ticket()
    elif food_rectpie_rect.collidepoint(event.pos) and product_list['102']['stock'] > 0:
        buy_with_code(product_list, cart, '102')
        update_ticket()
    elif food_fruitpie_rect.collidepoint(event.pos) and product_list['103']['stock'] > 0:
        buy_with_code(product_list, cart, '103')
        update_ticket()
    elif food_blueberryfish_rect.collidepoint(event.pos) and product_list['104']['stock'] > 0:
        buy_with_code(product_list, cart, '104')
        update_ticket()
    elif food_bread_turtle_rect.collidepoint(event.pos) and product_list['105']['stock'] > 0:
        buy_with_code(product_list, cart, '105')
        update_ticket()
    elif food_bread_crocodile_rect.collidepoint(event.pos) and product_list['106']['stock'] > 0:
        buy_with_code(product_list, cart, '106')
        update_ticket()
    elif food_baguette_rect.collidepoint(event.pos) and product_list['107']['stock'] > 0:
        buy_with_code(product_list, cart, '107')
        update_ticket()
    elif food_roundbread_rect.collidepoint(event.pos) and product_list['108']['stock'] > 0:
        buy_with_code(product_list, cart, '108')
        update_ticket()
    elif food_eggtoast_rect.collidepoint(event.pos) and product_list['109']['stock'] > 0:
        buy_with_code(product_list, cart, '109')
        update_ticket()
    elif food_toast_rect.collidepoint(event.pos) and product_list['110']['stock'] > 0:
        buy_with_code(product_list, cart, '110')
        update_ticket()
    elif food_pretzel_rect.collidepoint(event.pos) and product_list['111']['stock'] > 0:
        buy_with_code(product_list, cart, '111')
        update_ticket()
    elif food_croissant_rect.collidepoint(event.pos) and product_list['112']['stock'] > 0:
        buy_with_code(product_list, cart, '112')
        update_ticket()
    elif food_bagel_rect.collidepoint(event.pos) and product_list['113']['stock'] > 0:
        buy_with_code(product_list, cart, '113')
        update_ticket()

def check_remove_product():
    if food_pie1_rect.collidepoint(event.pos) and product_list['100']['stock'] > 0:
        return_product(product_list, cart, '100')
        update_ticket()
    elif food_pie2_rect.collidepoint(event.pos) and product_list['101']['stock'] > 0:
        return_product(product_list, cart, '101')
        update_ticket()
    elif food_rectpie_rect.collidepoint(event.pos) and product_list['102']['stock'] > 0:
        return_product(product_list, cart, '102')
        update_ticket()
    elif food_fruitpie_rect.collidepoint(event.pos) and product_list['103']['stock'] > 0:
        return_product(product_list, cart, '103')
        update_ticket()
    elif food_blueberryfish_rect.collidepoint(event.pos) and product_list['104']['stock'] > 0:
        return_product(product_list, cart, '104')
        update_ticket()
    elif food_bread_turtle_rect.collidepoint(event.pos) and product_list['105']['stock'] > 0:
        return_product(product_list, cart, '105')
        update_ticket()
    elif food_bread_crocodile_rect.collidepoint(event.pos) and product_list['106']['stock'] > 0:
        return_product(product_list, cart, '106')
        update_ticket()
    elif food_baguette_rect.collidepoint(event.pos) and product_list['107']['stock'] > 0:
        return_product(product_list, cart, '107')
        update_ticket()
    elif food_roundbread_rect.collidepoint(event.pos) and product_list['108']['stock'] > 0:
        return_product(product_list, cart, '108')
        update_ticket()
    elif food_eggtoast_rect.collidepoint(event.pos) and product_list['109']['stock'] > 0:
        return_product(product_list, cart, '109')
        update_ticket()
    elif food_toast_rect.collidepoint(event.pos) and product_list['110']['stock'] > 0:
        return_product(product_list, cart, '110')
        update_ticket()
    elif food_pretzel_rect.collidepoint(event.pos) and product_list['111']['stock'] > 0:
        return_product(product_list, cart, '111')
        update_ticket()
    elif food_croissant_rect.collidepoint(event.pos) and product_list['112']['stock'] > 0:
        return_product(product_list, cart, '112')
        update_ticket()
    elif food_bagel_rect.collidepoint(event.pos) and product_list['113']['stock'] > 0:
        return_product(product_list, cart, '113')
        update_ticket()

# Setup
pygame.init()
PRODUCT_HEIGHT = 30
MARGIN = 60
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # Create screen. This code ends, so to keep it running we use the while True (is never False).
pygame.display.set_caption('Bakery')
clock = pygame.time.Clock()  # clock object to handle frame rate
test_font = pygame.font.Font('font/Alkhemikal.ttf', 50)
ticket_products_font = pygame.font.Font('font/Alkhemikal.ttf', 35)
products_count_font = pygame.font.Font('font/Alkhemikal.ttf', 35)
game_active = True
running = True

# Bacgrkound & Store
welcome = pygame.image.load('graphics/welcome.png').convert_alpha()
welcome_rect = welcome.get_rect(center=(960, 120))

glass = pygame.image.load('graphics/glass.png').convert_alpha()
glass_rect = glass.get_rect(center=(960, 550))

chat_container = pygame.image.load('graphics/chat-container.png').convert_alpha()
chat_container_rect = chat_container.get_rect(center=(960, 970))

ticket = pygame.image.load('graphics/ticket.png').convert_alpha()
ticket_rect = ticket.get_rect(center=(250, 520))

current_y = 350

plates_type = pygame.image.load('graphics/plates-catalogue.png').convert_alpha()
plates_type = pygame.transform.scale(plates_type, (530, 380))
plates_type_rect = plates_type.get_rect(center=(1680, 970))

plate1 = pygame.image.load('graphics/plate1.png').convert_alpha()
plate1 = pygame.transform.scale(plate1, (170, 210))
plate2 = pygame.image.load('graphics/plate2.png').convert_alpha()
plate2 = pygame.transform.scale(plate2, (170, 210))
plate3 = pygame.image.load('graphics/plate3.png').convert_alpha()
plate3 = pygame.transform.scale(plate3, (170, 210))
plate4 = pygame.image.load('graphics/plate4.png').convert_alpha()
plate4 = pygame.transform.scale(plate4, (170, 210))
plate5 = pygame.image.load('graphics/plate5.png').convert_alpha()
plate5 = pygame.transform.scale(plate5, (170, 210))
plate6 = pygame.image.load('graphics/plate6.png').convert_alpha()
plate6 = pygame.transform.scale(plate6, (170, 210))

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
food_baguette = pygame.transform.scale(food_baguette, (170, 140))
food_baguette_rect = food_baguette.get_rect(center=(590, 400))

food_baguette_NS = pygame.image.load('graphics/food-baguette-NS.png')
food_baguette_NS = pygame.transform.scale(food_baguette_NS, (170, 140))
food_baguette_NS_rect = food_baguette_NS.get_rect(center=(590, 400))

food_roundbread = pygame.image.load('graphics/food-roundbread.png')
food_roundbread = pygame.transform.scale(food_roundbread, (170, 140))
food_roundbread_rect = food_roundbread.get_rect(center=(790, 400))

food_roundbread_NS = pygame.image.load('graphics/food-roundbread-NS.png')
food_roundbread_NS = pygame.transform.scale(food_roundbread_NS, (170, 140))
food_roundbread_NS_rect = food_roundbread_NS.get_rect(center=(790, 400))

# Zoo Bread
food_bread_turtle = pygame.image.load('graphics/food-breadturtle.png')
food_bread_turtle = pygame.transform.scale(food_bread_turtle, (170, 140))
food_bread_turtle_rect = food_bread_turtle.get_rect(center=(990, 400))

food_bread_turtle_NS = pygame.image.load('graphics/food-breadturtle-NS.png')
food_bread_turtle_NS = pygame.transform.scale(food_bread_turtle_NS, (170, 140))
food_bread_turtle_NS_rect = food_bread_turtle_NS.get_rect(center=(990, 400))

food_bread_crocodile = pygame.image.load('graphics/food-breadcrocodile.png')
food_bread_crocodile = pygame.transform.scale(food_bread_crocodile, (170, 140))
food_bread_crocodile_rect = food_bread_crocodile.get_rect(center=(1190, 400))

food_bread_crocodile_NS = pygame.image.load('graphics/food-breadcrocodile-NS.png')
food_bread_crocodile_NS = pygame.transform.scale(food_bread_crocodile_NS, (170, 140))
food_bread_crocodile_NS_rect = food_bread_crocodile_NS.get_rect(center=(1190, 400))

# Toast
food_eggtoast = pygame.image.load('graphics/food-eggtoast.png')
food_eggtoast = pygame.transform.scale(food_eggtoast, (170, 140))
food_eggtoast_rect = food_eggtoast.get_rect(center=(1390, 400))

food_eggtoast_NS = pygame.image.load('graphics/food-eggtoast-NS.png')
food_eggtoast_NS = pygame.transform.scale(food_eggtoast_NS, (170, 140))
food_eggtoast_NS_rect = food_eggtoast_NS.get_rect(center=(1390, 400))

food_toast = pygame.image.load('graphics/food-toast.png')
food_toast = pygame.transform.scale(food_toast, (170, 140))
food_toast_rect = food_toast.get_rect(center=(1590, 400))

food_toast_NS = pygame.image.load('graphics/food-toast-NS.png')
food_toast_NSt = pygame.transform.scale(food_toast_NS, (170, 140))
food_toast_NS_rect = food_toast_NS.get_rect(center=(1590, 400))

# Fruit Pie
food_pie1 = pygame.image.load('graphics/food-pie1.png')
food_pie1 = pygame.transform.scale(food_pie1, (170, 140))
food_pie1_rect = food_pie1.get_rect(center=(1780, 400))

food_pie1_NS = pygame.image.load('graphics/food-pie1-NS.png')
food_pie1_NS = pygame.transform.scale(food_pie1_NS, (170, 140))
food_pie1_NS_rect = food_pie1_NS.get_rect(center=(1780, 400))

food_pie2 = pygame.image.load('graphics/food-pie2.png')
food_pie2 = pygame.transform.scale(food_pie2, (170, 140))
food_pie2_rect = food_pie2.get_rect(center=(590, 650))

food_pie2_NS = pygame.image.load('graphics/food-pie2-NS.png')
food_pie2_NS = pygame.transform.scale(food_pie2_NS, (170, 140))
food_pie2_NS_rect = food_pie2_NS.get_rect(center=(590, 650))

food_rectpie = pygame.image.load('graphics/food-rectpie.png')
food_rectpie = pygame.transform.scale(food_rectpie, (170, 140))
food_rectpie_rect = food_rectpie.get_rect(center=(790, 650))

food_rectpie_NS = pygame.image.load('graphics/food-rectpie-NS.png')
food_rectpie_NS = pygame.transform.scale(food_rectpie_NS, (170, 140))
food_rectpie_NS_rect = food_rectpie_NS.get_rect(center=(790, 650))

food_fruitpie = pygame.image.load('graphics/food-fruitpie.png')
food_fruitpie = pygame.transform.scale(food_fruitpie, (170, 140))
food_fruitpie_rect = food_fruitpie.get_rect(center=(990, 650))

food_fruitpie_NS = pygame.image.load('graphics/food-fruitpie-NS.png')
food_fruitpie_NS = pygame.transform.scale(food_fruitpie_NS, (170, 140))
food_fruitpie_NS_rect = food_fruitpie_NS.get_rect(center=(990, 650))

food_blueberryfish = pygame.image.load('graphics/food-blueberryfish.png')
food_blueberryfish = pygame.transform.scale(food_blueberryfish, (170, 140))
food_blueberryfish_rect = food_blueberryfish.get_rect(center=(1190, 650))

food_blueberryfish_NS = pygame.image.load('graphics/food-blueberryfish-NS.png')
food_blueberryfish_NS = pygame.transform.scale(food_blueberryfish_NS, (170, 140))
food_blueberryfish_NS_rect = food_blueberryfish_NS.get_rect(center=(1190, 650))

# Sandwich
food_bagel = pygame.image.load('graphics/food-bagel.png')
food_bagel = pygame.transform.scale(food_bagel, (170, 140))
food_bagel_rect = food_bagel.get_rect(center=(1390, 650))

food_bagel_NS = pygame.image.load('graphics/food-bagel-NS.png')
food_bagel_NS = pygame.transform.scale(food_bagel_NS, (170, 140))
food_bagel_NS_rect = food_bagel_NS.get_rect(center=(1390, 650))

# Plain
food_pretzel = pygame.image.load('graphics/food-pretzel.png')
food_pretzel = pygame.transform.scale(food_pretzel, (170, 140))
food_pretzel_rect = food_pretzel.get_rect(center=(1590, 650))

food_pretzel_NS = pygame.image.load('graphics/food-pretzel-NS.png')
food_pretzel_NS = pygame.transform.scale(food_pretzel_NS, (170, 140))
food_pretzel_NS_rect = food_pretzel_NS.get_rect(center=(1590, 650))

food_croissant = pygame.image.load('graphics/food-croissant.png')
food_croissant = pygame.transform.scale(food_croissant, (170, 140))
food_croissant_rect = food_croissant.get_rect(center=(1780, 650))

food_croissant_NS = pygame.image.load('graphics/food-croissant-NS.png')
food_croissant_NS = pygame.transform.scale(food_croissant_NS, (170, 140))
food_croissant_NS_rect = food_croissant_NS.get_rect(center=(1780, 650))

discount_badge = pygame.image.load('graphics/food-blueberryfish.png')
discount_badge = pygame.transform.scale(discount_badge, (80, 50))
discount_badge_rect = discount_badge.get_rect(center=(1190, 650))

cart = {}
start_date = datetime.now()
product_list = createStock(bakery_products, start_date)
discountItem(start_date.day, start_date.month, product_list)
total_price = 0

products_text = {}

ticket_components = {}




while running:  # The game will be continuously updated.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left Click del Mouse
                check_add_product()
            elif event.button == 3: # Right Click del Mouse
                check_remove_product()

    if game_active:
        screen.fill((255, 255, 255))
        screen.blit(glass, glass_rect)
        screen.blit(welcome, welcome_rect)
        screen.blit(chat_container, chat_container_rect)
        screen.blit(plates_type, plates_type_rect)

        # Ticket
        screen.blit(ticket, ticket_rect)

        for name, product_component in products_text.items():
            component = ticket_products_font.render(
                f"{name}: {product_component['quantity']} x ${product_component['price']} = ${product_component['quantity'] * product_component['price']}",
                True, 'Black')

            screen.blit(component, (MARGIN, product_component['position_y']))

        # Display total price
        total_price_text = test_font.render(f"${total_price}", True, 'Black')
        screen.blit(total_price_text, (250, 700))

        # Plates
        # Line 1
        render_plate1()
        render_plate2()
        render_plate3()
        render_plate4()
        render_plate5()
        render_plate6()
        render_plate7()
        # Line 2
        render_plate8()
        render_plate9()
        render_plate10()
        render_plate11()
        render_plate12()
        render_plate13()
        render_plate14()

        if product_list['100']['stock'] > 0:
            screen.blit(food_pie1, food_pie1_rect)
            if product_list['100']['discount']:
                screen.blit(discount_badge, (food_pie1_rect.centerx - 16, food_pie1_rect.centery + 80))
        else:
            screen.blit(food_pie1_NS, food_pie1_NS_rect)

        if product_list['101']['stock'] > 0:
            screen.blit(food_pie2, food_pie2_rect)
            if product_list['101']['discount']:
                screen.blit(discount_badge, (food_pie2_rect.centerx - 16, food_pie2_rect.centery + 80))
        else:
            screen.blit(food_pie2_NS, food_pie2_NS_rect)

        if product_list['102']['stock'] > 0:
            screen.blit(food_rectpie, food_rectpie_rect)
            if product_list['102']['discount']:
                screen.blit(discount_badge, (food_rectpie_rect.centerx - 16, food_rectpie_rect.centery + 80))
        else:
            screen.blit(food_rectpie_NS, food_rectpie_NS_rect)

        if product_list['103']['stock'] > 0:
            screen.blit(food_fruitpie, food_fruitpie_rect)
            if product_list['103']['discount']:
                screen.blit(discount_badge, (food_fruitpie_rect.centerx - 16, food_fruitpie_rect.centery + 80))
        else:
            screen.blit(food_fruitpie_NS, food_fruitpie_NS_rect)

        if product_list['104']['stock'] > 0:
            screen.blit(food_blueberryfish, food_blueberryfish_rect)
            if product_list['104']['discount']:
                screen.blit(discount_badge, (food_blueberryfish_rect.centerx - 16, food_blueberryfish_rect.centery + 80))
        else:
            screen.blit(food_blueberryfish_NS, food_blueberryfish_NS_rect)

        if product_list['105']['stock'] > 0:
            screen.blit(food_bread_turtle, food_bread_turtle_rect)
            if product_list['105']['discount']:
                screen.blit(discount_badge, (food_bread_turtle_rect.centerx - 16, food_bread_turtle_rect.centery + 80))
        else:
            screen.blit(food_bread_turtle_NS, food_bread_turtle_NS_rect)

        if product_list['106']['stock'] > 0:
            screen.blit(food_bread_crocodile, food_bread_crocodile_rect)
            if product_list['106']['discount']:
                screen.blit(discount_badge, (food_bread_crocodile_rect.centerx - 16, food_bread_crocodile_rect.centery + 80))
        else:
            screen.blit(food_bread_crocodile_NS, food_bread_crocodile_NS_rect)

        if product_list['107']['stock'] > 0:
            screen.blit(food_baguette, food_baguette_rect)
            if product_list['107']['discount']:
                screen.blit(discount_badge, (food_baguette_rect.centerx - 16, food_baguette_rect.centery + 80))
        else:
            screen.blit(food_baguette_NS, food_baguette_NS_rect)

        if product_list['108']['stock'] > 0:
            screen.blit(food_roundbread, food_roundbread_rect)
            if product_list['108']['discount']:
                screen.blit(discount_badge, (food_roundbread_rect.centerx - 16, food_roundbread_rect.centery + 80))
        else:
            screen.blit(food_roundbread_NS, food_roundbread_NS_rect)

        if product_list['109']['stock'] > 0:
            screen.blit(food_eggtoast, food_eggtoast_rect)
            if product_list['109']['discount']:
                screen.blit(discount_badge, (food_eggtoast_rect.centerx - 16, food_eggtoast_rect.centery + 80))
        else:
            screen.blit(food_eggtoast_NS, food_eggtoast_NS_rect)

        if product_list['110']['stock'] > 0:
            screen.blit(food_toast, food_toast_rect)
            if product_list['110']['discount']:
                screen.blit(discount_badge, (food_toast_rect.centerx - 16, food_toast_rect.centery + 80))
        else:
            screen.blit(food_toast_NS, food_toast_NS_rect)

        if product_list['111']['stock'] > 0:
            screen.blit(food_pretzel, food_pretzel_rect)
            if product_list['111']['discount']:
                screen.blit(discount_badge, (food_pretzel_rect.centerx - 16, food_pretzel_rect.centery + 80))
        else:
            screen.blit(food_pretzel_NS, food_pretzel_NS_rect)

        if product_list['112']['stock'] > 0:
            screen.blit(food_croissant, food_croissant_rect)
            if product_list['112']['discount']:
                screen.blit(discount_badge, (food_croissant_rect.centerx - 16, food_croissant_rect.centery + 80))
        else:
            screen.blit(food_croissant_NS, food_croissant_NS_rect)

        if product_list['113']['stock'] > 0:
            screen.blit(food_bagel, food_bagel_rect)
            if product_list['113']['discount']:
                screen.blit(discount_badge, (food_bagel_rect.centerx - 16, food_bagel_rect.centery + 80))
        else:
            screen.blit(food_bagel_NS, food_bagel_NS_rect)

    pygame.display.update()  # update the screen
    clock.tick(60)  # while True runs 60 times per second
