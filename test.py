import unittest
from calculator import calculate
from calculator import calc_string

class TestCalculator(unittest.TestCase):
	def test_dodawanie(self):
		r = calculate(1,2,'+')
		self.assertEqual(r,3)
	def test_odejmowanie(self):
		r = calculate(1,2,'-')
		self.assertEqual(r,-1)
	def test_mnozenie(self):
		r = calculate(1,2,'*')
		self.assertEqual(r,2)
#	def test_dzielenie(self):
#		r = calculate(1,2,'/')
#		self.assertEqual(r,0.5)

class TestStringCalculator(unittest.TestCase):
	def test_string_dodawanie(self):
		r = calc_string('a','b','concat')
		self.assertEqual(r,'ab')
#	def test_string_mnozenie(self):
#		r = calc_string('a','3','mutliply')
#		self.assertEqual(r,'aaa')
