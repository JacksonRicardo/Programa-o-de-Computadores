while True:
  h1, m1, h2, m2 = input().split()
  h1=int(h1)
  m1=int(m1)
  h2=int(h2)
  m2=int(m2)

  if (h1+m1+h2+m2)==0:
    break
  
  horaIn = 0
  horaF =0

  if h1 == 0:
    horaIn = 24*60 + m1
  else:
    horaIn = h1*60 + m1
  if h2 == 0:
    horaF = 24*60 + m2
  else:
    horaF = h2*60 + m2
  
  if horaF > horaIn:
    print(horaF - horaIn)
  else:
    print(24*60 - (horaIn - horaF))
