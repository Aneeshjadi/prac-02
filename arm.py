n=input ("enter any number")
m=int(n)
sum=0
while(m>0):
	r=m%10
	sum=sum+r**len(n)
	m=m//10
if(int(n)==sum):
	print("it is armsrng no")
else:
	print("not armstrng no")
	
	
	

