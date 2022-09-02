consumo=int(input())
if(consumo<=10):
  print("7")
if(consumo>=11 and consumo<=30):
  print((consumo-10)*1+7)
elif(consumo>=31 and consumo<=100):
  print((consumo-30)*2+27)
if(consumo>=101):
  print((consumo-100)*5+167)
