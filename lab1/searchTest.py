import unittest
from search import linear_search
from search import binary_search 

class TestSearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 5, 6, 12, 7, 4, 8]
        self.assertEqual(linear_search(data, 6), 4)
        self.assertEqual(linear_search(data, 10),  -1)
        self.assertEqual(binary_search(data, 6), 4)
        self.assertEqual(binary_search(data, 10),  -1)

    def test_searchChar(self):
        data = ['t', 'a', 'b', 'l', 'e']
        self.assertEqual(linear_search(data, 'a'), 1)
        self.assertEqual(binary_search(data, 'a'), 1)


if __name__ == "__main__":
    unittest.main()