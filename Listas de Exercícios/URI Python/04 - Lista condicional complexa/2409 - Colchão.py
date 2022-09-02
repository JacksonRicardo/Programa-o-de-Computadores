A, B, C = map(int,input().split())
alt, larg = map(float,input().split())
if A<=alt and B<=larg or A<=larg and B<=alt or A<=alt and C<=larg or C<=alt and A<=larg or C<=alt and B<=larg or B<=alt and C<=larg:
    print("S")
else:
    print("N")
