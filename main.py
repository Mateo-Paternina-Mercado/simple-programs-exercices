#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6

def calcular_nueva_hora():
    # Solicitar la hora actual
    hora_actual = int(input("Current time (0-23): "))
    
    # Solicitar la cantidad de horas a sumar
    horas_a_sumar = int(input("Number of hours: "))
    
    # Calcular la nueva hora
    nueva_hora = (hora_actual + horas_a_sumar) % 24
    
    # Mostrar el resultado
    print(f"En {horas_a_sumar} hours, the clock will show {nueva_hora}.")

# Ejecutar el programa
calcular_nueva_hora()
