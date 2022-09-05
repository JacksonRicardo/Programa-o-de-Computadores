x=int(input())
aux=""
while(x>0):
    aux+=str(x%10)
    x=x//10
print(aux)
