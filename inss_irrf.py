#Entrada
salario = float(input('Digite o seu salário: '))

#Processamento: calculo do inss
if salario <= 1320:
    inss = salario * 0.075
elif salario <= 2571.29:
    inss = salario * 0.09 - 19.80
elif salario <= 3856.94:
    inss = salario * 0.12 - 96.94
elif salario <= 7507.49:
    inss = salario * 0.14 - 174.00
else:
    inss = 876.97 #teto

#Declaração da base do irrf
base_irrf = salario - inss
#CALCULO IRRF
if base_irrf <= 1903.90:
    irrf = 0
elif base_irrf <= 2826.65:
    irrf = base_irrf * 0.075 - 142.80
elif base_irrf <= 3751.05:
    irrf = base_irrf * 0.15 - 354.80
elif base_irrf <= 4664.68:
    irrf = base_irrf * 0.225 - 636.13
else:
    irrf = base_irrf * 0.275 - 869.36

#Declaração do salario liquido
slario_liquido = salario - inss - irrf


#saidas
print('-------------------------------')
print(f'Salário bruto R$ {salario:.2f}')
print('-------------------------------')
print(f'Desconto do INSS R$ {inss:.2f}')
print('-------------------------------')
print(f'Base do IRFF R$ {base_irrf:.2f}')
print('--------------------------------')
print(f'Desconto do IRRF R$ {irrf:.2f}')
print('-------------------------------')
print(f'Salário líquido R$ {slario_liquido:.2f}')