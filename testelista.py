from collections import defaultdict

list = [2, 5, 9, 1, 6, 7, 8, 3, 5, 7, 12, 1, 12]
list.sort()
print(f'Números ordenados:')
for i, elemento in enumerate(list):
    if elemento in list [i+1:]:
        print(f'Elemento repetido:{elemento}')


list = [2, 5, 9, 1, 6, 7, 8, 3, 5, 7, 12, 1, 12]
print(f'Números não ordenados:')
for i, elemento in enumerate(list):
    if elemento in list [i+1:]:
        print(f'Elemento repetido:{elemento}')

