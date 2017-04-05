def prime(n):
	'''
	:Author: Mbuvi
    :http://mbuv.wordpress.com
    :Email: meshmbuvi@gmail.com
	'''
	primes=[]
	i=0
	number=0
	while(i<n):
		if isprime(number):
			primes.append(number)
			i+=1
			number+=1
		else:
			number+=1
		
	return primes
def isprime(number):
	no_is_prime=False
	'''
	This function check whether a number is prime and if true
	:input:number
	:return True or False depending on whether number is prime
	'''
	if number>13:
		if not number%2==0 and not number%3==0 and not number%5==0 and not number%7==0 and not number%11==0 and not number%13==0:
			no_is_prime=True
	else:
		if number>1 and number<=3:
			no_is_prime=True
		elif not number%2==0 and not number%3==0 and number>1:
			no_is_prime=True
	return no_is_prime
print prime(10)
print prime(14)