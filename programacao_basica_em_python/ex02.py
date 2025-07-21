#01
idade = int(input('Qual a sua idade: '))
if idade < 0:
    print('Idade inválida')
elif idade <= 12:
    print('Criança')
elif idade <= 17:
        print('Adolescente')
elif idade >= 18:
    print('Adulto')

#02
M1 = float(input('Nota 01: '))
M2 = float(input('Nota 02: '))
M3 = float(input('Nota 03: '))
media = (M1 + M2 + M3) / 3

if media <= 4:
    print('Reprovado')
elif media <= 6:
    print('Exame')
    notaex = float(input('Nota do exame: '))
    if notaex > 6:
        print('Aprovado')
    else:
        print('Reprovado')
else:
    print('Aprovado')