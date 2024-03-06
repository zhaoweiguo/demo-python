import re
import unittest

class TestSplit(unittest.TestCase):
    def test_split_by_dot(self):
        text = "a.b.c.d"
        expected = ["a", "b", "c", "d"]
        actual = re.split("\.", text)
        self.assertEqual(expected, actual)

    def test_split_by_space(self):
        text = "a b  c   d"
        expected = ["a", "b", "c", "d"]
        actual = re.split("\s+", text)
        self.assertEqual(expected, actual)

    def test_split_by_lines(self):
        text = "a\nb\nc\nd"
        expected = ["a", "b", "c", "d"]
        actual = re.split("\n", text)
        self.assertEqual(expected, actual)

    def test_split_by_comma_and_space(self):
        text = "a, b ,  c,   d"
        expected = ["a", " b ", "  c", "   d"]
        actual = re.split(",", text)
        self.assertEqual(expected, actual)

    def test_capture_groups(self):
        text = "a1b2c3"
        expected = ["a", "1", "b", "2", "c", "3"]
        actual = re.split("([0-9])", text)
        self.assertNotEqual(expected, actual)

if __name__ == "__main__":
    unittest.main() 

