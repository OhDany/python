username = input("Capture su nombre de usaurio: ")
password = input("Ingrese su password: ")

password_legth = len(password)

hidden_password = '*' * password_legth

print(f'{username}, su password {hidden_password}, es {password_legth} letras de largo')