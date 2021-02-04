import unittest
import full_name


class TestFullName(unittest.TestCase):
    def test_empty_string(self):
        result = full_name.get_full_name("", "Last")
        self.assertEqual(result, None)

    def test_type_error(self):
        result = full_name.get_full_name("First", 10)
        self.assertEqual(result, None)

    def test_normal_use(self):
        result = full_name.get_full_name("Christopher", "LeMoss")
        self.assertEqual(result, "Christopher LeMoss")


if __name__ == "__main__":
    unittest.main()
