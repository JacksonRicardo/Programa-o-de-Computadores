A, B, C, D = input().split()
H1, M1 = A.split(':')
H2, M2 = B.split(':')
H3, M3 = C.split(':')
H4, M4 = D.split(':')
H1, M1, H2, M2, H3, M3, H4, M4 = [int(H1), int(M1), int(H2), int(M2), int(H3), int(M3), int(H4), int(M4)]
m1, m2, m3, m4 = [(H1*60)+M1, (H2*60)+M2, (H3*60)+M3, (H4*60)+M4]

if(m1>m2):
	d1 = (1440-m1)+m2
else:
	d1 = (m2-m1)

if(m3>m4):
	d2 = (1440-m3)+m4
else:
	d2 = m4-m3

if(((d1+d2)/2)>720):
	flight_Hours = ((d1+d2)/2)-720
	fuse_Difference = (d1-flight_Hours)
	if(fuse_Difference>720):
		fuse_Difference = fuse_Difference-1440

else:
	flight_Hours = (d1+d2)/2
	fuse_Difference = (d1-flight_Hours)

print(str(int(flight_Hours))+" "+str(int(fuse_Difference/60)))
