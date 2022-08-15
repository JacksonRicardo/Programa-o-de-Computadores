l=[0,20]
for i in range(0,20):
 n=int(input())
 l.append(n)
l.reverse()
for i in range(0,20):
    print("N[{}] = {}".format(i,l[i]))
