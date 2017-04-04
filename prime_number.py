def generate_prime_numbers(n):
	'''
	This function generates prime numbers from 0 to n.
	:args:n 
	:return: primes-a list containing all prime numbers from 0 to n
	:Author: Meshack Mbuvi
	:Email:meshmbuvi@gmail.com
	:Phone:+254719800509

	'''
	primes=[]
	if isinstance(n, str):
		return 'input of type string not allowed'
	elif n<0:
		return 'only positive numbers are allowed'
	elif isinstance(n,float):
		return 'only whole numbers are allowed'
	elif isinstance(n, list):
		return 'inputs of type list is not allowed'
	elif isinstance(n, dict):
		return 'dictionary inputs not allowed'
	else:
		for number in range(n+1):
			if number>13:
				if not number%2==0 and not number%3==0 and not number%5==0 and not number%7==0 and not number%11==0 and not number%13==0:
					primes.append(number)
			else:
				if number>1 and number<=3:
					primes.append(number)
				elif not number%2==0 and not number%3==0 and number>1:
					primes.append(number)
		return primes
if __name__=='__main__':
	print generate_prime_numbers(15)
	print generate_prime_numbers('10')
	print generate_prime_numbers(200)