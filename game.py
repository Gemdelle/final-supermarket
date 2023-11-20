from datetime import datetime

import pygame

from sys import exit  # to exit the game without having issues with the True loop
from random import randint
import math

from supermercado import buy_with_code, createStock, bakery_products, return_product, discountItem, add_product, \
    remove_product, increment_price_by_percentage, decrement_price_by_percentage, update_product_stock


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
    screen.blit(plate6, plate1_rect)
    screen.blit(products_count_font.render(
        f"{product_list['115']['stock']}",
        True, 'Black'
    ), (plate1_rect.centerx - 16, plate1_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['115']['price']}",
        True, 'Black'
    ), (plate1_rect.centerx - 25, plate1_rect.centery - 95 ))

def render_plate1_NS():
    screen.blit(plate6_NS, plate1_NS_rect)

def render_plate2():
    screen.blit(plate1, plate2_rect)
    screen.blit(products_count_font.render(
        f"{product_list['107']['stock']}",
        True, 'Black'
    ), (plate2_rect.centerx - 16, plate2_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['107']['price']}",
        True, 'Black'
    ), (plate2_rect.centerx - 25, plate2_rect.centery - 95))

def render_plate2_NS():
    screen.blit(plate1_NS, plate2_NS_rect)

def render_plate3():
    screen.blit(plate1, plate3_rect)
    screen.blit(products_count_font.render(
        f"{product_list['108']['stock']}",
        True, 'Black'
    ), (plate3_rect.centerx - 16, plate3_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['108']['price']}",
        True, 'Black'
    ), (plate3_rect.centerx - 25, plate3_rect.centery - 95))

def render_plate3_NS():
    screen.blit(plate1_NS, plate3_NS_rect)

def render_plate4():
    screen.blit(plate1, plate4_rect)
    screen.blit(products_count_font.render(
        f"{product_list['111']['stock']}",
        True, 'Black'
    ), (plate4_rect.centerx - 16, plate4_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['111']['price']}",
        True, 'Black'
    ), (plate4_rect.centerx - 25, plate4_rect.centery - 95))

def render_plate4_NS():
    screen.blit(plate1_NS, plate4_NS_rect)

def render_plate5():
    screen.blit(plate1, plate5_rect)
    screen.blit(products_count_font.render(
        f"{product_list['112']['stock']}",
        True, 'Black'
    ), (plate5_rect.centerx - 16, plate5_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['112']['price']}",
        True, 'Black'
    ), (plate5_rect.centerx - 25, plate5_rect.centery - 95))

def render_plate5_NS():
    screen.blit(plate1_NS, plate5_NS_rect)

def render_plate6():
    screen.blit(plate2, plate6_rect)
    screen.blit(products_count_font.render(
        f"{product_list['105']['stock']}",
        True, 'Black'
    ), (plate6_rect.centerx - 16, plate6_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['105']['price']}",
        True, 'Black'
    ), (plate6_rect.centerx - 25, plate6_rect.centery - 95))

def render_plate6_NS():
    screen.blit(plate2_NS, plate6_NS_rect)

def render_plate7():
    screen.blit(plate2, plate7_rect)
    screen.blit(products_count_font.render(
        f"{product_list['106']['stock']}",
        True, 'Black'
    ), (plate7_rect.centerx - 16, plate7_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['106']['price']}",
        True, 'Black'
    ), (plate7_rect.centerx - 25, plate7_rect.centery - 95))

def render_plate7_NS():
    screen.blit(plate2_NS, plate7_NS_rect)

def render_plate8():
    screen.blit(plate6, plate8_rect)
    screen.blit(products_count_font.render(
        f"{product_list['116']['stock']}",
        True, 'Black'
    ), (plate8_rect.centerx - 16, plate8_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['116']['price']}",
        True, 'Black'
    ), (plate8_rect.centerx - 25, plate8_rect.centery - 95))

def render_plate8_NS():
    screen.blit(plate6_NS, plate8_NS_rect)

def render_plate9():
    screen.blit(plate3, plate9_rect)
    screen.blit(products_count_font.render(
        f"{product_list['109']['stock']}",
        True, 'Black'
    ), (plate9_rect.centerx - 16, plate9_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['109']['price']}",
        True, 'Black'
    ), (plate9_rect.centerx - 25, plate9_rect.centery - 95))

def render_plate9_NS():
    screen.blit(plate3_NS, plate9_NS_rect)

def render_plate10():
    screen.blit(plate3, plate10_rect)
    screen.blit(products_count_font.render(
        f"{product_list['110']['stock']}",
        True, 'Black'
    ), (plate10_rect.centerx - 16, plate10_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['110']['price']}",
        True, 'Black'
    ), (plate10_rect.centerx - 25, plate10_rect.centery - 95))

def render_plate10_NS():
    screen.blit(plate3_NS, plate10_NS_rect)

def render_plate11():
    screen.blit(plate4, plate11_rect)
    screen.blit(products_count_font.render(
        f"{product_list['100']['stock']}",
        True, 'Black'
    ), (plate11_rect.centerx - 16, plate11_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['100']['price']}",
        True, 'Black'
    ), (plate11_rect.centerx - 25, plate11_rect.centery - 95))

def render_plate11_NS():
    screen.blit(plate4_NS, plate11_NS_rect)

def render_plate12():
    screen.blit(plate4, plate12_rect)
    screen.blit(products_count_font.render(
        f"{product_list['101']['stock']}",
        True, 'Black'
    ), (plate12_rect.centerx - 16, plate12_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['101']['price']}",
        True, 'Black'
    ), (plate12_rect.centerx - 25, plate12_rect.centery - 95))

def render_plate12_NS():
    screen.blit(plate4_NS, plate12_NS_rect)

def render_plate13():
    screen.blit(plate4, plate13_rect)
    screen.blit(products_count_font.render(
        f"{product_list['102']['stock']}",
        True, 'Black'
    ), (plate13_rect.centerx - 16, plate13_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['102']['price']}",
        True, 'Black'
    ), (plate13_rect.centerx - 25, plate13_rect.centery - 95))

def render_plate13_NS():
    screen.blit(plate4_NS, plate13_NS_rect)

def render_plate14():
    screen.blit(plate4, plate14_rect)
    screen.blit(products_count_font.render(
        f"{product_list['103']['stock']}",
        True, 'Black'
    ), (plate14_rect.centerx - 16, plate14_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['103']['price']}",
        True, 'Black'
    ), (plate14_rect.centerx - 25, plate14_rect.centery - 95))

def render_plate14_NS():
    screen.blit(plate4_NS, plate14_NS_rect)

def render_plate18():
    screen.blit(plate6, plate18_rect)
    screen.blit(products_count_font.render(
        f"{product_list['114']['stock']}",
        True, 'Black'
    ), (plate18_rect.centerx - 16, plate18_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['114']['price']}",
        True, 'Black'
    ), (plate18_rect.centerx - 25, plate18_rect.centery - 95))

def render_plate18_NS():
    screen.blit(plate6_NS, plate18_NS_rect)

def render_plate17():
    screen.blit(plate5, plate17_rect)
    screen.blit(products_count_font.render(
        f"{product_list['113']['stock']}",
        True, 'Black'
    ), (plate17_rect.centerx - 16, plate17_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['113']['price']}",
        True, 'Black'
    ), (plate17_rect.centerx - 25, plate17_rect.centery - 95))

def render_plate17_NS():
    screen.blit(plate5_NS, plate17_NS_rect)

def render_plate16():
    screen.blit(plate4, plate16_rect)
    screen.blit(products_count_font.render(
        f"{product_list['104']['stock']}",
        True, 'Black'
    ), (plate16_rect.centerx - 16, plate16_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['104']['price']}",
        True, 'Black'
    ), (plate16_rect.centerx - 25, plate16_rect.centery - 95))

def render_plate16_NS():
    screen.blit(plate4_NS, plate16_NS_rect)

def render_plate15():
    screen.blit(plate6, plate15_rect)
    screen.blit(products_count_font.render(
        f"{product_list['117']['stock']}",
        True, 'Black'
    ), (plate15_rect.centerx - 16, plate15_rect.centery + 75))
    screen.blit(products_price_font.render(
        f"${product_list['117']['price']}",
        True, 'Black'
    ), (plate15_rect.centerx - 25, plate15_rect.centery - 95))

