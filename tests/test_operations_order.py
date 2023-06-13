import unittest
from operations_order import operations_order


class OperationsOrderTestCase(unittest.TestCase):
    def test_operations_order(self):
        # Test cases
        test_cases = [
            ([1, 2, 3, 4, 5, 10], 65, [((1*2)+(3*4))*5-10]),
            ([2, 3, 4, 5, 6, 7], 42, [2*3*7]),
            # Add more test cases here
        ]

        for numbers, target, expected_solution in test_cases:
            with self.subTest(numbers=numbers, target=target):
                solutions = operations_order(numbers, target)
                self.assertEqual(solutions[0], expected_solution)


if __name__ == '__main__':
    unittest.main()
