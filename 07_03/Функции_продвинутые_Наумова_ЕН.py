tables = {
    1: ['Jiho', False],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: []
}

def assign_table(table_number, name, vip_status=False):
    tables[table_number] = [name, vip_status]
    return tables

assign_table(6, 'Yoni', False)
assign_table(4, 'Карла')

print(tables)

def print_order(*order_items):
    print(order_items)

print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')

tables = {
 1: {
 'name': 'Jiho',
 'vip_status': False,
 'order': 'Orange Juice, Apple Juice'
 },
 2: {},
 3: {},
 4: {},
 5: {},
 6: {},
 7: {},
}

def assign_table(table_number, name, vip_status=False):
   tables[table_number]['name'] = name
   tables[table_number]['vip_status'] = vip_status
   return tables

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for dish in order_items:
        print(dish)
    return tables

print(assign_table(2, 'Arwa', True))
print(assign_and_print_order(2, 'Стейк', 'Морской окунь', 'Бутылка вина'))

tables = {
 1: {
 'name': 'Chioma',
 'vip_status': False,
 'order': {
 'drinks': 'Orange Juice, Apple Juice',
 'food_items': 'Pancakes'
 }
 },
 2: {},
 3: {},
 4: {},
 5: {},
 6: {},
 7: {},
}

def  assign_food_items(**order_items):
    return order_items

print(assign_food_items(food='Pancakes, Poached Egg', drinks='Water'))

def calculate_price_per_person(total, tip, split):
 total_tip = total * (tip / 100)
 split_price = (total + total_tip) / split
 print(split_price)

table_7_total = [534.50,  20.0, 5]
calculate_price_per_person(*table_7_total)