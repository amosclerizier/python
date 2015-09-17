# COT 4930  Python Programming
# name: 
# id  : 
# lab : 02


def fib(n):
	listholder = []
	a,b = 1,1
	if n < 1 :
		print("Number has to be greater than 0!")
	elif n == 1 :
		listholder.append(0)
	elif n == 2:
		listholder.append(0)
		listholder.append(1)
	else:
		listholder.append(0)
		listholder.append(1)
		for i in range(n-2):
			a,b = b,a+b
			#a = b
			#b = a+b
			listholder.append(a)
		
	for i in range(0, len(listholder), 6):
		s = "".join(str(listholder[i:i + 6])).replace(",", "     ").replace("[","").replace("]","")
		print (s)


number = input('What is your number? ')
fib(int(number))
