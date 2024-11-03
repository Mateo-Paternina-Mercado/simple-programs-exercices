#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19

def obtener_parte_decimal():
    # Solicitar un número real al usuario
    numero = float(input("Enter a number: "))
    
    # Obtener la parte entera
    parte_entera = int(numero)
    
    # Calcular la parte decimal
    parte_decimal = abs(numero - parte_entera)
    
    # Mostrar la parte decimal con dos decimales
    print(f"{parte_decimal:.2f}")

# Ejecutar el programa
obtener_parte_decimal()

