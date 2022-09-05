velocidade_motor = int(input())
RPM = []
RPM = input().split()
Contador = 0
    
for i in range(1, velocidade_motor):
    if (int(RPM[i-1]) > int(RPM[i])):
        Contador = i + 1
        break
        
print(Contador)
