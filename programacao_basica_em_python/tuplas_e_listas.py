#Tuplas
tupla = ('Homo sapiens', 'Canis familiaris', 'Felis catus')
print(tupla)
print(tupla[0])
print(tupla.index('Canis familiaris'))
for elemento in tupla:
    print(elemento)

#Listas
l1 = ['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']
l3 = l1 + l2
print(l3)
l2_2 = l2 * 2
print(l2_2)
print(l1[0])
print(l1[0:2])
print(l1.append('Gorila gorila'))
print(l1)
print(l1.remove('Felis catus'))
print(l1)
del(l1)
print(l1)
for item in l2_2:
    print(item)
