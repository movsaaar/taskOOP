import unittest
from matrixtask import *

class TestMatrix(unittest.TestCase):
    def setUp(self):
        # Создаём матрицы для теста
        self.m1 = Matrix(2, 2, data=[[1, 2], [3, 4]])
        self.m2 = Matrix(2, 2, data=[[5, 6], [7, 8]])
        self.m3 = Matrix(2, 2, data=[[1, 2], [3, 4]])

    def test_eq(self):
        self.assertTrue(self.m1 == self.m3)
        self.assertFalse(self.m1 == self.m2)

    def test_add(self):
        result = self.m1 + self.m2
        expected = Matrix(2, 2, data=[[6, 8], [10, 12]])
        self.assertEqual(result, expected)

    def test_mul(self):
        result = self.m1 * 3
        expected = Matrix(2, 2, data=[[3, 6], [9, 12]])
        self.assertEqual(result, expected)

    def test_add_size_error(self):
        m_small = Matrix(1, 1, data=[[1]])
        with self.assertRaises(ValueError):
            _ = self.m1 + m_small

    def test_mul_type_error(self):
        with self.assertRaises(ValueError):
            _ = self.m1 * "abc"

if __name__ == "__main__":
    unittest.main()
