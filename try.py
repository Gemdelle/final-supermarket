cart = {'Manzana': {'quantity': 2, 'type': 'F'}, 'Cartera': {'quantity': 1, 'type': 'L'}, 'Cartera 2': {'quantity': 1, 'type': 'R'}, 'Cartera 3': {'quantity': 1, 'type': 'R'}, 'Cartera 4': {'quantity': 1, 'type': 'R'}, 'Pera': {'quantity': 1, 'type': 'F'}}

def ticket(cart):
    for item, details in cart.items():
        print(f'Item: {item} ------------------- {details["price"]}')
