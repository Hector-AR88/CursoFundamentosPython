# for element in range(1,21):
#     print(element)

# my_list = [23,45,67,89,43]
# for element in my_list:
#     print(element)

# my_tuple = ('nico','julio','hector')
# for element in my_tuple:
#     print(element)


# product = {
#     'name': 'camisa',
#     'price': 100,
#     'stock': 13
# }
# for key in product:
#     print(key, '=>', product[key])
# for key, value in product.items():
#     print(key, '=>', value)

people = [
    {
        'name':'Hector',
        'age':'34'
    },
    {
        'name':'Arumy',
        'age':'23'
    },
    {
        'name':'Ruby',
        'age':'50'
    }
]

for person  in people:
    pos=int(people.index(person))
    print(f'Person # {pos+1}')
    print(f"name => {person['name']}")   
