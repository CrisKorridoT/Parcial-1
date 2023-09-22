n1 = None
n2 = None
n3 = None

while n1 is None:
    valor = float(input("Ingrese el primer número (mayor que 0 y menor que 259): "))
    if valor < 0 or valor > 259:
        print("Error: el valor ingresado no cumple con las condiciones.")
    else:
        n1 = valor
while n2 is None:
    valor = float(input("Ingrese el segundo número (mayor que 0 y menor que 259): "))
    if valor < 0 or valor > 259:
        print("Error: el valor ingresado no cumple con las condiciones.")
    else:
        n2 = valor

while n3 is None:
    valor = float(input("Ingrese el tercer número (mayor que 0 y menor que 259): "))
    if valor < 0 or valor > 259:
        print("Error: el valor ingresado no cumple con las condiciones.")
    else:
        n3 = valor

promedio = (n1 + n2 + n3) / 3

print("El promedio es:", round(promedio, 2))

numero_actual = promedio
secuencia = str(numero_actual)

while numero_actual != 1:
    if numero_actual % 2 == 0:
        numero_actual = numero_actual / 2
    else:
        numero_actual = (numero_actual * 3) + 1
    
    secuencia += " -> " + str(numero_actual)

print("La secuencia de Collatz para el promedio es:", secuencia)