# if

'''
if True:
    print('deberia ejecutarse')

if False:
    print('no deberia ejecutarse')
'''


pet = input('Cual es tu animal favorito, perro, gato o pez? => ')    

if pet == 'perro':
    print('Genial te gustan los perros')
elif pet == 'gato':
    print('Genial te gustan los gatos')
elif pet == 'pez':
    print('Genial te gustan los gatos')
else:
    print('No reconzco esa mascota')


''' 
stock = int(input('Ingresa el numero de stock => '))
if stock >= 100 and stock <= 1000:
    print('El stock es correcto')
else:
    print('El stock es incorrecto')
'''