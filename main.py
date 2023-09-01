import random

options = ('piedra','papel','tijera')

rounds = 1
computer_wins = 0
user_wins = 0
empates=0

while True:

    print('*'*10)
    print(f'Round {rounds}')
    print(f'User Wins => {user_wins}')
    print(f'Computer Wins => {computer_wins}')
    print(f'Empates => {empates}')
    print('')

    user_option = input('Elije piedra, papel o tijera => ').lower()
    rounds+=1

    print('')
    print(f'User option => {user_option}')
    computer_option = random.choice(options)
    print(f'Computer option => {computer_option}')

    if not user_option in options:
        print('Esa opcion no es valida!!')
        continue

    if user_option == computer_option:
        empates+=1
        print('Empate')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Felicidades ganaste!!')
            user_wins+=1
        else:
            print('Papel gana a pieda')
            print('Computer gana!!')
            computer_wins+=1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Felicidades ganaste!!')
            user_wins+=1
        else:
            print('Tijera le gana a papel')
            print('Computer gana!!')
            computer_wins+=1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Felicidades ganaste!!')
            user_wins+=1
        else:
            print('Piedra gana a tijera')
            print('Computer gana!!')
            computer_wins+=1

    if computer_wins == 2:
        print('Computer gana el juego!!')
        break
    
    if user_wins == 2:
        print('Haz ganado el juego!!')
        break
