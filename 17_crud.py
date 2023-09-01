# CRUD Create, Read, Update & Delete

# Create *********************************
numbers = [1,2,3,4,5]

# Read ***********************************
print(numbers)

# Update *********************************
numbers[-1]=10
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'Hola')
print(numbers)

numbers.insert(3, 'Change')
print(numbers)

tasks = ['todo 1', 'todo 2','todo 3']
new_list = numbers + tasks
print(new_list)

what_index = new_list.index('todo 2')
new_list[what_index] = 'todo changed'
print(new_list)

new_list.reverse()
print(new_list)

numbers_a = [1,4,6,3]
print(numbers_a)
numbers_a.sort()
print(numbers_a)

strings = ['re','ab','ed']
print(strings)
strings.sort()
print(strings)

# new_list.sort()


# Delete *********************************
new_list.remove('todo 1')
print(new_list)

new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)
