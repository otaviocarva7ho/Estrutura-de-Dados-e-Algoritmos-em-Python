#01
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print(f'A adição entre {n1} e {n2} é: {n1 + n2}')
print(f'A subtração entre {n1} e {n2} é: {n1 - n2}')
print(f'A multiplicação entre {n1} e {n2} é: {n1 * n2}')
print(f'A divisão entre {n1} e {n2} é: {n1 / n2}')

#02
tempo = float(input('Tempo gasto na viagem: '))
velocidade_media = float(input('Velocidade média: '))

distancia = tempo * velocidade_media
litros_usados = distancia / 12

print(f'A velocidade média usada foi de {velocidade_media}, tempo gasto de {tempo}, a distância percorrida foi de {distancia} e a quantidade de litros utilizada foi de {litros_usados}')