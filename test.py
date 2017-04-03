import unittest
from loanAmount import get_Loan_amount
class calculator(unittest.TestCase):
	def test_it_works(self):
		self.assertEquals(get_Loan_amount(100000,12,12),112000)
	def test_months_not_greater_than_12(self):
		self.assertTrue(get_Loan_amount(-1,12,14),'Amount cannot be negative')
		
if __name__=='__main__':
	unittest.main()