x=[]

while(1):
 try:
   maior=0
   x.clear()
   n=int(input())
   l=list(map(int,input().split()))
 
   for i in range(0,n):
     x.insert(i,l[i])

   maior=max(x)
   if(maior<10):
     print("1")
   elif((maior>10)and(maior<20)):
     print("2")
   else:
     print("3")
  
 except EOFError:
   break
