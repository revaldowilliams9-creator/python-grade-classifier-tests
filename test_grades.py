import unittest
from grades import classify_grade


class TestGradeClassifier(unittest.TestCase):
    def test_distinction(self):
        self.assertEqual(classify_grade(80), "Distinction")
        self.assertEqual(classify_grade(75), "Distinction")
        self.assertEqual(classify_grade(100), "Distinction")

    def test_pass(self):
        self.assertEqual(classify_grade(62), "Pass")
        self.assertEqual(classify_grade(50), "Pass")
        self.assertEqual(classify_grade(74.9), "Pass")

    def test_fail(self):
        self.assertEqual(classify_grade(40), "Fail")
        self.assertEqual(classify_grade(0), "Fail")
        self.assertEqual(classify_grade(49.9), "Fail")

    def test_out_of_range_raises_value_error(self):
        with self.assertRaises(ValueError):
            classify_grade(-1)
        with self.assertRaises(ValueError):
            classify_grade(101)

    def test_invalid_type_raises_type_error(self):
        with self.assertRaises(TypeError):
            classify_grade("80")
        with self.assertRaises(TypeError):
            classify_grade(True)
        with self.assertRaises(TypeError):
            classify_grade(False)


if __name__ == "__main__":
    unittest.main()
