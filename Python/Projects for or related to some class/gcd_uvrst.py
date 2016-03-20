def gcd(A,B):
	a=A
	b=B
	r=B
	u,v,s,t = 1,0,0,1
	while b!=0:
		print(a," = ",u, "*",A," + ", v, "*",B)
		print(b," = ",s, "*",A," + ", t, "*",B)
		r= a%b
		q= a//b
		a= b
		b= r
		
		u_s,v_s = u,v
		u,v = s,t
		s,t = u_s-q*s, v_s-q*t
	print(a," = ",u, "*",A," + ", v, "*",B)
	
	return a
		
	






