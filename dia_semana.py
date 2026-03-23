# Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'
# Qualquer outro numero exibir: 'Opção inválida!'

#-------------------------------------------------------------------------------------

dia = int(input('Digite um número de 1-7: '))

match dia:
    case 1:
        print('Segunda')
    case 2:
        print('terça')
    case 3:
        print('Quarta')
    case 4:
        print('Quinta')
    case 5:
        print('Sexta')
    case 6:
        print('Sábado')
    case 7:
        print('Domingo')
    case _:
        print('Dia não existe')