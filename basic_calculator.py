print("\n Basic Calculator\n-----------------\n")
print("+ Addition \n- Subtraction \n* Multiplication \n/ Division \ne Exit\n")

while True:
	op_choice = input("Enter the operator: ")
	if op_choice == 'e':
		print("End of operations")
		break

	num1 = float(input("Enter the first number: "))
	num2 = float(input("Enter the second number: "))
	if str(num1).replace('.','',1).isdigit() and str(num2).replace('.','',1).isdigit():
		
		if op_choice == '+':
			sum_num = num1 + num2
			print(sum_num,"\n")
	
		elif op_choice == '-':
			sub_num = num1 - num2
			print(sub_num,"\n")

		elif op_choice == '*':
			mul_num = num1 * num2
			print(mul_num,"\n")

		elif op_choice == '/':
			div_num = num1 / num2
			print(div_num,"\n")

	else:
		print("Wrong input\n Enter again")
