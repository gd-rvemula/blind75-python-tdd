from unittest import TestCase

class TestProductOfArrayExceptSelf(unittest.TestCase):

    def test_empty_array(self):
        # Given: an empty array
        nums = []
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an empty array
        self.assertEqual(result, [])

    def test_single_element_array(self):
        # Given: an array with one element
        nums = [1]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with one element, 1
        self.assertEqual(result, [1])

    def test_two_elements_array(self):
        # Given: an array with two elements
        nums = [1, 2]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with the products except self
        self.assertEqual(result, [2, 1])

    def test_multiple_elements_array(self):
        # Given: an array with multiple elements
        nums = [1, 2, 3, 4]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with the products except self
        self.assertEqual(result, [24, 12, 8, 6])

    def test_array_with_zero(self):
        # Given: an array with one zero
        nums = [0, 1, 2, 3, 4]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with the products except self, considering zero
        self.assertEqual(result, [24, 0, 0, 0, 0])

    def test_array_with_multiple_zeros(self):
        # Given: an array with more than one zero
        nums = [0, 1, 2, 0, 4]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with all elements as zero
        self.assertEqual(result, [0, 0, 0, 0, 0])

    def test_array_with_negative_numbers(self):
        # Given: an array with negative numbers
        nums = [-1, -2, -3, -4]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with the products except self
        self.assertEqual(result, [-24, -12, -8, -6])

    def test_large_numbers_array(self):
        # Given: an array with large numbers
        nums = [100000, 200000, 300000, 400000]
        # When: product_of_array_except_self is called
        result = product_of_array_except_self(nums)
        # Then: the result should be an array with the products except self
        expected_result = [24000000000000, 12000000000000, 8000000000000, 6000000000000]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()