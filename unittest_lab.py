import unittest
from flask_lab3 import Diskriminant, roots

class MyTestCase(unittest.TestCase):
    def test_Diskriminant(self):
        self.assertEqual(Diskriminant(2,5,-3),49)

    def test_roots(self):
        self.assertEqual(roots(4,8,-6,1), (0.5, 0.25))


if __name__ == '__main__':
    unittest.main()