def render_plate15_NS():
    screen.blit(plate6_NS, plate15_NS_rect)


def check_add_product():
    global small_food_pie1_rect, small_food_pie2_rect, small_food_rectpie_rect, small_food_fruitpie_rect, \
        small_food_blueberryfish_rect, small_food_bread_turtle_rect, small_food_bread_crocodile_rect, \
        small_food_baguette_rect, \
        small_food_roundbread_rect, \
        small_food_eggtoast_rect, \
        small_food_toast_rect, \
        small_food_pretzel_rect, \
        small_food_croissant_rect, \
        small_food_bagel_rect, \
        small_food_chocolatebread_rect, \
        small_food_cookies_rect, \
        small_food_creambread_rect, \
        small_food_cupcake_rect

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
    elif food_chocolatebread_rect.collidepoint(event.pos) and product_list['114']['stock'] > 0:
        buy_with_code(product_list, cart, '114')
        update_ticket()
    elif food_cookies_rect.collidepoint(event.pos) and product_list['115']['stock'] > 0:
        buy_with_code(product_list, cart, '115')
        update_ticket()
    elif food_creambread_rect.collidepoint(event.pos) and product_list['116']['stock'] > 0:
        buy_with_code(product_list, cart, '116')
        update_ticket()
    elif food_cupcake_rect.collidepoint(event.pos) and product_list['117']['stock'] > 0:
        buy_with_code(product_list, cart, '117')
        update_ticket()



def check_manager_add_product():
    global small_food_pie1_rect, small_food_pie2_rect, small_food_rectpie_rect, small_food_fruitpie_rect, \
        small_food_blueberryfish_rect, small_food_bread_turtle_rect, small_food_bread_crocodile_rect, \
        small_food_baguette_rect, \
        small_food_roundbread_rect, \
        small_food_eggtoast_rect, \
        small_food_toast_rect, \
        small_food_pretzel_rect, \
        small_food_croissant_rect, \
        small_food_bagel_rect, \
        small_food_chocolatebread_rect, \
        small_food_cookies_rect, \
        small_food_creambread_rect, \
        small_food_cupcake_rect

    if small_food_pie1_rect.collidepoint(event.pos) and product_list['100']['status'] == 'STORAGE':
        return add_product(product_list, '100')
    elif small_food_pie2_rect.collidepoint(event.pos) and product_list['101']['status'] == 'STORAGE':
        return add_product(product_list, '101')
    elif small_food_rectpie_rect.collidepoint(event.pos) and product_list['102']['status'] == 'STORAGE':
        return add_product(product_list, '102')
    elif small_food_fruitpie_rect.collidepoint(event.pos) and product_list['103']['status'] == 'STORAGE':
        return add_product(product_list, '103')
    elif small_food_blueberryfish_rect.collidepoint(event.pos) and product_list['104']['status'] == 'STORAGE':
        return add_product(product_list, '104')
    elif small_food_bread_turtle_rect.collidepoint(event.pos) and product_list['105']['status'] == 'STORAGE':
        return add_product(product_list, '105')
    elif small_food_bread_crocodile_rect.collidepoint(event.pos) and product_list['106']['status'] == 'STORAGE':
        return add_product(product_list, '106')
    elif small_food_baguette_rect.collidepoint(event.pos) and product_list['107']['status'] == 'STORAGE':
        return add_product(product_list, '107')
    elif small_food_roundbread_rect.collidepoint(event.pos) and product_list['108']['status'] == 'STORAGE':
        return add_product(product_list, '108')
    elif small_food_eggtoast_rect.collidepoint(event.pos) and product_list['109']['status'] == 'STORAGE':
        return add_product(product_list, '109')
    elif food_toast_rect.collidepoint(event.pos) and product_list['110']['status'] == 'STORAGE':
        return add_product(product_list, '110')
    elif small_food_pretzel_rect.collidepoint(event.pos) and product_list['111']['status'] == 'STORAGE':
        return add_product(product_list, '111')
    elif small_food_croissant_rect.collidepoint(event.pos) and product_list['112']['status'] == 'STORAGE':
        return add_product(product_list, '112')
    elif small_food_bagel_rect.collidepoint(event.pos) and product_list['113']['status'] == 'STORAGE':
        return add_product(product_list, '113')
    elif small_food_chocolatebread_rect.collidepoint(event.pos) and product_list['114']['status'] == 'STORAGE':
        return add_product(product_list, '114')
    elif small_food_cookies_rect.collidepoint(event.pos) and product_list['115']['status'] == 'STORAGE':
        return add_product(product_list, '115')
    elif small_food_creambread_rect.collidepoint(event.pos) and product_list['116']['status'] == 'STORAGE':
        return add_product(product_list, '116')
    elif small_food_cupcake_rect.collidepoint(event.pos) and product_list['117']['status'] == 'STORAGE':
        return add_product(product_list, '117')

def check_manager_remove_product():
    global small_food_pie1_rect, small_food_pie2_rect, small_food_rectpie_rect, small_food_fruitpie_rect, \
        small_food_blueberryfish_rect, small_food_bread_turtle_rect, small_food_bread_crocodile_rect, \
        small_food_baguette_rect, \
        small_food_roundbread_rect, \
        small_food_eggtoast_rect, \
        small_food_toast_rect, \
        small_food_pretzel_rect, \
        small_food_croissant_rect, \
        small_food_bagel_rect, \
        small_food_chocolatebread_rect, \
        small_food_cookies_rect, \
        small_food_creambread_rect, \
        small_food_cupcake_rect

    if small_food_pie1_rect.collidepoint(event.pos) and product_list['100']['status'] == 'GLASS':
        remove_product(product_list, '100')
    elif small_food_pie2_rect.collidepoint(event.pos) and product_list['101']['status'] == 'GLASS':
        remove_product(product_list, '101')
    elif small_food_rectpie_rect.collidepoint(event.pos) and product_list['102']['status'] == 'GLASS':
        remove_product(product_list, '102')
    elif small_food_fruitpie_rect.collidepoint(event.pos) and product_list['103']['status'] == 'GLASS':
        remove_product(product_list, '103')
    elif small_food_blueberryfish_rect.collidepoint(event.pos) and product_list['104']['status'] == 'GLASS':
        remove_product(product_list, '104')
    elif small_food_bread_turtle_rect.collidepoint(event.pos) and product_list['105']['status'] == 'GLASS':
        remove_product(product_list, '105')
    elif small_food_bread_crocodile_rect.collidepoint(event.pos) and product_list['106']['status'] == 'GLASS':
        remove_product(product_list, '106')
    elif small_food_baguette_rect.collidepoint(event.pos) and product_list['107']['status'] == 'GLASS':
        remove_product(product_list, '107')
    elif small_food_roundbread_rect.collidepoint(event.pos) and product_list['108']['status'] == 'GLASS':
        remove_product(product_list, '108')
    elif small_food_eggtoast_rect.collidepoint(event.pos) and product_list['109']['status'] == 'GLASS':
        remove_product(product_list, '109')
    elif small_food_toast_rect.collidepoint(event.pos) and product_list['110']['status'] == 'GLASS':
        remove_product(product_list, '110')
    elif small_food_pretzel_rect.collidepoint(event.pos) and product_list['111']['status'] == 'GLASS':
        remove_product(product_list, '111')
    elif small_food_croissant_rect.collidepoint(event.pos) and product_list['112']['status'] == 'GLASS':
        remove_product(product_list, '112')
    elif small_food_bagel_rect.collidepoint(event.pos) and product_list['113']['status'] == 'GLASS':
        remove_product(product_list, '113')
    elif small_food_chocolatebread_rect.collidepoint(event.pos) and product_list['114']['status'] == 'GLASS':
        remove_product(product_list, '114')
    elif small_food_cookies_rect.collidepoint(event.pos) and product_list['115']['status'] == 'GLASS':
        remove_product(product_list, '115')
    elif small_food_creambread_rect.collidepoint(event.pos) and product_list['116']['status'] == 'GLASS':
        remove_product(product_list, '116')
    elif small_food_cupcake_rect.collidepoint(event.pos) and product_list['117']['status'] == 'GLASS':
        remove_product(product_list, '117')

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

