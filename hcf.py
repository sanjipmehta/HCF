l=[]
l2=[]
z=[]
def factor1(num):
	for x in range(1,num+1):
		if num % x==0:
			l.append(x)
			

def factor2(num2):
	for y in range(1,num2+1):
		if num2 % y==0:
			l2.append(y)
			

x1=int(input("Enter the first number:"))
factor1(x1)
x2=int(input("Enter the second number:"))
factor2(x2)

for i in l:
	if i in l2:
		z.append(i)
		z.sort()

print("List of common element are:",z)
print("The number of common element are:",len(z))
print("The Highest Common factor is:",z[-1])