filename = ['cats.txt','dogs.txt']
try:
	for file in filename:
		with open(file,'r') as f:
			files = f.read()
			print(files)
except:
	print("File Not Found !!!")