def check_update_stock_button_clicked():
    global small_update_stock_food_pie1_rect, \
        small_update_stock_food_pie2_rect, \
        small_update_stock_food_rectpie_rect, \
        small_update_stock_food_fruitpie_rect, \
        small_update_stock_food_blueberryfish_rect, \
        small_update_stock_food_bread_turtle_rect, \
        small_update_stock_food_bread_crocodile_rect, \
        small_update_stock_food_baguette_rect, \
        small_update_stock_food_roundbread_rect, \
        small_update_stock_food_eggtoast_rect, \
        small_update_stock_food_toast_rect, \
        small_update_stock_food_pretzel_rect, \
        small_update_stock_food_croissant_rect, \
        small_update_stock_food_bagel_rect, \
        small_update_stock_food_chocolatebread_rect, \
        small_update_stock_food_cookies_rect, \
        small_update_stock_food_creambread_rect, \
        small_update_stock_food_cupcake_rect

    if small_update_stock_food_pie1_rect.collidepoint(event.pos) and product_list['100']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '100', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_pie2_rect.collidepoint(event.pos) and product_list['101']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '101', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_rectpie_rect.collidepoint(event.pos) and product_list['102']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '102', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_fruitpie_rect.collidepoint(event.pos) and product_list['103']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '103', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_blueberryfish_rect.collidepoint(event.pos) and product_list['104']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '104', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_bread_turtle_rect.collidepoint(event.pos) and product_list['105']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '105', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_bread_crocodile_rect.collidepoint(event.pos) and product_list['106']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '106', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_baguette_rect.collidepoint(event.pos) and product_list['107']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '107', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_roundbread_rect.collidepoint(event.pos) and product_list['108']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '108', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_eggtoast_rect.collidepoint(event.pos) and product_list['109']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '109', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_toast_rect.collidepoint(event.pos) and product_list['110']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '110', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_pretzel_rect.collidepoint(event.pos) and product_list['111']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '111', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_croissant_rect.collidepoint(event.pos) and product_list['112']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '112', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_bagel_rect.collidepoint(event.pos) and product_list['113']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '113', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_chocolatebread_rect.collidepoint(event.pos) and product_list['114']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '114', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_cookies_rect.collidepoint(event.pos) and product_list['115']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '115', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_creambread_rect.collidepoint(event.pos) and product_list['116']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '116', MIN_STOCK_TO_UPDATE)
    elif small_update_stock_food_cupcake_rect.collidepoint(event.pos) and product_list['117']['stock'] < MIN_STOCK_TO_UPDATE:
        update_product_stock(product_list, '117', MIN_STOCK_TO_UPDATE)

def check_increment_porcentage_button_clicked():
    if increment_porcentage_button_rect.collidepoint(event.pos):
        increment_price_by_percentage(product_list, 0.1)

def check_decrement_porcentage_button_clicked():
    if decrement_porcentage_button_rect.collidepoint(event.pos):
        decrement_price_by_percentage(product_list, 0.1)

def draw_button(x, y, width, height, text, button_color, text_color):
    pygame.draw.rect(screen, button_color, (x, y, width, height))

    text_surface = button_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))

    screen.blit(text_surface, text_rect)
    return text_rect

def render_user_game_screen():
    screen.fill((255, 255, 255))
    screen.blit(glass, glass_rect)
    screen.blit(welcome, welcome_rect)
    screen.blit(plates_type, plates_type_rect)
    # Ticket
    screen.blit(ticket, ticket_rect)
    for name, product_component in products_text.items():
        component = ticket_products_font.render(
            f"{name}: {product_component['quantity']} x ${product_component['price']} = ${product_component['quantity'] * product_component['price']}",
            True, (82,74,68))

        screen.blit(component, (MARGIN, product_component['position_y']))
    # Display total price
    total_price_text = test_font.render(f"TOTAL ${total_price}", True, 'Black')
    screen.blit(total_price_text, (124, 885))
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
    render_plate15()
    render_plate16()
    render_plate17()
    render_plate18()

    tagx = 25
    tagy = -120

    if product_list['100']['stock'] > 0:
        screen.blit(food_pie1, food_pie1_rect)
        if product_list['100']['discount']:
            screen.blit(discount_badge, (food_pie1_rect.centerx + tagx, food_pie1_rect.centery + tagy))
    else:
        screen.blit(food_pie1_NS, food_pie1_NS_rect)
    if product_list['101']['stock'] > 0:
        screen.blit(food_pie2, food_pie2_rect)
        if product_list['101']['discount']:
            screen.blit(discount_badge, (food_pie2_rect.centerx + tagx, food_pie2_rect.centery + tagy))
    else:
        screen.blit(food_pie2_NS, food_pie2_NS_rect)
    if product_list['102']['stock'] > 0:
        screen.blit(food_rectpie, food_rectpie_rect)
        if product_list['102']['discount']:
            screen.blit(discount_badge, (food_rectpie_rect.centerx + tagx, food_rectpie_rect.centery + tagy))
    else:
        screen.blit(food_rectpie_NS, food_rectpie_NS_rect)
    if product_list['103']['stock'] > 0:
        screen.blit(food_fruitpie, food_fruitpie_rect)
        if product_list['103']['discount']:
            screen.blit(discount_badge, (food_fruitpie_rect.centerx + tagx, food_fruitpie_rect.centery + tagy))
    else:
        screen.blit(food_fruitpie_NS, food_fruitpie_NS_rect)
    if product_list['104']['stock'] > 0:
        screen.blit(food_blueberryfish, food_blueberryfish_rect)
        if product_list['104']['discount']:
            screen.blit(discount_badge, (food_blueberryfish_rect.centerx + tagx, food_blueberryfish_rect.centery + tagy))
    else:
        screen.blit(food_blueberryfish_NS, food_blueberryfish_NS_rect)
    if product_list['105']['stock'] > 0:
        screen.blit(food_bread_turtle, food_bread_turtle_rect)
        if product_list['105']['discount']:
            screen.blit(discount_badge, (food_bread_turtle_rect.centerx + tagx, food_bread_turtle_rect.centery + tagy))
    else:
        screen.blit(food_bread_turtle_NS, food_bread_turtle_NS_rect)
    if product_list['106']['stock'] > 0:
        screen.blit(food_bread_crocodile, food_bread_crocodile_rect)
        if product_list['106']['discount']:
            screen.blit(discount_badge,
                        (food_bread_crocodile_rect.centerx + tagx, food_bread_crocodile_rect.centery + tagy))
    else:
        screen.blit(food_bread_crocodile_NS, food_bread_crocodile_NS_rect)
    if product_list['107']['stock'] > 0:
        screen.blit(food_baguette, food_baguette_rect)
        if product_list['107']['discount']:
            screen.blit(discount_badge, (food_baguette_rect.centerx + tagx, food_baguette_rect.centery + tagy))
    else:
        screen.blit(food_baguette_NS, food_baguette_NS_rect)
    if product_list['108']['stock'] > 0:
        screen.blit(food_roundbread, food_roundbread_rect)
        if product_list['108']['discount']:
            screen.blit(discount_badge, (food_roundbread_rect.centerx + tagx, food_roundbread_rect.centery + tagy))
    else:
        screen.blit(food_roundbread_NS, food_roundbread_NS_rect)
    if product_list['109']['stock'] > 0:
        screen.blit(food_eggtoast, food_eggtoast_rect)
        if product_list['109']['discount']:
            screen.blit(discount_badge, (food_eggtoast_rect.centerx + tagx, food_eggtoast_rect.centery + tagy))
    else:
        screen.blit(food_eggtoast_NS, food_eggtoast_NS_rect)
    if product_list['110']['stock'] > 0:
        screen.blit(food_toast, food_toast_rect)
        if product_list['110']['discount']:
            screen.blit(discount_badge, (food_toast_rect.centerx + tagx, food_toast_rect.centery + tagy))
    else:
        screen.blit(food_toast_NS, food_toast_NS_rect)
    if product_list['111']['stock'] > 0:
        screen.blit(food_pretzel, food_pretzel_rect)
        if product_list['111']['discount']:
            screen.blit(discount_badge, (food_pretzel_rect.centerx + tagx, food_pretzel_rect.centery + tagy))
    else:
        screen.blit(food_pretzel_NS, food_pretzel_NS_rect)
    if product_list['112']['stock'] > 0:
        screen.blit(food_croissant, food_croissant_rect)
        if product_list['112']['discount']:
            screen.blit(discount_badge, (food_croissant_rect.centerx + tagx, food_croissant_rect.centery + tagy))
    else:
        screen.blit(food_croissant_NS, food_croissant_NS_rect)
    if product_list['113']['stock'] > 0:
        screen.blit(food_bagel, food_bagel_rect)
        if product_list['113']['discount']:
            screen.blit(discount_badge, (food_bagel_rect.centerx + tagx, food_bagel_rect.centery + tagy))
    else:
        screen.blit(food_bagel_NS, food_bagel_NS_rect)

    if product_list['114']['stock'] > 0:
        screen.blit(food_chocolatebread, food_chocolatebread_rect)
    else:
        screen.blit(food_chocolatebread_NS, food_chocolatebread_NS_rect)

    if product_list['115']['stock'] > 0:
        screen.blit(food_cookies, food_cookies_rect)
    else:
        screen.blit(food_cookies_NS, food_cookies_NS_rect)

    if product_list['116']['stock'] > 0:
        screen.blit(food_creambread, food_creambread_rect)
    else:
        screen.blit(food_creambread_NS, food_creambread_NS_rect)

    if product_list['117']['stock'] > 0:
        screen.blit(food_cupcake, food_cupcake_rect)
    else:
        screen.blit(food_cupcake_NS, food_cupcake_NS_rect)

