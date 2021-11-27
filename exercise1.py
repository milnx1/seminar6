try:
	file1=open('mailbox.txt')
except:
	print("File cannot be opened or doesn't exist")
	exit()

file2=open("output.txt", "w")
lines=file1.readlines()
count=0
count2=0
list1=[]
for line in lines:
	count+=line.count("@")
	count2+=1
	if "@" in line:
		print(count2)
		list1.append(count2)

for item in list1:
	file2.write(str(item))
	file2.write("\n")

print(count)
