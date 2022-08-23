x = int(input())
Horas = x // 3600
resto = x % 3600
Minutos = resto // 60
resto = resto % 60
Segundos = resto // 1
print('%d:%d:%d' %(Horas, Minutos, Segundos))