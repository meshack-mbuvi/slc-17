def get_Loan_amount(amount,time,rate):
	'''
	This function calculates the accumulated loan amount over a period of time
	:params
	:args:amount,time,rate
	:outputs:amount

	'''
	#Allow only numbers
	if isinstance(amount,str) or isinstance(time,str) or isinstance(rate,str):
		return 'only number inputs are allowed'
	elif time<0:#test for negative time
		return 'Time cannot have negative value'
	elif amount<0:
		return 'Amount cannot be negative'
	else:
		Interest=(amount*rate/100*time/12)#calculate the accumulated interest
		A=amount+Interest
		return A
print get_Loan_amount(100000,12,12)