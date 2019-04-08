x = input("Name = ")
fi = "file1.txt"
file = open(fi ,'w')
file.write(x)
file.close()

file = open(fi , 'r')
file3 = file.read()

#print(file3)
file.close()

xd = "file4.txt"
file = open(xd,'w')
file.write(file3)
file.close()
