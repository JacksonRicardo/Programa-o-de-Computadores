teste = int(input())
while teste > 0:
    teste -= 1
    carneiros = int(input())
    sequencias_carneiros = [int(x) for x in input().split()]
    print(len(set(sequencias_carneiros)))
