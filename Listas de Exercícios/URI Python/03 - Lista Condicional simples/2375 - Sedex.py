n = int(input()) 
entrada = input() 
a, l, p = [int(numero) for numero in entrada.split(" ")] 
if ((a < n) or (l < n) or (p < n)): 
    print("N") 
else: 
    print("S")
