# T.P. Supermercado

# Información a tener en cuenta de cada producto: código, descripción, stock, precio
# unitario, fecha de vencimiento y tipo de producto, por ejemplo: "L" para lácteos, "V" para
# verdulería, etc.
import sqlite3
import random
from datetime import datetime, timedelta

# Products

bakery_products = {
    '100': {
        'description': 'Strawberry Pie',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'F',
        'discount': False
    },
    '101': {
        'description': 'Grape Pie',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'F',
        'discount': False
    },
    '102': {
        'description': 'Apple Pie',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'F',
        'discount': False
    },
    '103': {
        'description': 'Fruit Pie',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'F',
        'discount': False
    },
    '104': {
        'description': 'Blueberry Pie',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'F',
        'discount': False
    },
    '105': {
        'description': 'Bread Turtle',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'Z',
        'discount': False
    },
    '106': {
        'description': 'Bread Crocodile',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'Z',
        'discount': False
    },
    '107': {
        'description': 'Baguette',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'B',
        'discount': False
    },
    '108': {
        'description': 'Bun',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'B',
        'discount': False
    },
    '109': {
        'description': 'Egg Toast',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'T',
        'discount': False
    },
    '110': {
        'description': 'Butter Toast',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'T',
        'discount': False
    },
    '111': {
        'description': 'Pretzel',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'P',
        'discount': False
    },
    '112': {
        'description': 'Croissant',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'P',
        'discount': False
    },
    '113': {
        'description': 'Bagel',
        'stock': 0,
        'expire_date': '',
        'price': 0,
        'type': 'S',
        'discount': False
    }
}

def greeting():
    print('Las acciones que puede hacer son: \nA: Add (agregar)')

def defineDate():
    print('Bienvenido al supermercado X. Ingrese la fecha del día de hoy antes de comenzar su compra: ')
    start_date = input('Fecha [YYYY-MM-DD]: ')
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    return start_date

