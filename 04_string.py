# Strings
name = 'Hector'
last_name = 'Alpuche Rodriguez'
full_name = name + ' ' + last_name
age = 34
print(full_name)

quote = "I'am Hector"
print(quote)

quote2 = 'He said "Hello"'
print(quote2)

# format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print(template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name,last_name)
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print(template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"
print(template)
