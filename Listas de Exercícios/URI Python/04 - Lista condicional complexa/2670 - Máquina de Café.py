A1=int(input())
A2=int(input())
A3=int(input())

b1=(A2*2)+(A3*4)
b2=(A1*2)+(A3*2)
b3=(A1*4)+(A2*2)

if(b1<=b2 and b1<=b3):
    print(b1)
elif(b2<b1 and b2<=b3):
    print(b2)
elif(b3<b1 and b3<=b2):
    print(b3)