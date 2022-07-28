a,b=input().split()
a=int(a)
b=int(b)
if((a%b==0) | (b%a==0)):
    print("Sao Multiplos")
    
else:
    print("Nao sao Multiplos")