def render_manager_game_screen():
    screen.fill((255, 255, 255))
    screen.blit(glass, glass_rect)
    screen.blit(welcome, welcome_rect)
    screen.blit(plates_type, plates_type_rect)
    # Ticket
    screen.blit(ticket, ticket_rect)

    render_add_product_section()

    render_remove_product_section()

    render_update_price()

    render_update_stock()

    render_old_products()

    if product_list['100']['status'] == 'GLASS':
        render_plate11()
        if product_list['100']['stock'] > 0:
            screen.blit(food_pie1, food_pie1_rect)
        else:
            screen.blit(food_pie1_NS, food_pie1_NS_rect)
    else:
        render_plate11_NS()

    if product_list['101']['status'] == 'GLASS':
        render_plate12()
        if product_list['101']['stock'] > 0:
            screen.blit(food_pie2, food_pie2_rect)
        else:
            screen.blit(food_pie2_NS, food_pie2_NS_rect)
    else:
        render_plate12_NS()

    if product_list['102']['status'] == 'GLASS':
        render_plate13()
        if product_list['102']['stock'] > 0:
            screen.blit(food_rectpie, food_rectpie_rect)
        else:
            screen.blit(food_rectpie_NS, food_rectpie_NS_rect)
    else:
        render_plate13_NS()

    if product_list['103']['status'] == 'GLASS':
        render_plate14()
        if product_list['103']['stock'] > 0:
            screen.blit(food_fruitpie, food_fruitpie_rect)
        else:
            screen.blit(food_fruitpie_NS, food_fruitpie_NS_rect)
    else:
        render_plate14_NS()

    if product_list['104']['status'] == 'GLASS':
        render_plate16()
        if product_list['104']['stock'] > 0:
            screen.blit(food_blueberryfish, food_blueberryfish_rect)
        else:
            screen.blit(food_blueberryfish_NS, food_blueberryfish_NS_rect)
    else:
        render_plate16_NS()

    if product_list['105']['status'] == 'GLASS':
        render_plate6()
        if product_list['105']['stock'] > 0:
            screen.blit(food_bread_turtle, food_bread_turtle_rect)
        else:
            screen.blit(food_bread_turtle_NS, food_bread_turtle_NS_rect)
    else:
        render_plate6_NS()

    if product_list['106']['status'] == 'GLASS':
        render_plate7()
        if product_list['106']['stock'] > 0:
            screen.blit(food_bread_crocodile, food_bread_crocodile_rect)
        else:
            screen.blit(food_bread_crocodile_NS, food_bread_crocodile_NS_rect)
    else:
        render_plate7_NS()

    if product_list['107']['status'] == 'GLASS':
        render_plate2()
        if product_list['107']['stock'] > 0:
            screen.blit(food_baguette, food_baguette_rect)
        else:
            screen.blit(food_baguette_NS, food_baguette_NS_rect)
    else:
        render_plate2_NS()

    if product_list['108']['status'] == 'GLASS':
        render_plate3()
        if product_list['108']['stock'] > 0:
            screen.blit(food_roundbread, food_roundbread_rect)
        else:
            screen.blit(food_roundbread_NS, food_roundbread_NS_rect)
    else:
        render_plate3_NS()

    if product_list['109']['status'] == 'GLASS':
        render_plate9()
        if product_list['109']['stock'] > 0:
            screen.blit(food_eggtoast, food_eggtoast_rect)
        else:
            screen.blit(food_eggtoast_NS, food_eggtoast_NS_rect)
    else:
        render_plate9_NS()

    if product_list['110']['status'] == 'GLASS':
        render_plate10()
        if product_list['110']['stock'] > 0:
            screen.blit(food_toast, food_toast_rect)
        else:
            screen.blit(food_toast_NS, food_toast_NS_rect)
    else:
        render_plate10_NS()

    if product_list['111']['status'] == 'GLASS':
        render_plate4()
        if product_list['111']['stock'] > 0:
            screen.blit(food_pretzel, food_pretzel_rect)
        else:
            screen.blit(food_pretzel_NS, food_pretzel_NS_rect)
    else:
        render_plate4_NS()

    if product_list['112']['status'] == 'GLASS':
        render_plate5()
        if product_list['112']['stock'] > 0:
            screen.blit(food_croissant, food_croissant_rect)
        else:
            screen.blit(food_croissant_NS, food_croissant_NS_rect)
    else:
        render_plate5_NS()

    if product_list['113']['status'] == 'GLASS':
        render_plate17()
        if product_list['113']['stock'] > 0:
            screen.blit(food_bagel, food_bagel_rect)
        else:
            screen.blit(food_bagel_NS, food_bagel_NS_rect)
    else:
        render_plate17_NS()

    if product_list['114']['status'] == 'GLASS':
        render_plate18()
        if product_list['114']['stock'] > 0:
            screen.blit(food_chocolatebread, food_chocolatebread_rect)
        else:
            screen.blit(food_chocolatebread_NS, food_chocolatebread_NS_rect)
    else:
        render_plate18_NS()

    if product_list['115']['status'] == 'GLASS':
        render_plate1()
        if product_list['115']['stock'] > 0:
            screen.blit(food_cookies, food_cookies_rect)
        else:
            screen.blit(food_cookies_NS, food_cookies_NS_rect)
    else:
        render_plate1_NS()

    if product_list['116']['status'] == 'GLASS':
        render_plate8()
        if product_list['116']['stock'] > 0:
            screen.blit(food_creambread, food_creambread_rect)
        else:
            screen.blit(food_creambread_NS, food_creambread_NS_rect)
    else:
        render_plate8_NS()

    if product_list['117']['status'] == 'GLASS':
        render_plate15()
        if product_list['117']['stock'] > 0:
            screen.blit(food_cupcake, food_cupcake_rect)
        else:
            screen.blit(food_cupcake_NS, food_cupcake_NS_rect)
    else:
        render_plate15_NS()


def render_old_products():
    screen.blit(manager_actions_titles_font.render(
        f"OLD PRODUCTS",
        True, 'Black'
    ), (70, 950))


