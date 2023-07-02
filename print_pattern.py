def print_pattern(inp_num):
	i = 1
	j = 1
	while i <= inp_num:
		while j < i+1:
			print(j,end=" ")
			j += 1
		j=1
		i += 1
		print(" ")
		
		

inp_num = int(input("Input number is: "))
print_pattern(inp_num)
