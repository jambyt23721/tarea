nota1 = int(input("Ingrese la primera nota (0-20): "))
nota2 = int(input("Ingrese la segunda nota (0-20): "))
nota3 = int(input("Ingrese la tercera nota (0-20): "))

promedio = (nota1 + nota2 + nota3) / 3

print(f"El promedio es: {promedio:}")
if promedio >= 10:
    print("Aprobado")
else:
    print("Reprobado")