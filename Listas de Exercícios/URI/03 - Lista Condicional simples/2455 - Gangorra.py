p1,c1,p2,c2=input().split()
p1=int(p1)
c1=int(c1)
p2=int(p2)
c2=int(c2)

x=p1*c1
y=p2*c2


if(x<y):
    print('1')
else:
    if(x>y):
        print('-1')
    else:
        print('0')
