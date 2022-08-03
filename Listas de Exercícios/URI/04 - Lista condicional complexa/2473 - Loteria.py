a,b,c,d,e,f=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
g,h,i,j,k,l=input().split()
g=int(g)
h=int(h)
i=int(i)
j=int(j)
k=int(k)
l=int(l)

if(a==g or a==h or a==i or a==j or a==k or a==l):
  a=1
else:
  a=0
  
if(b==g or b==h or b==i or b==j or b==k or b==l):
  b=1
else:
  b=0
  
if(c==g or c==h or c==i or c==j or c==k or c==l):
  c=1
else:
  c=0
  
if(d==g or d==h or d==i or d==j or d==k or d==l):
  d=1
else:
  d=0
  
if(e==g or e==h or e==i or e==j or e==k or e==l):
  e=1
else:
  e=0
  
if(f==g or f==h or f==i or f==j or f==k or f==l):
  f=1
else:
  f=0

soma=a+b+c+d+e+f

if(soma==3):
  print("terno")
elif (soma==4):
  print("quadra")
elif(soma==5):
  print("quina")
elif(soma==6):
  print("sena")
else:
  print("azar")