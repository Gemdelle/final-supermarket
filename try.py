cart = {'Manzana': {'quantity': 2, 'type': 'F'}, 'Cartera': {'quantity': 1, 'type': 'L'}, 'Cartera 2': {'quantity': 1, 'type': 'R'}, 'Cartera 3': {'quantity': 1, 'type': 'R'}, 'Cartera 4': {'quantity': 1, 'type': 'R'}, 'Pera': {'quantity': 1, 'type': 'F'}}

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

print(f'The most purchased category is "{most_purchased_category}" with {most_purchased_category_num} items')
