# unit test for MaximumSubarray problem

import unittest
class TestFindMaximumProductSubArray_test:

    def test_single_element(self):
        # Given: an array with a single element
        nums = [1]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be the single element itself as the max product subarray
        self.assertEqual(result, [1])

    def test_all_positive(self):
        # Given: an array with all positive numbers
        nums = [1, 2, 3, 4]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be the entire array as the max product subarray
        self.assertEqual(result, nums)

    def test_all_negative(self):
        # Given: an array with all negative numbers
        nums = [-1, -2, -3, -4]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be the subarray with the highest negative number if even count of negatives
        self.assertEqual(result, [-1])

    def test_mix_positive_negative(self):
        # Given: an array with a mix of positive and negative numbers
        nums = [2, 3, -2, 4]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be the subarray with the largest product
        self.assertEqual(result, [2, 3])

    def test_zero_in_array(self):
        # Given: an array with a zero breaking the continuity of product
        nums = [0, 2, 3, -2, 4]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be the subarray with the largest product after the zero
        self.assertEqual(result, [2, 3])

    def test_all_zeros(self):
        # Given: an array with all zeros
        nums = [0, 0, 0, 0]
        # When: max_subarray_product is called
        result = max_subarray_product(nums)
        # Then: the result should be a single zero
        self.assertEqual(result, [0])

if __name__ == '__main__':
    unittest.main()