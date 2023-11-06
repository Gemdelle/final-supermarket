# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:50:40 2023

@author: milu2
"""

# T.P. Supermercado

# Información a tener en cuenta de cada producto: código, descripción, stock, precio
# unitario, fecha de vencimiento y tipo de producto, por ejemplo: "L" para lácteos, "V" para
# verdulería, etc.

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
        product_list[code] = [description, stock, price, expire_date, kind]
    
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
    products = {
        '100': {
            'description': ,
            'stock': ,
            'expire date': ,
            
        }['Leche', 50, 300, '2023-12-15', 'L'],
        '101': ['Manzana', 100, 150, '2023-11-10', 'V'],
        '102': ['Yogur', 30, 180, '2023-12-05', 'L'],
        '103': ['Zanahoria', 75, 100, '2023-11-30', 'V'],
        '104': ['Pan', 60, 90, '2023-11-25', 'P'],
        '105': ['Pollo', 20, 400, '2023-12-10', 'C'],
        '107': ['Cepillo de Dientes', 25, 50, '2023-12-01', 'H'],
        '108': ['Pasta de Dientes', 20, 60, '2023-12-02', 'H'],
        '109': ['Arroz', 80, 200, '2023-11-29', 'P'],
        '110': ['Cereal', 40, 120, '2023-12-08', 'L'],
        '111': ['Naranja', 90, 120, '2023-11-20', 'V']
    }
    
    # products = {}
    
    action = defineAction()
    
    while action != 'E':
        if action == 'A':
            addProduct(products)
            action = defineAction()
        elif action == 'D':
            deleteProduct(products)
            action = defineAction()
        elif action == 'L':
            printProducts(products)
            action = defineAction()
            
    print(products)
    
main()
    