import unittest
from prime_number import generate_prime_numbers
class prime_numbers(unittest.TestCase):
	#test for non number inputs
	def test_non_number_inputs(self):
		self.assertTrue(generate_prime_numbers('123'),'input of type string not allowed')
	#should not accept negative numbers
	def test_negative_numbers(self):
		self.assertEqual(generate_prime_numbers(-1),'only positive numbers are allowed')
	#should not accept lists
	def test_list_input(self):
		self.assertEqual(generate_prime_numbers([2]),'inputs of type list is not allowed')
	#should work on only whole numbers
	def test_non_whole_numbers(self):
		self.assertTrue(generate_prime_numbers(1.5),'only whole numbers are allowed')
	#should not accept dictionary inputs
	def test_dict_input(self):
		self.assertTrue(generate_prime_numbers({1:1}),'dictionary inputs not allowed')
	#test that function works correctly
	def test_it_works_correctly(self):
		self.assertEqual(generate_prime_numbers(10),[2,3,5,7])
		self.assertEqual(generate_prime_numbers(5),[2,3,5])
if __name__=='__main__':
	unittest.main()