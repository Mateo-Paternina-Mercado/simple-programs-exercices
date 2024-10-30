#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

# Pedimos al usuario que ingrese un número de tres dígitos
numero = input("Enter a three-digit number: ")

# Invertimos el número
numero_invertido = numero[2] + numero[1] + numero[0]

# Mostramos el resultado
print(numero_invertido)
