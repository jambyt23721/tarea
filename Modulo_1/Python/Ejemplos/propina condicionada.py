total_cuenta = float(input("Ingrese el total de la cuenta: "))
propina = 0
if total_cuenta < 50:
    propina = total_cuenta * 0.10
    print(f"la propina es: {propina}")

else:
    propina = total_cuenta * 0.15
    print(f"la propina es: {propina}")