def createStock(products,start_date):
    for product in products:
        products[product]['stock'] = random.randint(0,300)
        products[product]['expire_date'] = (start_date + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
        products[product]['price'] = random.randint(350,1200)

    # Hacer que no haya stock de 2 productos al inicio
    products[str(random.randint(100,113))]['stock'] = 0
    products[str(random.randint(100,113))]['stock'] = 0

    # Ver los productos de los que no hay stock
    # for key,value in products.items():
    #     if products[key]['stock'] == 0:
    #         print(f"{key}: {value}")

def defineAction():
    return input('\nIngrese la acción que desea realizar [A/D/E/L]: ').upper()

def addProduct(product_list):
    code = input('Código: ')
    description = input('Descripción: ')
    stock = int(input('Stock: '))
    price = input('Precio unitario: ')
    expire_date = input('Fecha de vencimiento: ')
    kind = input('Tipo [L/V/F]: ')
    
    if code not in product_list:
        product_list[code] = {
            'description': description,
            'stock': stock,
            'price': price,
            'expire_date': expire_date,
            'kind': kind,
            'discount': False
        }
    
    return product_list
  
def deleteProduct(product_list):
    code = input('Ingrese el código del producto: ')
    del product_list[code]
    
    return product_list

def printProducts(product_list):
    print()
    for code,product in product_list.items():
        print(f'\n-------------\n{code}')
        for key,value in product.items():
            print(f'{key}: {value}')

def updateStock(product_list):
    print('Ingrese la información del producto a vender:')
    user_code = input('Código: ')
    quantity = int(input('Cantidad: '))
    
    if product_list[user_code]['stock'] - quantity >= 0:
        product_list[user_code]['stock'] -= quantity
        
def updatePrice(product_list):
    print('Ingrese la información del producto a modificar el precio: ')
    user_code = input('Código: ')
    percentage = float(input('Porcentaje a modificar: '))
        
    product_list[user_code]['price'] = product_list[user_code]['price'] + product_list[user_code]['price'] * percentage  

def verifyStock(product_list,cart):
    print('Ingrese la información del producto que desea comprar: ')
    user_code = input('Código: ')
    quantity = int(input('Cantidad: '))
    product = product_list[user_code]["description"]

    if product_list[user_code]['stock'] < quantity:
        print(f'No hay stock disponible del el producto {product}')
    else:
        if product in cart:
            cart[product]['quantity'] += quantity
            cart[product]['pay'] = quantity * cart[product]['price']
        else:
            cart[product] = {'quantity': quantity,'type': product_list[user_code]['type'], 'pay': product_list[user_code]['price'] * quantity}
        print(f'Has agregado {quantity} de {product} al carrito por un precio de {(product_list[user_code]["price"])*quantity}')
        product_list[user_code]['stock'] -= quantity

def viewCart(cart):
    for product in cart:
        print(f'{product}: {cart[product]["quantity"]}')

def updateStock(product_list):
    print('Ingrese la información del producto que desea reponer: ')
    user_code = input('Código: ')
    stock_limit = int(input('Mínimo de stock requerido: '))

    if product_list[user_code]['stock'] < stock_limit:
        print(f'El stock del producto {product_list[user_code]["description"]} está por debajo del límite.')
        stock_update = int(input('Cantidad de stock a reponer: '))
        product_list[user_code]['stock'] = stock_limit + stock_update 
    else:
        print(f'El stock del producto {product_list[user_code]["description"]} es de {product_list[user_code]["stock"]}, está por encima del mínimo {stock_limit}')

def delivery():
    print('\nIngrese la información para realizar el envío: ')
    name = input('Nombre y apellido: ')
    dni = input('DNI: ')
    address = input('Domicilio: ')
    phone_number = input('Número de teléfono: ')
    payment_method = input('Método de pago [T/E]: ').upper()

    print(f'\n-------------------------------\nInformación de pago\n\nNombre: {name}\nDNI: {dni}\nDirección: {address}\nNúmero de teléfono: {phone_number}\nMétodo de pago: {payment_method}\n-------------------------------\n')
    repeat = input('¿Es correcta la información? [Y/N]: ').upper()
    
    while repeat == 'N':
        print()
        name = input('Nombre y apellido: ')
        dni = input('DNI: ')
        address = input('Domicilio: ')
        phone_number = input('Número de teléfono: ')
        payment_method = input('Método de pago [T/E]: ').upper()
        print(f'\n-------------------------------\nInformación de pago:\n\nNombre: {name}\nDNI: {dni}\nDirección: {address}\nNúmero de teléfono: {phone_number}\nMétodo de pago: {payment_method}\n-------------------------------\n')
        repeat = input('¿Es correcta la información? [Y/N]: ').upper()

    print('Los datos del envío han sido ingresados correctamente.')

def mostPurchasedItem(cart):
    most_purchased_item = ''
    item_quantity = 0

    for item in cart:
        if cart[item]['quantity'] > item_quantity:
            most_purchased_item = item
            item_quantity = cart[item]['quantity']

    print(f'\nInformación de producto más llevado: \nProducto: {most_purchased_item}\nCantidad: {item_quantity}')

def mostPurchasedItemType(cart):

    types = {}

    for item in cart:
        item_type = cart[item]['type']

        if item_type not in types:
            types[item_type] = 1
        else: 
            types[item_type] += 1

    # Create a list of tuples from the types dictionary
    types_arr = []
    for item_type in types:
        types_arr.append(types[item_type])
        types_arr.append(item_type)

    most_purchased_category = ''
    most_purchased_category_num = 0
    for i in range(len(types_arr)-1):
        if isinstance(types_arr[i], int):
            if types_arr[i] > most_purchased_category_num:
                most_purchased_category_num = types_arr[i]
                most_purchased_category = types_arr[i+1]

    print(f'The most purchased category is "{most_purchased_category}" with {most_purchased_category_num} items.')

    # print(f'\nProducto más llevado por tipo:\n\n')

def deleteOldProducts(day,month,product_list):
    old_products = {}

    product_list_copy = product_list.copy()

    for product_code, product_data in product_list_copy.items():
        expire_month = int(product_data['expire_date'].split('-')[1])
        expire_day = int(product_data['expire_date'].split('-')[2])
        if expire_month == month and (expire_day <= day):
            # Move the product to the old_products dictionary
            old_products[product_code] = product_data
            # Remove the product from the original product list
            del product_list[product_code]
    
    print(old_products)

def discountItem(day,month,product_list):

    for product_code, product_data in product_list.items():
        expire_month = int(product_data['expire_date'].split('-')[1])
        expire_day = int(product_data['expire_date'].split('-')[2])
        if (month == expire_month and expire_day - day > 7) or (month != expire_month and (31 - day + expire_day) > 7):
            product_list[product_code]['discount'] = True
            product_list[product_code]['price'] = product_list[product_code]['price'] - product_list[product_code]['price'] * 0.1

# def ticket(cart):
#     print(cart)
    # for item, details in cart.items():
    #     print(f'Item: {item} ------------------- {details["price"]}')

def main():

    greeting()
    start_date = defineDate()
    products = createStock(bakery_products,start_date)

    cart = {}
    old_products = {}

    action = defineAction()
    
    while action != 'E':
        if action == 'A': # Add
            addProduct(products)
        elif action == 'D': # Delete
            deleteProduct(products)
        elif action == 'L': # List
            printProducts(products)
        elif action == 'S': # Sell
            updateStock(products)
        elif action == 'UP': # Update price
            updatePrice(products)
        elif action == 'B': # Buy
            verifyStock(products,cart)
        elif action == 'C': # Cart
            viewCart(cart)
        elif action == 'US': # Update Stock
            updateStock(products)
        elif action == 'H': # Home
            delivery()
        elif action == 'MP':
            mostPurchasedItem(cart)
        elif action == 'MPT':
            mostPurchasedItemType(cart)
        elif action == 'DOP': # Delete Old Products
            deleteOldProducts(start_date,products)
        action = defineAction()
    
    ticket(cart)

main()

# [X] Agregar un nuevo producto.
# [X] Eliminar un producto dado su código.
# [X] Listar todos los productos de una forma prolija.
# [X] Actualizar el stock cuando se vende un producto.
# [X] Actualizar el precio unitario de un producto determinado en un cierto procentaje.
# [X] Determinar la existencia de un producto para poder vender la cantidad solicitada.
# [X] Reponer un producto cuando el stock está por debajo de un mínimo requerido.
# [X] Pedir los datos de un cliente para hacer envío a domicilio.
# [X] Determinar cuál es el artículo más vendido.
# [-] Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén vencidos.
# [O] Simular la venta a un cliente y emitir el ticket de venta.
# [-] Si el producto vence en una semana hacer un 10% de descuento y agregarlo al objeto.
# [-] Determinar el producto más vendido dependiendo del tipo de producto.