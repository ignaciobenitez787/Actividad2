def check_username(username):
    """Takes a username and checks if it's valid"""
    return (len(username) >= 5) and (any(char.isdigit() for char in username)) and (any(char.isupper() for char in username)) and (all(char.isalnum() for char in username))

user = input("Ingresa un nombre de usuario:")
if check_username(user):
    print("El nombre de usuario es válido.")
else:
    print("El nombre de usuario no cumple con los requisitos")