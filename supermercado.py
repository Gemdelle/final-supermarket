# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:50:40 2023

@author: milu2
"""

# T.P. Supermercado

# Información a tener en cuenta de cada producto: código, descripción, stock, precio
# unitario, fecha de vencimiento y tipo de producto, por ejemplo: "L" para lácteos, "V" para
# verdulería, etc.

# Products
products = {
    '100': {
        'description': 'Leche',
        'stock': 50,
        'expire_date': '2023-12-15',
        'price': 300,
        'type': 'L'
    },
    '101': {
        'description': 'Manzana',
        'stock': 100,
        'expire_date': '2023-11-10',
        'price': 150,
        'type': 'V'
    },
    '102': {
        'description': 'Yogur',
        'stock': 30,
        'expire_date': '2023-12-05',
        'price': 180,
        'type': 'L'
    },
    '103': {
        'description': 'Zanahoria',
        'stock': 75,
        'expire_date': '2023-11-30',
        'price': 100,
        'type': 'V'
    },
    '104': {
        'description': 'Pan',
        'stock': 60,
        'expire_date': '2023-11-25',
        'price': 90,
        'type': 'P'
    },
    '105': {
        'description': 'Pollo',
        'stock': 20,
        'expire_date': '2023-12-10',
        'price': 400,
        'type': 'C'
    },
    '106': {
        'description': 'Cepillo de Dientes',
        'stock': 25,
        'expire_date': '2023-12-01',
        'price': 50,
        'type': 'H'
    },
    '107': {
        'description': 'Pasta de Dientes',
        'stock': 20,
        'expire_date': '2023-12-02',
        'price': 60,
        'type': 'H'
    },
    '108': {
        'description': 'Arroz',
        'stock': 80,
        'expire_date': '2023-11-29',
        'price': 200,
        'type': 'P'
    },
    '109': {
        'description': 'Cereal',
        'stock': 40,
        'expire_date': '2023-12-08',
        'price': 120,
        'type': 'L'
    },
    '110': {
        'description': 'Naranja',
        'stock': 90,
        'expire_date': '2023-11-20',
        'price': 120,
        'type': 'V'
    },
}

def defineAction():
    return input('\nIngrese la acción que desea realizar [A/D/E/L]: ').upper()

def addProduct(product_list):
    code = input('Código: ')
    description = input('Descripción: ')
    stock = input('Stock: ')
    price = input('Precio unitario: ')
    expire_date = input('Fecha de vencimiento: ')
    kind = input('Tipo [L/V/F]: ')
    
    if code not in product_list:
        product_list[code] = {
            'description': description,
            'stock': stock,
            'price': price,
            'expire_date': expire_date,
            'kind': kind
        }
    
    return product_list
  
def deleteProduct(product_list):
    code = input('Ingrese el código del producto: ')
    del product_list[code]
    
    return product_list

def printProducts(product_list):
    print()
    for product in product_list:
        print(f'Producto {product}: {product_list[product]}')

def main():

    action = defineAction()
    
    while action != 'E':
        if action == 'A':
            addProduct(products)
        elif action == 'D':
            deleteProduct(products)
        elif action == 'L':
            printProducts(products)
        action = defineAction()
    
main()
    