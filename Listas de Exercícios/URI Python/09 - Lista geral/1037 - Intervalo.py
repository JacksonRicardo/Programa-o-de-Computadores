numero = float(input())

if numero >= 0 and numero <= 25:
    print ("Intervalo [0,25]", end="\n")
elif numero > 25 and numero <= 50:
    print ("Intervalo (25,50]", end="\n")
elif numero > 50 and numero <= 75:
    print ("Intervalo (50,75]", end="\n")
elif numero > 75 and numero <= 100:
    print ("Intervalo (75,100]", end="\n")
else:
    print ("Fora de intervalo", end="\n")