def find_prime_factors(inp_num):
	ls_primes = []
	i = 2
	while i in range(2,inp_num+1):
		while inp_num % i == 0:
			ls_primes.append(i)
			inp_num //= i
			break
		i += 1
		
		 
	print(ls_primes)


inp_num = int(input("Enter the number: "))
find_prime_factors(inp_num)
