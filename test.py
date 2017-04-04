import unittest
from loanAmount import get_Loan_amount
class calculator(unittest.TestCase):
	#test that function works
	def test_it_works(self):
		self.assertEquals(get_Loan_amount(100000,12,12),112000)
	#test for negative values
	def test_months_not_greater_than_12(self):
		self.assertTrue(get_Loan_amount(-1,12,14),msg='Amount cannot have negative value')
	#test for string inputs
	def test_string_input_not_allowed(self):
		self.assertTrue(get_Loan_amount('amount',12,12),msg='only number inputs are allowed')
if __name__=='__main__':
	unittest.main()