def render_update_stock():
    global small_update_stock_food_pie1_rect, \
        small_update_stock_food_pie2_rect, \
        small_update_stock_food_rectpie_rect, \
        small_update_stock_food_fruitpie_rect, \
        small_update_stock_food_blueberryfish_rect, \
        small_update_stock_food_bread_turtle_rect, \
        small_update_stock_food_bread_crocodile_rect, \
        small_update_stock_food_baguette_rect, \
        small_update_stock_food_roundbread_rect, \
        small_update_stock_food_eggtoast_rect, \
        small_update_stock_food_toast_rect, \
        small_update_stock_food_pretzel_rect, \
        small_update_stock_food_croissant_rect, \
        small_update_stock_food_bagel_rect, \
        small_update_stock_food_chocolatebread_rect, \
        small_update_stock_food_cookies_rect, \
        small_update_stock_food_creambread_rect, \
        small_update_stock_food_cupcake_rect

    screen.blit(manager_actions_titles_font.render(
        f"UPDATE STOCK",
        True, 'Black'
    ), (70, 850))

    products_without_min_stock = {key: value for key, value in product_list.items() if value['stock'] < MIN_STOCK_TO_UPDATE}
    products_x = 100
    products_y = 900
    products_line_height = 60
    products_line_width = 100
    products_inline_count = 1

    for product_code, product in products_without_min_stock.items():
        if product_code == '100':
            small_update_stock_food_pie1_rect = small_update_stock_food_pie1.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_pie1, small_update_stock_food_pie1_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '101':
            small_update_stock_food_pie2_rect = small_update_stock_food_pie2.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_pie2, small_update_stock_food_pie2_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '102':
            small_update_stock_food_rectpie_rect = small_update_stock_food_rectpie.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_rectpie, small_update_stock_food_rectpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '103':
            small_update_stock_food_fruitpie_rect = small_update_stock_food_fruitpie.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_fruitpie, small_update_stock_food_fruitpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '104':
            small_update_stock_food_blueberryfish_rect = small_update_stock_food_blueberryfish.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_blueberryfish, small_update_stock_food_blueberryfish_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '105':
            small_update_stock_food_bread_turtle_rect = small_update_stock_food_bread_turtle.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_bread_turtle, small_update_stock_food_bread_turtle_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '106':
            small_update_stock_food_bread_crocodile_rect = small_update_stock_food_bread_crocodile.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_bread_crocodile, small_update_stock_food_bread_crocodile_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '107':
            small_update_stock_food_baguette_rect = small_update_stock_food_baguette.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_baguette, small_update_stock_food_baguette_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '108':
            small_update_stock_food_roundbread_rect = small_update_stock_food_roundbread.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_roundbread, small_update_stock_food_roundbread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '109':
            small_update_stock_food_eggtoast_rect = small_update_stock_food_eggtoast.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_eggtoast, small_update_stock_food_eggtoast_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '110':
            small_update_stock_food_toast_rect = small_update_stock_food_toast.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_toast, small_update_stock_food_toast_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '111':
            small_update_stock_food_pretzel_rect = small_update_stock_food_pretzel.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_pretzel, small_update_stock_food_pretzel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '112':
            small_update_stock_food_croissant_rect = small_update_stock_food_croissant.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_croissant, small_update_stock_food_croissant_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '113':
            small_update_stock_food_bagel_rect = small_update_stock_food_bagel.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_bagel, small_update_stock_food_bagel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '114':
            small_update_stock_food_chocolatebread_rect = small_update_stock_food_chocolatebread.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_chocolatebread, small_update_stock_food_chocolatebread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '115':
            small_update_stock_food_cookies_rect = small_update_stock_food_cookies.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_cookies, small_update_stock_food_cookies_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '116':
            small_update_stock_food_creambread_rect = small_update_stock_food_creambread.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_creambread, small_update_stock_food_creambread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '117':
            small_update_stock_food_cupcake_rect = small_update_stock_food_cupcake.get_rect(center=(products_x, products_y))
            screen.blit(small_update_stock_food_cupcake, small_update_stock_food_cupcake_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1


def render_update_price():
    global increment_porcentage_button_rect, decrement_porcentage_button_rect
    screen.blit(manager_actions_titles_font.render(
        f"PRICE UPDATE",
        True, 'Black'
    ), (70, 750))
    increment_porcentage_button_rect = draw_button(330, 745, 100, 50, "+10%", 'Grey', 'Black')
    decrement_porcentage_button_rect = draw_button(450, 745, 100, 50, "-10%", 'Grey', 'Black')


def render_remove_product_section():
    global small_food_pie1_rect, small_food_pie2_rect, small_food_rectpie_rect, small_food_fruitpie_rect,\
        small_food_blueberryfish_rect, small_food_bread_turtle_rect, small_food_bread_crocodile_rect, \
        small_food_baguette_rect, \
        small_food_roundbread_rect, \
        small_food_eggtoast_rect, \
        small_food_toast_rect, \
        small_food_pretzel_rect, \
        small_food_croissant_rect, \
        small_food_bagel_rect, \
        small_food_chocolatebread_rect, \
        small_food_cookies_rect, \
        small_food_creambread_rect, \
        small_food_cupcake_rect

    screen.blit(manager_actions_titles_font.render(
        f"DELETE PRODUCT",
        True, 'Black'
    ), (70, 550))
    products_in_glass = {key: value for key, value in product_list.items() if value['status'] == 'GLASS'}
    products_x = 100
    products_y = 650
    products_line_height = 60
    products_line_width = 100
    products_inline_count = 1
    for product_code, product in products_in_glass.items():
        if product_code == '100':
            small_food_pie1_rect = small_food_pie1.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pie1,small_food_pie1_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '101':
            small_food_pie2_rect = small_food_pie2.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pie2, small_food_pie2_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '102':
            small_food_rectpie_rect = small_food_rectpie.get_rect(center=(products_x, products_y))
            screen.blit(small_food_rectpie, small_food_rectpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '103':
            small_food_fruitpie_rect = small_food_fruitpie.get_rect(center=(products_x, products_y))
            screen.blit(small_food_fruitpie, small_food_fruitpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '104':
            small_food_blueberryfish_rect = small_food_blueberryfish.get_rect(center=(products_x, products_y))
            screen.blit(small_food_blueberryfish, small_food_blueberryfish_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '105':
            small_food_bread_turtle_rect = small_food_bread_turtle.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bread_turtle, small_food_bread_turtle_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '106':
            small_food_bread_crocodile_rect = small_food_bread_crocodile.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bread_crocodile, small_food_bread_crocodile_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '107':
            small_food_baguette_rect = small_food_baguette.get_rect(center=(products_x, products_y))
            screen.blit(small_food_baguette, small_food_baguette_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '108':
            small_food_roundbread_rect = small_food_roundbread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_roundbread, small_food_roundbread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '109':
            small_food_eggtoast_rect = small_food_eggtoast.get_rect(center=(products_x, products_y))
            screen.blit(small_food_eggtoast, small_food_roundbread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '110':
            small_food_toast_rect = small_food_toast.get_rect(center=(products_x, products_y))
            screen.blit(small_food_toast, small_food_toast_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '111':
            small_food_pretzel_rect = small_food_pretzel.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pretzel, small_food_pretzel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '112':
            small_food_croissant_rect = small_food_croissant.get_rect(center=(products_x, products_y))
            screen.blit(small_food_croissant, small_food_croissant_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '113':
            small_food_bagel_rect = small_food_bagel.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bagel, small_food_bagel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '114':
            small_food_chocolatebread_rect = small_food_chocolatebread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_chocolatebread, small_food_chocolatebread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '115':
            small_food_cookies_rect = small_food_cookies.get_rect(center=(products_x, products_y))
            screen.blit(small_food_cookies, small_food_cookies_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '116':
            small_food_creambread_rect = small_food_creambread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_creambread, small_food_creambread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '117':
            small_food_cupcake_rect = small_food_cupcake.get_rect(center=(products_x, products_y))
            screen.blit(small_food_cupcake, small_food_cupcake_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

def render_add_product_section():
    global small_food_pie1_rect, small_food_pie2_rect, small_food_rectpie_rect, small_food_fruitpie_rect, \
        small_food_blueberryfish_rect, small_food_bread_turtle_rect, small_food_bread_crocodile_rect, \
        small_food_baguette_rect, \
        small_food_roundbread_rect, \
        small_food_eggtoast_rect, \
        small_food_toast_rect, \
        small_food_pretzel_rect, \
        small_food_croissant_rect, \
        small_food_bagel_rect, \
        small_food_chocolatebread_rect, \
        small_food_cookies_rect, \
        small_food_creambread_rect, \
        small_food_cupcake_rect

    screen.blit(manager_actions_titles_font.render(
        f"ADD PRODUCT",
        True, 'Black'
    ), (70, 350))
    products_in_storage = {key: value for key, value in product_list.items()  if value['status'] == 'STORAGE'}
    products_x = 100
    products_y = 430
    products_line_height = 60
    products_line_width = 100
    products_inline_count = 1
    for product_code, product in products_in_storage.items():
        if product_code == '100':
            small_food_pie1_rect = small_food_pie1.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pie1, small_food_pie1_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '101':
            small_food_pie2_rect = small_food_pie2.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pie2, small_food_pie2_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '102':
            small_food_rectpie_rect = small_food_rectpie.get_rect(center=(products_x, products_y))
            screen.blit(small_food_rectpie, small_food_rectpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '103':
            small_food_fruitpie_rect = small_food_fruitpie.get_rect(center=(products_x, products_y))
            screen.blit(small_food_fruitpie, small_food_fruitpie_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '104':
            small_food_blueberryfish_rect = small_food_blueberryfish.get_rect(center=(products_x, products_y))
            screen.blit(small_food_blueberryfish, small_food_blueberryfish_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '105':
            small_food_bread_turtle_rect = small_food_bread_turtle.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bread_turtle, small_food_bread_turtle_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '106':
            small_food_bread_crocodile_rect = small_food_bread_crocodile.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bread_crocodile, small_food_bread_crocodile_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '107':
            small_food_baguette_rect = small_food_baguette.get_rect(center=(products_x, products_y))
            screen.blit(small_food_baguette, small_food_baguette_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '108':
            small_food_roundbread_rect = small_food_roundbread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_roundbread, small_food_roundbread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '109':
            small_food_eggtoast_rect = small_food_eggtoast.get_rect(center=(products_x, products_y))
            screen.blit(small_food_eggtoast, small_food_roundbread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '110':
            small_food_toast_rect = small_food_toast.get_rect(center=(products_x, products_y))
            screen.blit(small_food_toast, small_food_toast_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '111':
            small_food_pretzel_rect = small_food_pretzel.get_rect(center=(products_x, products_y))
            screen.blit(small_food_pretzel, small_food_pretzel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '112':
            small_food_croissant_rect = small_food_croissant.get_rect(center=(products_x, products_y))
            screen.blit(small_food_croissant, small_food_croissant_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '113':
            small_food_bagel_rect = small_food_bagel.get_rect(center=(products_x, products_y))
            screen.blit(small_food_bagel, small_food_bagel_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '114':
            small_food_chocolatebread_rect = small_food_chocolatebread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_chocolatebread, small_food_chocolatebread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '115':
            small_food_cookies_rect = small_food_cookies.get_rect(center=(products_x, products_y))
            screen.blit(small_food_cookies, small_food_cookies_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '116':
            small_food_creambread_rect = small_food_creambread.get_rect(center=(products_x, products_y))
            screen.blit(small_food_creambread, small_food_creambread_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1

        if product_code == '117':
            small_food_cupcake_rect = small_food_cupcake.get_rect(center=(products_x, products_y))
            screen.blit(small_food_cupcake, small_food_cupcake_rect)
            if products_inline_count > 3:
                products_y += products_line_height
                products_inline_count = 0
                products_x = 100
            else:
                products_x += products_line_width
                products_inline_count += 1


def listen_to_key_binding():
    global event, running, game_selected
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        elif game_selected == '':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_user_button.collidepoint(event.pos):
                    game_selected = 'USER'
                elif login_manager_button.collidepoint(event.pos):
                    game_selected = 'MANAGER'
        elif game_selected == 'USER':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click del Mouse
                    check_add_product()
                elif event.button == 3:  # Right Click del Mouse
                    check_remove_product()
        elif game_selected == 'MANAGER':
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left Click del Mouse
                    check_increment_porcentage_button_clicked()
                    check_decrement_porcentage_button_clicked()
                    check_update_stock_button_clicked()
                    product_added = check_manager_add_product()
                    if not product_added:
                        check_manager_remove_product()

# Setup
pygame.init()
PRODUCT_HEIGHT = 28
MARGIN = 130
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
MIN_STOCK_TO_UPDATE = 100
screen = pygame.display.set_mode((SCREEN_WIDTH,
                                  SCREEN_HEIGHT))  # Create screen. This code ends, so to keep it running we use the while True (is never False).
pygame.display.set_caption('Bakery')
clock = pygame.time.Clock()  # clock object to handle frame rate
test_font = pygame.font.Font('font/Alkhemikal.ttf', 40)
button_font = pygame.font.Font('font/Alkhemikal.ttf', 40)
ticket_products_font = pygame.font.Font('font/Alkhemikal.ttf', 26)
products_count_font = pygame.font.Font('font/Alkhemikal.ttf', 28)
products_price_font = pygame.font.Font('font/Alkhemikal.ttf', 25)
manager_actions_titles_font = pygame.font.Font('font/Alkhemikal.ttf', 40)
game_active = True
running = True

# Bacgrkound & Store
welcome = pygame.image.load('graphics/welcome.png').convert_alpha()
welcome_rect = welcome.get_rect(center=(960, 120))

glass = pygame.image.load('graphics/glass.png').convert_alpha()
glass = pygame.transform.scale(glass, (1920, 900))
glass_rect = glass.get_rect(topleft=(0, 220))

ticket = pygame.image.load('graphics/ticket.png').convert_alpha()
ticket = pygame.transform.scale(ticket, (550, 650))
ticket_rect = ticket.get_rect(topleft=(100, 320))

current_y = 430

plates_type = pygame.image.load('graphics/plates-catalogue.png').convert_alpha()
plates_type = pygame.transform.scale(plates_type, (450, 300))
plates_type_rect = plates_type.get_rect(topleft=(1500, 30))

plate1 = pygame.image.load('graphics/plates/plate1.png').convert_alpha()
plate1 = pygame.transform.scale(plate1, (170, 210))
plate2 = pygame.image.load('graphics/plates/plate2.png').convert_alpha()
plate2 = pygame.transform.scale(plate2, (170, 210))
plate3 = pygame.image.load('graphics/plates/plate3.png').convert_alpha()
plate3 = pygame.transform.scale(plate3, (170, 210))
plate4 = pygame.image.load('graphics/plates/plate4.png').convert_alpha()
plate4 = pygame.transform.scale(plate4, (170, 210))
plate5 = pygame.image.load('graphics/plates/plate5.png').convert_alpha()
plate5 = pygame.transform.scale(plate5, (170, 210))
plate6 = pygame.image.load('graphics/plates/plate6.png').convert_alpha()
plate6 = pygame.transform.scale(plate6, (170, 210))

# Plain
plate1_rect = plate1.get_rect(center=(1390, 900))
plate2_rect = plate1.get_rect(center=(790, 390))
plate3_rect = plate1.get_rect(center=(990, 390))
plate4_rect = plate1.get_rect(center=(1190, 390))

# Zoo Bread
plate5_rect = plate1.get_rect(center=(1390, 390))
plate6_rect = plate1.get_rect(center=(1590, 390))

# Toast
plate7_rect = plate1.get_rect(center=(1780, 390))
plate8_rect = plate1.get_rect(center=(1590, 900))

# Fruit Pie
plate9_rect = plate1.get_rect(center=(790, 640))
plate10_rect = plate1.get_rect(center=(990, 640))
plate11_rect = plate1.get_rect(center=(1190, 640))
plate12_rect = plate1.get_rect(center=(1390, 640))
plate13_rect = plate1.get_rect(center=(1590, 640))

# Sandwich
plate14_rect = plate1.get_rect(center=(1780, 640))

# Chocolates
plate15_rect = plate1.get_rect(center=(1790, 900))
plate16_rect = plate1.get_rect(center=(790, 890))
plate17_rect = plate1.get_rect(center=(990, 890))
plate18_rect = plate1.get_rect(center=(1190, 890))

# Plates NS

plate1_NS = pygame.image.load('graphics/plates/plate1-NS.png').convert_alpha()
plate1_NS = pygame.transform.scale(plate1_NS, (170, 210))
plate2_NS = pygame.image.load('graphics/plates/plate2-NS.png').convert_alpha()
plate2_NS = pygame.transform.scale(plate2_NS, (170, 210))
plate3_NS = pygame.image.load('graphics/plates/plate3-NS.png').convert_alpha()
plate3_NS = pygame.transform.scale(plate3_NS, (170, 210))
plate4_NS = pygame.image.load('graphics/plates/plate4-NS.png').convert_alpha()
plate4_NS = pygame.transform.scale(plate4_NS, (170, 210))
plate5_NS = pygame.image.load('graphics/plates/plate5-NS.png').convert_alpha()
plate5_NS = pygame.transform.scale(plate5_NS, (170, 210))
plate6_NS = pygame.image.load('graphics/plates/plate6-NS.png').convert_alpha()
plate6_NS = pygame.transform.scale(plate6_NS, (170, 210))

# Plain
plate1_NS_rect = plate1_NS.get_rect(center=(590, 390))
plate2_NS_rect = plate1_NS.get_rect(center=(790, 390))

# Zoo Bread
plate3_NS_rect = plate2_NS.get_rect(center=(990, 390))
plate4_NS_rect = plate2_NS.get_rect(center=(1190, 390))

# Toast
plate5_NS_rect = plate3_NS.get_rect(center=(1390, 390))
plate6_NS_rect = plate3_NS.get_rect(center=(1590, 390))

# Fruit Pie
plate7_NS_rect = plate4_NS.get_rect(center=(1780, 390))
plate8_NS_rect = plate4_NS.get_rect(center=(590, 640))
plate9_NS_rect = plate4_NS.get_rect(center=(790, 640))
plate10_NS_rect = plate4_NS.get_rect(center=(990, 640))
plate11_NS_rect = plate4_NS.get_rect(center=(1190, 640))

# Sandwich
plate12_NS_rect = plate5_NS.get_rect(center=(1390, 640))

# Bread
plate13_NS_rect = plate6_NS.get_rect(center=(1590, 640))
plate14_NS_rect = plate6_NS.get_rect(center=(1780, 640))

# Chocolates
plate15_NS_rect = plate4_NS.get_rect(center=(590, 890))
plate16_NS_rect = plate4_NS.get_rect(center=(790, 890))
plate17_NS_rect = plate4_NS.get_rect(center=(990, 890))
plate18_NS_rect = plate4_NS.get_rect(center=(1190, 890))

# FOOD -----------------------------------------------------------------------------------------------------------------
# Bread
food_baguette = pygame.image.load('graphics/food-baguette.png')
food_baguette = pygame.transform.scale(food_baguette, (170, 140))
food_baguette_rect = food_baguette.get_rect(center=(790, 400))

food_baguette_NS = pygame.image.load('graphics/food-baguette-NS.png')
food_baguette_NS = pygame.transform.scale(food_baguette_NS, (170, 140))
food_baguette_NS_rect = food_baguette_NS.get_rect(center=(790, 400))

food_roundbread = pygame.image.load('graphics/food-roundbread.png')
food_roundbread = pygame.transform.scale(food_roundbread, (170, 140))
food_roundbread_rect = food_roundbread.get_rect(center=(990, 400))

food_roundbread_NS = pygame.image.load('graphics/food-roundbread-NS.png')
food_roundbread_NS = pygame.transform.scale(food_roundbread_NS, (170, 140))
food_roundbread_NS_rect = food_roundbread_NS.get_rect(center=(990, 400))

# Zoo Bread
food_bread_turtle = pygame.image.load('graphics/food-breadturtle.png')
food_bread_turtle = pygame.transform.scale(food_bread_turtle, (170, 140))
food_bread_turtle_rect = food_bread_turtle.get_rect(center=(1590, 400))

food_bread_turtle_NS = pygame.image.load('graphics/food-breadturtle-NS.png')
food_bread_turtle_NS = pygame.transform.scale(food_bread_turtle_NS, (170, 140))
food_bread_turtle_NS_rect = food_bread_turtle_NS.get_rect(center=(1590, 400))

food_bread_crocodile = pygame.image.load('graphics/food-breadcrocodile.png')
food_bread_crocodile = pygame.transform.scale(food_bread_crocodile, (170, 140))
food_bread_crocodile_rect = food_bread_crocodile.get_rect(center=(1780, 400))

food_bread_crocodile_NS = pygame.image.load('graphics/food-breadcrocodile-NS.png')
food_bread_crocodile_NS = pygame.transform.scale(food_bread_crocodile_NS, (170, 140))
food_bread_crocodile_NS_rect = food_bread_crocodile_NS.get_rect(center=(1780, 400))

# Toast
food_eggtoast = pygame.image.load('graphics/food-eggtoast.png')
food_eggtoast = pygame.transform.scale(food_eggtoast, (170, 140))
food_eggtoast_rect = food_eggtoast.get_rect(center=(790, 650))

food_eggtoast_NS = pygame.image.load('graphics/food-eggtoast-NS.png')
food_eggtoast_NS = pygame.transform.scale(food_eggtoast_NS, (170, 140))
food_eggtoast_NS_rect = food_eggtoast_NS.get_rect(center=(790, 650))

food_toast = pygame.image.load('graphics/food-toast.png')
food_toast = pygame.transform.scale(food_toast, (190, 160))
food_toast_rect = food_toast.get_rect(center=(990, 650))

food_toast_NS = pygame.image.load('graphics/food-toast-NS.png')
food_toast_NS = pygame.transform.scale(food_toast_NS, (190, 160))
food_toast_NS_rect = food_toast_NS.get_rect(center=(990, 650))

# Fruit Pie
food_pie1 = pygame.image.load('graphics/food-pie1.png')
food_pie1 = pygame.transform.scale(food_pie1, (170, 140))
food_pie1_rect = food_pie1.get_rect(center=(1190, 650))

food_pie1_NS = pygame.image.load('graphics/food-pie1-NS.png')
food_pie1_NS = pygame.transform.scale(food_pie1_NS, (170, 140))
food_pie1_NS_rect = food_pie1_NS.get_rect(center=(1190, 650))

food_pie2 = pygame.image.load('graphics/food-pie2.png')
food_pie2 = pygame.transform.scale(food_pie2, (170, 140))
food_pie2_rect = food_pie2.get_rect(center=(1390, 650))

food_pie2_NS = pygame.image.load('graphics/food-pie2-NS.png')
food_pie2_NS = pygame.transform.scale(food_pie2_NS, (170, 140))
food_pie2_NS_rect = food_pie2_NS.get_rect(center=(1390, 650))

food_rectpie = pygame.image.load('graphics/food-rectpie.png')
food_rectpie = pygame.transform.scale(food_rectpie, (170, 140))
food_rectpie_rect = food_rectpie.get_rect(center=(1590, 650))

food_rectpie_NS = pygame.image.load('graphics/food-rectpie-NS.png')
food_rectpie_NS = pygame.transform.scale(food_rectpie_NS, (170, 140))
food_rectpie_NS_rect = food_rectpie_NS.get_rect(center=(1590, 650))

food_fruitpie = pygame.image.load('graphics/food-fruitpie.png')
food_fruitpie = pygame.transform.scale(food_fruitpie, (170, 140))
food_fruitpie_rect = food_fruitpie.get_rect(center=(1790, 650))

food_fruitpie_NS = pygame.image.load('graphics/food-fruitpie-NS.png')
food_fruitpie_NS = pygame.transform.scale(food_fruitpie_NS, (170, 140))
food_fruitpie_NS_rect = food_fruitpie_NS.get_rect(center=(1790, 650))

food_blueberryfish = pygame.image.load('graphics/food-blueberryfish.png')
food_blueberryfish = pygame.transform.scale(food_blueberryfish, (170, 140))
food_blueberryfish_rect = food_blueberryfish.get_rect(center=(790, 900))

food_blueberryfish_NS = pygame.image.load('graphics/food-blueberryfish-NS.png')
food_blueberryfish_NS = pygame.transform.scale(food_blueberryfish_NS, (170, 140))
food_blueberryfish_NS_rect = food_blueberryfish_NS.get_rect(center=(790, 900))

# Sandwich
food_bagel = pygame.image.load('graphics/food-bagel.png')
food_bagel = pygame.transform.scale(food_bagel, (170, 140))
food_bagel_rect = food_bagel.get_rect(center=(990, 900))

food_bagel_NS = pygame.image.load('graphics/food-bagel-NS.png')
food_bagel_NS = pygame.transform.scale(food_bagel_NS, (170, 140))
food_bagel_NS_rect = food_bagel_NS.get_rect(center=(990, 900))

# Plain
food_pretzel = pygame.image.load('graphics/food-pretzel.png')
food_pretzel = pygame.transform.scale(food_pretzel, (170, 140))
food_pretzel_rect = food_pretzel.get_rect(center=(1190, 400))

food_pretzel_NS = pygame.image.load('graphics/food-pretzel-NS.png')
food_pretzel_NS = pygame.transform.scale(food_pretzel_NS, (170, 140))
food_pretzel_NS_rect = food_pretzel_NS.get_rect(center=(1190, 400))

food_croissant = pygame.image.load('graphics/food-croissant.png')
food_croissant = pygame.transform.scale(food_croissant, (170, 140))
food_croissant_rect = food_croissant.get_rect(center=(1390, 400))

food_croissant_NS = pygame.image.load('graphics/food-croissant-NS.png')
food_croissant_NS = pygame.transform.scale(food_croissant_NS, (170, 140))
food_croissant_NS_rect = food_croissant_NS.get_rect(center=(1390, 400))

food_chocolatebread = pygame.image.load('graphics/food-chocolatebread.png')
food_chocolatebread = pygame.transform.scale(food_chocolatebread, (130, 120))
food_chocolatebread_rect = food_chocolatebread.get_rect(center=(1190, 900))

food_chocolatebread_NS = pygame.image.load('graphics/food-chocolatebread-NS.png')
food_chocolatebread_NS = pygame.transform.scale(food_chocolatebread_NS, (130, 120))
food_chocolatebread_NS_rect = food_chocolatebread_NS.get_rect(center=(1190, 900))

food_cookies = pygame.image.load('graphics/food-cookies.png')
food_cookies = pygame.transform.scale(food_cookies, (140, 130))
food_cookies_rect = food_cookies.get_rect(center=(1390, 900))

food_cookies_NS = pygame.image.load('graphics/food-cookies-NS.png')
food_cookies_NS = pygame.transform.scale(food_cookies_NS, (140, 130))
food_cookies_NS_rect = food_cookies_NS.get_rect(center=(1390, 900))

food_creambread = pygame.image.load('graphics/food-creambread.png')
food_creambread = pygame.transform.scale(food_creambread, (130, 110))
food_creambread_rect = food_creambread.get_rect(center=(1590, 900))

food_creambread_NS = pygame.image.load('graphics/food-creambread-NS.png')
food_creambread_NS = pygame.transform.scale(food_creambread_NS, (130, 110))
food_creambread_NS_rect = food_creambread_NS.get_rect(center=(1590, 900))

food_cupcake = pygame.image.load('graphics/food-cupcake.png')
food_cupcake = pygame.transform.scale(food_cupcake, (120, 130))
food_cupcake_rect = food_cupcake.get_rect(center=(1790, 900))

food_cupcake_NS = pygame.image.load('graphics/food-cupcake-NS.png')
food_cupcake_NS = pygame.transform.scale(food_cupcake_NS, (120, 130))
food_cupcake_NS_rect = food_cupcake_NS.get_rect(center=(1790, 900))

discount_badge = pygame.image.load('graphics/tags/discount.png')
discount_badge = pygame.transform.scale(discount_badge, (30, 35))

empty_rect = None
small_food_cupcake = pygame.transform.scale(food_cupcake, (70, 60))
small_food_cupcake_rect = empty_rect
small_food_pie1 = pygame.transform.scale(food_pie1, (70, 60))
small_food_pie1_rect = empty_rect
small_food_pie2 = pygame.transform.scale(food_pie2, (70, 60))
small_food_pie2_rect = empty_rect
small_food_rectpie = pygame.transform.scale(food_rectpie, (70, 60))
small_food_rectpie_rect = empty_rect
small_food_fruitpie = pygame.transform.scale(food_fruitpie, (70, 60))
small_food_fruitpie_rect = empty_rect
small_food_blueberryfish = pygame.transform.scale(food_blueberryfish, (70, 60))
small_food_blueberryfish_rect = empty_rect
small_food_bread_turtle = pygame.transform.scale(food_bread_turtle, (70, 60))
small_food_bread_turtle_rect = empty_rect
small_food_bread_crocodile = pygame.transform.scale(food_bread_crocodile, (70, 60))
small_food_bread_crocodile_rect = empty_rect
small_food_baguette = pygame.transform.scale(food_baguette, (70, 60))
small_food_baguette_rect = empty_rect
small_food_roundbread = pygame.transform.scale(food_roundbread, (70, 60))
small_food_roundbread_rect = empty_rect
small_food_eggtoast = pygame.transform.scale(food_eggtoast, (70, 60))
small_food_eggtoast_rect = empty_rect
small_food_toast = pygame.transform.scale(food_toast, (70, 60))
small_food_toast_rect = empty_rect
small_food_pretzel = pygame.transform.scale(food_pretzel, (70, 60))
small_food_pretzel_rect = empty_rect
small_food_croissant = pygame.transform.scale(food_croissant, (70, 60))
small_food_croissant_rect = empty_rect
small_food_bagel = pygame.transform.scale(food_bagel, (70, 60))
small_food_bagel_rect = empty_rect
small_food_chocolatebread = pygame.transform.scale(food_chocolatebread, (70, 60))
small_food_chocolatebread_rect = empty_rect
small_food_cookies = pygame.transform.scale(food_cookies, (70, 60))
small_food_cookies_rect = empty_rect
small_food_creambread = pygame.transform.scale(food_creambread, (70, 60))
small_food_creambread_rect = empty_rect

small_update_stock_food_cupcake = pygame.transform.scale(food_cupcake, (70, 60))
small_update_stock_food_cupcake_rect = empty_rect
small_update_stock_food_pie1 = pygame.transform.scale(food_pie1, (70, 60))
small_update_stock_food_pie1_rect = empty_rect
small_update_stock_food_pie2 = pygame.transform.scale(food_pie2, (70, 60))
small_update_stock_food_pie2_rect = empty_rect
small_update_stock_food_rectpie = pygame.transform.scale(food_rectpie, (70, 60))
small_update_stock_food_rectpie_rect = empty_rect
small_update_stock_food_fruitpie = pygame.transform.scale(food_fruitpie, (70, 60))
small_update_stock_food_fruitpie_rect = empty_rect
small_update_stock_food_blueberryfish = pygame.transform.scale(food_blueberryfish, (70, 60))
small_update_stock_food_blueberryfish_rect = empty_rect
small_update_stock_food_bread_turtle = pygame.transform.scale(food_bread_turtle, (70, 60))
small_update_stock_food_bread_turtle_rect = empty_rect
small_update_stock_food_bread_crocodile = pygame.transform.scale(food_bread_crocodile, (70, 60))
small_update_stock_food_bread_crocodile_rect = empty_rect
small_update_stock_food_baguette = pygame.transform.scale(food_baguette, (70, 60))
small_update_stock_food_baguette_rect = empty_rect
small_update_stock_food_roundbread = pygame.transform.scale(food_roundbread, (70, 60))
small_update_stock_food_roundbread_rect = empty_rect
small_update_stock_food_eggtoast = pygame.transform.scale(food_eggtoast, (70, 60))
small_update_stock_food_eggtoast_rect = empty_rect
small_update_stock_food_toast = pygame.transform.scale(food_toast, (70, 60))
small_update_stock_food_toast_rect = empty_rect
small_update_stock_food_pretzel = pygame.transform.scale(food_pretzel, (70, 60))
small_update_stock_food_pretzel_rect = empty_rect
small_update_stock_food_croissant = pygame.transform.scale(food_croissant, (70, 60))
small_update_stock_food_croissant_rect = empty_rect
small_update_stock_food_bagel = pygame.transform.scale(food_bagel, (70, 60))
small_update_stock_food_bagel_rect = empty_rect
small_update_stock_food_chocolatebread = pygame.transform.scale(food_chocolatebread, (70, 60))
small_update_stock_food_chocolatebread_rect = empty_rect
small_update_stock_food_cookies = pygame.transform.scale(food_cookies, (70, 60))
small_update_stock_food_cookies_rect = empty_rect
small_update_stock_food_creambread = pygame.transform.scale(food_creambread, (70, 60))
small_update_stock_food_creambread_rect = empty_rect


increment_porcentage_button_rect = empty_rect
decrement_porcentage_button_rect = empty_rect

cart = {}
start_date = datetime.now()
product_list = createStock(bakery_products, start_date)
discountItem(start_date.day, start_date.month, product_list)
total_price = 0

products_text = {}

ticket_components = {}

game_selected = ''
login_user_button = None
login_manager_button = None

while running:  # The game will be continuously updated.
    listen_to_key_binding()
    if game_active:
        if game_selected == 'USER':
            render_user_game_screen()
        elif game_selected == 'MANAGER':
            render_manager_game_screen()
        else:
            # Draw the button
            login_user_button = draw_button(800, 400, 350, 50, "LOGIN AS USER", 'Grey', 'Black')
            login_manager_button = draw_button(800, 500, 350, 50, "LOGIN AS MANAGER", 'Grey', 'Black')

    pygame.display.update()  # update the screen
    clock.tick(60)  # while True runs 60 times per second
