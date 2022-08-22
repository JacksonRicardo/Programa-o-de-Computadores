primeira_carta, segunda_carta, terceira_carta, quarta_carta, quinta_carta = map(int, (input().split()))
if (primeira_carta<segunda_carta) and (segunda_carta<terceira_carta) and (terceira_carta<quarta_carta) and (quarta_carta<quinta_carta):
  print("C")
elif (primeira_carta>segunda_carta) and (segunda_carta>terceira_carta) and (terceira_carta>quarta_carta) and (quarta_carta>quinta_carta):
  print("D")
else:
  print("N")