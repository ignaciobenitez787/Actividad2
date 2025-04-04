import string
rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""
# Se separa las reglas en una lista
rules = rules.splitlines()
key = input("Ingrese una palabra clave:")
key = key.lower()
# Cada regla se separa en palabras 
for rule in rules:
    for word in rule.split():
        word = word.lower()
        if word.startswith(key.lower()) & word.endswith((key,", ", ".")):
            print(rule)
            break
        