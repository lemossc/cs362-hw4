import unittest
import list_average


class TestListAverage(unittest.TestCase):
    def test_zero_elements(self):
        result = list_average.list_average([])
        self.assertEqual(result, 0)

    def test_type_error(self):
        # String elements
        result = list_average.list_average(["word1", "word2"])
        self.assertEqual(result, None)
        result = list_average.list_average([0, 1, 2, 3, 4, "oops"])
        self.assertEqual(result, None)
        # Non-list
        result = list_average.list_average(20)
        self.assertEqual(result, None)
        result = list_average.list_average("12345")
        self.assertEqual(result, None)
        # Complex number
        result = list_average.list_average([2, complex(5, 3)])
        self.assertEqual(result, None)

    def test_normal_use(self):
        # Integers
        result = list_average.list_average([0, 1, 2, 3, 4, 5])
        self.assertEqual(result, 2.5)
        # Float
        result = list_average.list_average([2.5, 8.10, 9.7])
        self.assertEqual(result, 6.766666666666666)
        # Tuple
        result = list_average.list_average((0, 1, 2, 3, 4, 5))
        self.assertEqual(result, 2.5)


if __name__ == "__main__":
    unittest.main()
