#  Desenvolva um programa que leia quatro notas bimestrais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média final. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 8.9         B
#   Entre 6.0 e 7.4         C
#   Entre 4.0 e 5.9         D
#   Entre zero e 3.9        E
# O programa deve exibir na tela:
#   1. As quatro notas bimestrais,
#   2. A média final,
#   3. O conceito correspondente e,
#   4. A mensagem "APROVADO" ou "Reprovado" de acordo com a regra a seguir:
#      4.1. Se o conceito       for A, B ou C    exibir "APROVADO"
#      4.2. Senão se o conceito for D ou E       exibir "REPROVADO"
#---------------------------------------------------------------------------------------------------------------

nota1 = float(input('Digite sua nota do primeiro bimestre: '))
nota2 = float(input('Digite sua nota do segundo bimestre:  '))
nota3 = float(input('Digite sua nota do terceiro bimestre: '))
nota4 = float(input('Digite sua nota do quarto bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 9.0:
    con = 'A'
    mens = 'aprovado'
elif media >= 7.5:
    con = 'B'
    mens = 'Aprovado'
elif media >= 6.0:
    con = 'c'
    mens = 'Aprovado'
elif media >= 4.0:
    con = 'D'
    mens = 'Reprovado'
elif media >= 0:
    con = 'E'
    mens = 'Reprovado'

print(f'primeiro bimestre: {nota1}')
print(f'Segundo bimestre: {nota2}')
print(f'Terceiro bimestre: {nota3}')
print(f'Quarto bimestre: {nota4}')
print(f'Média final: {media:.2f}')
print(f'Conceito: {con}')
print(f'Você está: {mens}')