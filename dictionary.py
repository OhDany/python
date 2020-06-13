# Dictionary
dictionary = {
    'a': 1,
    'b': 2
}

print(dictionary['a'])

user = {
    'basket': [1, 2, 3],
    'greet': 'hello',
    'age': 20
}

user2 = dict(name='dany')

print(user.get('age', 55)) # default value
print(user2)

# clear
print('\n')
print('clear')
user.clear()
print(user)

# copy
user2 = user.copy()
print(user)
print(user2)

# pop
print(user.pop('age'))
print(user)

# update
print(user.update({'age': 33}))
print(user)