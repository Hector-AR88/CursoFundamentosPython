'''
while True:
    print('Se ejecuta')

counter = 0
while counter < 10:
    counter += 1
    print(counter)
print(counter)

counter = 0
while counter < 20:
    counter += 1
    print(counter)
    if counter == 15:
        break
'''

counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)

