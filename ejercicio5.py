reaction = input("Ingrese su tiempo de reacción:")
if reaction.isdigit():
    reaction = int(reaction)
else:
    print("Tiempo de reacción no valido")
    exit(1)
if(reaction < 200):
    speed = "Rápido"
elif(reaction <= 500):
    speed = "Normal"
else:
    speed = "Lento"
print("Categoría:",speed)
