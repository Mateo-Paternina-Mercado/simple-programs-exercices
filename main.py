#Escriba un programa que reciba como entrada el radio de un círculo y entregue como salida su perímetro y su área:

#Ingrese el radio: 5
#Perimetro: 31.4
#Área: 78.5

radio = float(input("Write the radio of the circle : "))
perimeter = 2 * (radio) * 3.1416
area = 3.1416 * (radio ** 2) 

print(f"the perimeter is : {perimeter :.2f}\nthe area is : {area :.2}")