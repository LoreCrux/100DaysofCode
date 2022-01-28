print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_dict = {
    'small_pizza': 15,
    'medium_pizza': 20,
    'large_pizza': 25,
    'pep_small': 2,
    'pep_medium_large': 3,
    'extra_cheese': 1
}
order = 0

if size == 'L':
    order += pizza_dict['large_pizza']
    if add_pepperoni == 'Y':
        order += pizza_dict['pep_medium_large']
    if extra_cheese == 'Y':
        order += pizza_dict['extra_cheese']
         
if size =='M':
    order += pizza_dict['medium_pizza']
    if add_pepperoni == 'Y':
        order += pizza_dict['pep_medium_large']
    if extra_cheese == 'Y':
        order += pizza_dict['extra_cheese']

if size == 'S':
    order += pizza_dict['small_pizza']
    if add_pepperoni == 'Y':
        order += pizza_dict['pep_small']
    if extra_cheese == 'Y':
        order += pizza_dict['extra_cheese']

print(f'Your final bill is: ${order}.')