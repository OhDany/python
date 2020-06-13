#Data Types
print(type(2))

print(type(2 + 4))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(2 ** 3) # Potencia
print(6 // 4)
print(6 % 4)

print(' ')

#Math function
print('Math functions')
print(round(3.6))
print(abs(-7))

print(' ')
# bin()
print('bin()')
print(bin(5))
print(int('0b101', 2))

print('\n')
variable = 4
variable += 1

print(variable)

print('\n')
print('start:stop:stepover')

dato = '01234567'

print(dato[0:8:2])
print(dato[::2])
print(dato[::-1]) #reverse

# What is my age
print('\n')
birth_ege = input('What year were you born: ')

age = 2019 - int(birth_ege)
print('\n')
print(f'My age is: {age}')

username = input("Capture su nombre de usaurio: ")
password = input("Ingrese su password: ")

password_legth = len(password)

hidden_password = '*' * password_legth

print(f'{username}, su password {hidden_password}, es {password_legth} letras de largo')
