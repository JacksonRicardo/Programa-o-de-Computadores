N=int(input())
LA,LB=map(int,input().split())
SA,SB=map(int,input().split())
if ((N>=LA and N<=LB) and (N>=SA and N<=SB)):
    print("possivel")
else:
    print("impossivel")
