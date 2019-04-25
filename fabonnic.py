n = int(input("Enter a no. = "))

print("01")

x = 0
y = 1
i = 0
while (i<n-2):
	m = x+y
	print(m)
	x = y
	y = m
	i+=1

