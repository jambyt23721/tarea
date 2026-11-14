celcius = float(input("Ingrese la temperatura en grados celcius: "))

fahrenheit = (celcius * 9/5) + 32
print(f"La temperatura en fahrenheit es: {fahrenheit}")

if fahrenheit < 50:
    print("Hace frio")

elif fahrenheit >= 50 and fahrenheit <= 80:
    print("Hace calor")
else:
    print("Hace mucho calor")