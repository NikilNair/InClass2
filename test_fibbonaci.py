import unittest
import fibbonaci

class TestCase(unittest.TestCase):
    def test_fibbonaci_values(self):
        self.assertEqual(fibbonaci.program(3), 2)
        self.assertEqual(fibbonaci.program(4), 3)
        self.assertEqual(fibbonaci.program(5), 5)
        self.assertEqual(fibbonaci.program(8), 21)
        self.assertEqual(fibbonaci.program(10), 55)

    def test_factorial_values(self):
        self.assertEqual(fibbonaci.program1(2), 2)
        self.assertEqual(fibbonaci.program1(3), 6)
        self.assertEqual(fibbonaci.program1(4), 24)
        self.assertEqual(fibbonaci.program1(5), 120)
        self.assertEqual(fibbonaci.program1(6), 720)


if __name__ == '__main__':
    unittest.main()
