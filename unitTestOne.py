import unittest
import SimpleProgram

class Testdivide(unittest.TestCase):
     def test_divide(self):
          self.assertEqual(functions.divide(6, 3), 2)
if __name__ == '__main__':
    unittest.main()
