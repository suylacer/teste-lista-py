from collections import defaultdict

lista = [2, 5, 9, 1, 6, 7, 8, 3, 5, 7, 12, 1, 12]
lista.sort()
print(f'Numeros em ordem crescente e posição ocupada:')
keys = defaultdict(list);

for key, value in enumerate(lista):
    keys[value].append(key)

for value in keys:
    if len(keys[value]) > 1:
        print(value, keys[value])

lista = [2, 5, 9, 1, 6, 7, 8, 3, 5, 7, 12, 1, 12]
lista.sort(reverse=True)
print(f'Numeros em ordem decrescente e posição ocupada:')
keys = defaultdict(list);

for key, value in enumerate(lista):
    keys[value].append(key)

for value in keys:
    if len(keys[value]) > 1:
        print(value, keys[value])