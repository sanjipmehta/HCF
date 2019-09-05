n=input("Enter the string:")
num=int(input("Enter the size you want to split the string:"))
i=0
m=num

while i<=len(n)+1 :
	print(n[i:m])
	i=m
	
	m=num+i