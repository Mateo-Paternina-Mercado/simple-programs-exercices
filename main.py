#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#                                        NC=(C1+C2+C3)3
#                                        NF=NC⋅0.7+NL⋅0.3
#Donde NC
# es el promedio de certámenes, NL
# el promedio de laboratorio y NF
# la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


def calcular_nota_necesaria():
    # Solicitar las notas al usuario
    certamen1 = float(input("Enter contest note 1: "))
    certamen2 = float(input("Enter contest note 2: "))
    nota_laboratorio = float(input("Enter laboratory note: "))
    
    # Definir la nota final mínima para aprobar
    nota_final_deseada = 60
    
    # Calcular la nota necesaria en el promedio de certámenes
    NF_laboratorio = nota_final_deseada - (nota_laboratorio * 0.3)
    NC_necesario = NF_laboratorio / 0.7
    
    # Calcular la nota necesaria en el certamen 3
    nota_certamen3_necesaria = (NC_necesario * 3) - certamen1 - certamen2
    
    # Mostrar el resultado
    print(f"Need note {nota_certamen3_necesaria:.2f} in the contest 3")

# Ejecutar el programa
calcular_nota_necesaria()