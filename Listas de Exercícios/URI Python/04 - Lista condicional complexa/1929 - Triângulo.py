a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if ((abs(a-b)<c<a+b) and (abs(a-c)<b<a+c)  and (abs(b-c)<a<b+c)):
    print("S")
elif((abs(a-d)<c<a+d) and (abs(a-c)<d<a+c)  and (abs(d-c)<a<d+c)):
    print("S")
elif((abs(a-b)<d<a+b) and (abs(a-d)<b<a+d)  and (abs(b-d)<a<b+d)):
    print("S")
elif((abs(d-b)<c<d+b) and (abs(d-c)<b<d+c)  and (abs(b-c)<d<b+c)):
    print("S")
else:
    print("N")