n = int(input("Enter a no. = "))
i = n
j = 0
fact = 1

def facto(x):
	fact*=x
	x-=1
	return x

while ( i >= 1):
	i = facto(i)
print("Fact = ", fact) 
