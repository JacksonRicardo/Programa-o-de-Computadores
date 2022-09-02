N1,N2=map(int,input().split())
if(N2>=0 and N2<=2 ):
	print("nova")
elif(N2>=3 and N2<=96):
	if(N2>N1):
		print("crescente")
	else:
		print("minguante")
elif(N2>=97 and N2<= 100):
	print("cheia")
