import random

lista = ['piedra', 'papel', 'tijeras']
class ppt():
    manou = ''
    manom = '' 

    def manomachine(self):
        self.manom = random.choice(lista)
        return self.manom

    def juego(self):
        if self.manou == self.manom:
            return 'Empatamos, juguemos de nuevo'
        else:
            if self.manou == 'piedra':
                if self.manom == 'papel':
                    return 'Usted pierde'
                else:
                    return 'Usted gana'
            if self.manou == 'papel':
                if self.manom == 'piedra':
                    return 'Usted gana'
                else:
                    return 'Usted pierde'
            if self.manou == 'tijeras':
                if self.manom == 'papel':
                    return 'Usted gana'
                else:
                    return 'Usted pierde'

resultado = 'Empatamos, juguemos de nuevo'
print('Vamos a jugar piedra, papel y tijeras')
while resultado == 'Empatamos, juguemos de nuevo':
    ppt_juego = ppt()
    ppt_juego.manou = input('Ingrese su elección: ').lower()
    while ppt_juego.manou not in lista:
        ppt_juego.manou = input('Esa no es una elección valida, por favor teclee una de las siguientes opciones: piedra, papel y tijeras: ').lower()
    manom = ppt_juego.manomachine()
    print(f'Yo escojo {manom}')
    resultado = ppt_juego.juego()
    print(resultado)
