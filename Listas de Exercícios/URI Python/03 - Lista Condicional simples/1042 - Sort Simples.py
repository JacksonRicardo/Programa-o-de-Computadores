number = input().split(' ')
n1, n2, n3 = number
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
if n1<=n2 and n2<=n3:
    menor = n1
    meio = n2
    maior = n3
elif n1<=n3 and n3<=n2:
    menor = n1
    meio = n3
    maior = n2
elif n2<=n1 and n1<=n3:
    menor = n2
    meio = n1
    maior = n3
elif n2<=n3 and n3<=n1:
    menor = n2
    meio = n3
    maior = n1
elif n3<=n1 and n1<=n2:
    menor = n3
    meio = n1
    maior = n2
elif n3<=n2 and n2<=n1:
    menor = n3
    meio = n2
    maior = n1
print('%d' %menor)
print('%d' %meio)
print('%d' %maior)
print('')
print('%d' %n1)
print('%d' %n2)
print('%d' %n3)
