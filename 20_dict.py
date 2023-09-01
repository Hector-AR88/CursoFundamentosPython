person = {
    'name':'hector',
    'last_name':'Alpuche rodriguez',
    'age':34,
    'langs':['python','javascript']
}


print(person)

person['name'] = 'Hercules'
person['age'] -= 4
person['langs'].append('rust')
print(person)

del person['age']
person.pop("last_name")
print(person)

print("ITEMS")
print(person.items())
print("KEYS")
print(person.keys())
print("VALUES")
print(person.values())