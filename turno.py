# Desenvolva um programa que pergunte em que turno você estuda. 
# Peça para digitar: M-Matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# Obs.: Somente letras maiúsculas para M, V ou N.

#==========================================================================================================

turno = input('Em qual turno você estuda? ')
# M - matutino
# V - vespertino
# N - noturno
if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noita')
else:
    print('Valor inválido')