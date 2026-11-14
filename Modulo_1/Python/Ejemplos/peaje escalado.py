horas = int(input("Ingrese la cantidad de horas Estacionado: "))

if horas >= 5:
    tarifa = 10
else:
    tarifa = horas * 2

print(f"El total a pagar es: {tarifa}")