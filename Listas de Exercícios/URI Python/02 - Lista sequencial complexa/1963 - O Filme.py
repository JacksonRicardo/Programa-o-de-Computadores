a,b=input().split()
a=float(a)
b=float(b)
c=b-a
print(str("{:.2f}".format((c*100)/a))+"%")
