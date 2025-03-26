def check_username(username):
    """Takes an username and checks if it's valid"""
    alphanumeric = [char.isdigit() or char.isalpha() for char in username]
    return (len(username) >= 5) & (any(char.isdigit() for char in username)) & (any(char.isupper() for char in username)) & (all(alphanumeric))

user = input("Ingresa un nombre de usuario:")
if check_username(user):
    print("El nombre de usuario es válido.")
else:
    print("El nombre de usuario no cumple con los requisitos")