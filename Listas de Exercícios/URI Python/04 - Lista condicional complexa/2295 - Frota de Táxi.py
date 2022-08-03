A,G,RA,RG=input().split()
A=float(A)
G=float(G)
RA=float(RA)
RG=float(RG)

PA=RA/A
PG=RG/G

if(PG<PA): 
	print("A")
if(PA<PG or PA==PG):
	print("G")