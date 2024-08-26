import unittest
from py_utils_knaier.core.classes import Dog

class DogTest(unittest.TestCase):
    """ Tests for dog """

    def test_sit(self):
        print("test sitting")
        self.assertTrue(True)

    def setUp(self) -> None:
        print("Setup")


if __name__ == '__main__':
    unittest.main()
