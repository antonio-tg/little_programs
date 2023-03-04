# En este caso, nuestro objetivo es averiguar exactamente la cantidad de propina que hay que proporcionar después de un servicio. En este caso, hay que solicitar la factura total. Con esto, aplicaremos la propina para el 18%, 20% y 25%.

# Se calcula el porcentaje de propina que se les cobrará a los comenzales
factura = ''
while str(type(factura))!= "<class 'float'>":
    try:
        factura = float(input('¿Cuál es la factura total de hoy, por favor? '))
    except:
        pass
if factura > 0: propina = 18
if factura > 99.99999: propina = 20
if factura > 199.9999: propina = 25
# Se pide el número de comezales 
comenzales = ''
while str(type(comenzales))!= "<class 'int'>":
    try:
        comenzales = int(input('¿Cuanto comenzales son? '))
    except:
        pass
# Se le pregunta al usuario si desea divir la cuenta en partes iguales o si prefiere usar una distribución distinta
pesos = ''
desicion = ''
while desicion not in {'si','no'}:
    desicion = input('Desea devidir la cuenta en partes iguales, si o no? ').lower()
    if desicion == 'no':
        while len(pesos) != comenzales:
            pesos = input('Introduzca el porcentajes en los que desea divir la comida y asegurese que sumen 100% ').split(',')
            print(f'La propina aplicando el {propina}% es ${round(factura*(propina/100),2)}, que contabiliza un total de ${round(factura*(1 + propina/100),2)} y les toca de a:')
            for i in range(len(pesos)):
                print(f'Al comenzal {i+1} le toca ${round(factura*(1 + propina/100)*(float(pesos[i])/100),2)}')
    if desicion == 'si':
        print(f'La propina aplicando el {propina}% es ${round(factura*(propina/100),2)}, que contabiliza un total de ${round(factura*(1 + propina/100),2)} y les toca de a {round(factura*(1 + propina/100)*(1/comenzales),2)}')
