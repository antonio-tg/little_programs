import random

lista = ['piedra', 'papel', 'tijeras']
manou = input('Vamos a jugar piedra, papel y tijeras, ingrese su elección: ').lower()
manom= ''
while manou != manom:
    while manou not in lista:
        manou = input('Esa no es una elección valida, por favor teclee una de las siguientes opciones: piedra, papel y tijeras: ')

    print(f'Usted ingreso {manou}')
    manom = random.choice(lista)
    print(f'Yo escojo {manom}')
    if manou == manom:
        print('Jugemos de nuevo')
        manou = input('Vamos a jugar piedra, papel y tijeras, ingrese su elección: ')
    else:
        if manou == 'piedra':
            if manom == 'papel':
                print('Usted pierde')
            else:
                print('Usted gana')
        if manou == 'papel':
            if manom == 'piedra':
                print('Usted gana')
            else:
                print('Usted gana')
        if manou == 'tijeras':
            if manom == 'papel':
                print('Usted gana')
            else:
                print('Usted pierde')
        break
