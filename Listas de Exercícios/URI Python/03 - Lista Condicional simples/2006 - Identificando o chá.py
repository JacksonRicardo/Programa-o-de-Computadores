t=int(input())
a, b, c, d, e=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)

contador=0
if(t==a):
  contador+=1
if(t==b):
  contador+=1
if(t==c):
  contador+=1
if(t==d): 
  contador+=1 
if(t==e):
  contador+=1

print(contador)
