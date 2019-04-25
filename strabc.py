a = input("Enter a string:")
b = input("Enter a char:")
i=0
m=0
x = len(a)
while (i<x):
	if(b == a[i]):
		m+=1
	i+=1

print(m)
