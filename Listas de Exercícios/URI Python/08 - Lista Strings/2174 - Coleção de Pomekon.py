z=int(input())
y=[]
w=151
for i in range(0,z):
    x=input().upper()
    if x not in y:
        w-=1
    y.append(x)
print("Falta(m)",w,"pomekon(s).")
