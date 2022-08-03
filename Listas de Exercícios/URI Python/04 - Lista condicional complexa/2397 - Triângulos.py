a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if(a<b+c and b<a+c and c<b+a):
	if(a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
		print("r")
	elif(a**2>b**2+c**2 or b**2>a**2+c**2 or c**2>a**2+b**2):
		print("o")
	elif(a**2<b**2+c**2 or b**2<a**2+c**2 or c**2<a**2+b**2):
		print("a")
else:
	print("n")