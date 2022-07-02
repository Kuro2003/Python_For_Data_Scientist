# method 1: 
with open('data.txt') as file:
	f = file.read()
	f = f.replace('Python','Cuong')
	print(f)