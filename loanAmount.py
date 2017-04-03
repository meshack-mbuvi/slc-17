def get_Loan_amount(amount,time,rate):
	'''
	This function calculates the accumulated loan amount
	:params
	:args:amount,time,rate
	:outputs:amount

	'''
	if time<0:
		return 'Invalid time'
	elif amount<0:
		return 'Amount cannot be negative'
	else:
		Interest=(amount*rate/100*time/12)#calculate the accumulated interest
		A=amount+Interest
		return A
print get_Loan_amount(100000,12,12)