# Desenvolver um programa que leia o peso e a altura de uma pessoa e calcule seu imc utilizando a fórmula: imc = peso / altura * altura
# Com o imc exiba para o usuário seu imc e a classificação:
# IMC		Classificação
# < 16		'Magreza grave'
# 16 a < 17	'Magreza moderada'
# 17 a < 18,5	'Magreza leve'
# 18,5 a < 25	'Saudável'
# 25 a < 30	'Sobrepeso'
# 30 a < 35	'Obesidade Grau I'
# 35 a < 40	'Obesidade Grau II (severa)'
# ≥ 40		'Obesidade Grau III (mórbida)'

#-------------------------------------------------------------------------------------------------------------------------------------------

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (pow(altura, 2))

if imc < 16:
    print(f'{imc:.2f} Magreza grave')
elif imc < 17:
    print(f'{imc:.2f} Magreza moderada')
elif imc < 18.5:
    print(f'{imc:.2f} Magreza leve')
elif imc  < 25:
    print(f'{imc:.2f} Saudável')
elif imc < 30:
    print(f'{imc:.2f} Sobrepeso')
elif imc < 35:
    print(f'{imc:.2f} Obesidade Grau I')
elif imc  < 40:
    print(f'{imc:.2f} Obesidade Grau II (severa)')
elif imc > 40:
    print(f'{imc:.2f} Obesidade Grau III (mórbida)')