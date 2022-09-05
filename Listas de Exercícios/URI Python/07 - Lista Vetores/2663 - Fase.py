Competidores = int(input())
Minimo_competidores = int(input())
Pontuacao_competidor = [int(input()) for x in range(Competidores)]
Pontuacao_competidor.sort(reverse=True)
total = Minimo_competidores
while total < Competidores and Pontuacao_competidor[total] == Pontuacao_competidor[Minimo_competidores-1]:
    total += 1
