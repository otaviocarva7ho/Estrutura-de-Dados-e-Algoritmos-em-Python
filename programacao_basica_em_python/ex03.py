# 01
# For
nota = soma = media = 0
for i in range(1, 6):
    nota = float(input('Informe a nota do aluno: '))
    soma += nota
print(soma)
media = soma / 5
print(media)

# while
cont = nota = soma = media = 0
while cont < 5:
    nota = float(input('Informe a nota do aluno: '))
    soma += nota
    cont += 1
print(soma)
media = soma / 5
print(media)

# 02
# For
for i in range(1, 11):
    print(f'3 x {i} = {3*i}')

# While
cont = 1
while cont < 11:
    print(f'3 x {cont} = {3*cont}')
    cont += 1