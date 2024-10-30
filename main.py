#Escriba un programa que convierta de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros.

#Ingrese longitud: 45
#45 cm = 17.7165 in
#Ingrese longitud: 13
#13 cm = 5.1181 in

# Pedimos al usuario que ingrese la longitud en centímetros
entrada = input("Enter length in centimeters: ")

# Convertimos la entrada a un número
centimetros = float(entrada)

# Calculamos las pulgadas (1 pulgada = 2.54 centímetros)
pulgadas = centimetros / 2.54

# Mostramos el resultado
print(centimetros, "cm =", pulgadas, "in")
