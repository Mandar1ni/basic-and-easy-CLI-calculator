continueorleave = input('\n\nType "start" to continue or "exit" to leave, without quotation marks\n\n --> ')
flag = True if continueorleave == 'start' else False
while flag:
	select = int(input("""\nType what kind of operation you would like to do\n
	0 for Addition
	1 for Subtraction
	2 for Multiplication
	3 for Division
	4 for Modulo
	5 for Floor_Division
	6 for Exponentiation\n\n--> """))
	print('\n\nEnter x and y below\n')
	x, y = [int(input('--> ')) for _ in range(2)]
	def Addition ():
		return x + y
	def Subtraction():
		return x - y
	def Multiplication():
		return x * y
	def Exponentiation():
		return x ** y
	def Division():
		return x / y
	def Floor_Division():
		return x // y
	def Modulo():
		return x % y
	choosen_dict = {0: Addition(),
	1: Subtraction(),
	2: Multiplication(),
	3: Division(),
	4: Modulo(),
	5: Floor_Division(),
	6: Exponentiation(),}
	print(f'\n\nresult --> {choosen_dict[select]}')
	continueorleave = input('\n\nType "start" to continue or "exit" to leave\n\n--> ')
	flag = True if continueorleave == 'start' else False
