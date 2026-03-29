# Desenvolva um programa que recebe o salário de um funcionário e determine o reajuste segundo o seguinte critério, baseado no salário atual:
#   salários até R$ 1000,00 (incluindo)     : aumento de 20%
#   salários até R$ 1.700,00                : aumento de 15%
#   salários até R$ 2.300,00                : aumento de 10%
#   salários acima de R$ 2.300,00 em diante : aumento de 5%

# Após o processamento exibir na tela:
#   o salário antes do reajuste;
#   o percentual de aumento aplicado;
#   o valor do aumento;
#   o novo salário, após o aumento.

#-------------------------------------------------------------------------------------------------------

#Entrada
salario = float(input('Digite o valor do seu salário: '))

#Processamento dos percentuais
if salario <= 1000:
    percentual = 0.20
elif salario <= 1700:
    percentual = 0.15
elif salario <= 2300:
    percentual = 0.10
else:
    percentual = 0.05

#Processamento: calculos
aumento = salario * percentual
novo_salario = salario + aumento

#saidas
print(f'Seu antigo salário era de R$ {salario:.2f}')
print('-------------------------------------------')
print(f'O salario sofreu um aumento de {percentual * 100}%')
print('---------------------------------------------------')
print(f'O valor do aumento foi de R$ {aumento:2.2f}')
print('--------------------------------------------')
print(f'O seu novo saário é de R$ {novo_salario:.2f}')
print('---------------------------------------------')