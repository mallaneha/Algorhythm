import unittest
from mergesort import mergesort


class TestSearch(unittest.TestCase):

    def test_mergesort(self):
        data = [1, 4, 3, 9, 6, 12, 7, 4, 8]
        dataS = data
        mergesort(data, 0, len(data) - 1)
        dataS.sort()
        self.assertEqual(data, dataS)


if __name__ == "__main__":
    unittest.main()