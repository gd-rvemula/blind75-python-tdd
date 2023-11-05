from unittest import TestCase


class TestSolution(TestCase):
    def test_check_duplicate_in_array(self):
        # Given
        from python.src.ContainsDuplicate import Solution
        solution = Solution()
        # When
        result = solution.checkDuplicateInArray([1, 2, 3, 1])
        # Then
        self.assertEqual(result, True)
        # When
        result = solution.checkDuplicateInArray([1, 2, 3, 4])
        # Then
        self.assertEqual(result, False)
        # When
        result = solution.checkDuplicateInArray([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        # Then
        self.assertEqual(result, True)
        # When
        result = solution.checkDuplicateInArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        # Then
        self.assertEqual(result, False)
        self.fail()
