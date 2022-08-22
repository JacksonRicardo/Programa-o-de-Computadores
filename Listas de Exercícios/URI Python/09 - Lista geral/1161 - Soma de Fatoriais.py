def fatorial(x):
  f=1 
  for i in range(1,x+1):
    f = f*i
  return f

def soma_fatorial(m,n):
  a = m+n
  return a

while True:
  try:
    m, n= map(int,input().split()) 
    fatorialA = fatorial(m)
    fatorialB = fatorial(n)
    soma = soma_fatorial(fatorialA,fatorialB)
    print(soma)
  except:
    break