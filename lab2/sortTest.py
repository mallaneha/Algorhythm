import unittest
from mergesort import mergesort
from insertionsort import insertionsort


class TestSort(unittest.TestCase):

    def test_mergesort(self):
        data = [1, 4, 3, 9, 6, 12, 7, 4, 8]
        dataS = data
        mergesort(data, 0, len(data) - 1)
        dataS.sort()
        self.assertEqual(data, dataS)


    def test_insertionsort(self):
        data = [1, 4, 3, 9, 6, 12, 7, 4, 8]
        dataS = data
        insertionsort(data)
        dataS.sort()
        self.assertEqual(data, dataS)


if __name__ == "__main__":
    unittest.main()