x = int(input("Enter a no. = "))
i = x
k = 0
r = 0
while (x>0):
	r = r * 10
	r = r + x%10
	x = int(x/10)
	
print(r)

if (i == r):
	print("palin")
else:
	print("not palin")
