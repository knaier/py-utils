import unittest
from src.classes import Dog

class DogTest(unittest.TestCase):
    """ Tests for dog """

    def test_sit(self):
        print("test sitting")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()