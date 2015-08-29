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
		print ("0")
	elif n == 2:
		print ("0    1")
	else:
		listholder.append(0)
		listholder.append(1)
		for i in range(n-1):
			a,b = b,a+b
			listholder.append(a)
		
		#for i in range(0, len(listholder), 5):
			#dontuncomment#print(listholder[i:i + 5])
			#s = "".join(str(listholder[i:i + 5])).replace(",", "     ").replace("[","").replace("]","")
			#print (s)
			
		for a,b,c,d,e in zip(listholder[::5],listholder[1::5],listholder[2::5],listholder[3::5],listholder[4::5]):
			print ('{:<20}{:<20}{:<20}{:<20}{:<}'.format(a,b,c,d,e))
		return a
	
number = input('What is your number? ')
fib(int(number))
#fib(20)
