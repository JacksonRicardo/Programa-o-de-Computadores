valor = 0
acumulador = 0
contador = 0

for i in range (1, 7):
    valor = float (input())

    if (valor > 0):
        acumulador = acumulador + valor
        contador = contador + 1
        media = (acumulador / contador)
        media_str="{:.1f}".format(media)
 
print(contador, "valores positivos")  
print(media_str)
