a = int(input("Enter the 1st no. = "))
b = int(input("Enter the 2nd no. = "))

i=0
j=0
k = 0
if (a<b and a<100 and b<100):
	for i in range(a,b):
		#j = i+1
		#print(i," ",j)
		for j in range(2,i):
			#j = i+1
			#print(i," ",j)
			if(i%j == 0):
				k = 0
				break;
			else:
				j+=1
				k = 1
		if(k == 1):
			print("hlo",i)
		i+=1
else:
	print("invalid")
