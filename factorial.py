def find_factorial(inp_num):
	if inp_num == 0:
		pass
	i = 1
	num_fact = 1
	while i<= inp_num:
		num_fact *= i
		i += 1
	print(num_fact)	



inp_num = int(input("Enter the number: "))
find_factorial(inp_num)

