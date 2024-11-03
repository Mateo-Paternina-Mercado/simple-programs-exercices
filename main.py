import math
TO = float(input("Temperatura original del huevo\n")) #Temperatura original del huevo
TW = 100 #Temperatura del agua para alcanzar la ebullición
TY = 70 #Temperatura de la yema para coagularse 
M = 67 #Masa del huevo 47 = pequeño y 67 grande
P = 1.038 #Constante de la formula = densidad del huevo
C = 3.7 #Constante de la formula = capacidad calorífica del huevo
K = 5.4 * math.pow(10, -3) #Constante de la formula = conductividad térmica del huevo
dividendo = math.pow(M, (2/3)) * (C * (math.pow(P, (1/3))))
divisor = (K * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
resultado = dividendo / divisor

resultado2 = math.log(0.76 * ((TO - TW) / (TY - TW)))

segundos = resultado * resultado2
#minutos = round(segundos/60)

print(f"El tiempo máxima para prepararlo a la copa {segundos} segundos")
#print(f"El tiempo máxima para prepararlo a la copa {minutos} minutos")