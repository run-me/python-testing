import unittest
from testable_functions import sum_


class TestSum(unittest.TestCase):
	def test_list_int(self):
		data = [1, 2, 3]
		result = sum(data)
		self.assertEquals(result, 6)


if __name__ == "__main__":
	unittest.main()
