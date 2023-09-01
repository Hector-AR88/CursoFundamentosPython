numbers = (1,2,3,5,5)
strings = ('hector','arumy','crystal')

print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

print(strings.index('arumy'))
print(numbers.count(5))

my_list = list(strings)
print(my_list)
print(type(my_list))

my_list[1] = 'ruby'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))

