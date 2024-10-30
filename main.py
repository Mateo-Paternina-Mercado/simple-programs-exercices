#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75

note1 = float(input("Enter the note value: "))
note2 = float(input("Enter the note value: "))
note3 = float(input("Enter the note value: "))
note4 = float(input("Enter the note value: "))

promedio = ((note1+note2+note3+note4)/4)

print(f"""{promedio} """)