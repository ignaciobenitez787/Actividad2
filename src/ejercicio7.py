import string
import random
while True:
    username = input("Ingrese un nombre de usuario(Maximo 15 caracteres):")
    break
date = input("Ingrese la fecha en formato YYYY-DD-MM:")
if len(date) != 10 or not all(number.isdigit() for number in date.split('-')) or not (date[4]=='-' and date[-3]=='-') or int(date[5:7]) > 31 or int(date[8:]) > 12 :
    print("Fecha invalida")
    exit(1)
else:
    print("Fecha valida")       
date = date.split('-')
date = "".join(date)
random_code = random.choices(string.ascii_uppercase + string.digits, k=20-len(username))
random_code = "".join(random_code)
code = [username.upper(), date, random_code]
print("Código de descuento:", "-".join(code))                                                            