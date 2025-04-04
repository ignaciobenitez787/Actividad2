from funciones import check_username
user = input("Ingresa un nombre de usuario:")
if check_username(user):
    print("El nombre de usuario es válido.")
else:
    print("El nombre de usuario no cumple con los requisitos")