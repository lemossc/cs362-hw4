import unittest
import cube


class TestCalculator(unittest.TestCase):
    # Side length must be float or int
    def test_invalid_input(self):
        result = cube.volume("length")
        self.assertEqual(result, None)
        result = cube.volume(complex(5, 3))
        self.assertEqual(result, None)

    # Side lengths <= 0 don't make physical sense
    def test_zero(self):
        result = cube.volume(0)
        self.assertEqual(result, None)

    def test_negative(self):
        result = cube.volume(-2)
        self.assertEqual(result, None)

    def test_float(self):
        result = cube.volume(2.5)
        self.assertEqual(result, 15.625)

    def test_int(self):
        result = cube.volume(7)
        self.assertEqual(result, 343)


if __name__ == "__main__":
    unittest.main()
