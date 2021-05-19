# Triangulos
base= float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

area = (base*altura)/2
area = round(area,2)
print("El área del triángulo es: " + str(area) + " área")

lado_a = float(input("Ingresa otro lado del triángulo al que llamaremos a: "))
lado_b = float(input("Ingresa el otro lado al que llamaremos b: "))

if base == lado_a and base==lado_b:
    print("Tu triángulo es equilatero")

elif base==lado_a or base==lado_b or lado_a==lado_b:
    print("Tu triángulo es isósceles")

else:
    print("Tu triángulo es escaleno")