my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name':'Hector',
    'last_name':'Alpuche Rodriguez',
    'age':34
}

print(my_dict)
print(len(my_dict))
print(my_dict['name'])
print(my_dict['last_name'])
print(my_dict['age'])
print(my_dict.get('name'))
print(my_dict.get('a_value'))

print('avion' in my_dict)
print('avalue' in my_dict)




