base = float    (input("cual es la base?: "))
altura = float(input("cual es la altura?: "))

area = (base * altura)
print(f"el area es {area}")

if base == altura:
    print("es un cuadrado")
else:
    print("es un rectangulo")