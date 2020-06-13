# Tuple
tupla = (1, 2, 3, 4, 5, 1, 1)

print(tupla[2])
print(5 in tupla)

user = {
    (1, 2, 3): [1, 2, 3],
    'great': 'hello',
    'age': 20
}

print(user[(1, 2, 3)])

new_tipla = tupla[1:4]

print(new_tipla)

# count
print('\n')
print('cont')
print(tupla.count(1))

# index
print('\n')
print('index')
print(tupla.index(5))

print(len(tupla))