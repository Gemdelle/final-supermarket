import random
from datetime import datetime, timedelta

products = {
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

# start_date = input('Ingrese una fecha [YYYY-MM-DD]: ')
start_date = '2023-02-01'
start_date = datetime.strptime(start_date, '%Y-%m-%d')

def createStock(products):
    for product in products:
        products[product]['stock'] = random.randint(0,300)
        products[product]['expire_date'] = (start_date + timedelta(days=random.randint(30, 365))).strftime('%Y-%m-%d')
        products[product]['price'] = random.randint(350,1200)

createStock(products)

for key,value in products.items():
    print(f"{key}: {value}")