import math

ponto_1_plano = input().split(" ")
ponto_2_plano = input().split(" ")
x1,y1 = ponto_1_plano
x2,y2 = ponto_2_plano
distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))
print("%0.4f" %distancia)