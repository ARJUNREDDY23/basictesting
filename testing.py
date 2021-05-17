import unittest
import main


class TestMain(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(5, 4), 9)
        self.assertEqual(main.add(10,4),14)

    def test_sub(self):
        self.assertEqual(main.sub(5,4),1)
        self.assertEqual(main.sub(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(main.multiply(5,4),20)
        self.assertEqual(main.multiply(10, 4), 40)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            main.divide(5,0)
        self.assertEqual(main.divide(10,4),2.5)


if __name__ == "__main__":
    unittest.main()
