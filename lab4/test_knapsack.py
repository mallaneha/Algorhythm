import unittest
from knapsack import Greedy, BruteForceZO, BruteForceF, Dynamic


class TestKnapsack(unittest.TestCase):

    def setUp(self):
        self.p = [5, 6, 7, 2]# profit
        self.w = [4, 2, 3, 1]# weight
        self.m = 8# max weight

    def test_Greedy(self):
        # array tuple = profit, weight, key
        array = [[5, 4, '1'], [6, 2, '2'],[7, 3, '3'], [2, 1, '4']]
        # solution tuple have the fractional profit and weight that are chosen
        solution = [[6, 2, '2'], [7, 3, '3'], [2, 1, '4'], [2.5, 2, '1']]
        profit = 17.5
        self.assertEqual(Greedy(array, 8), (solution, profit))

    def test_BruteForceZO(self):
        self.assertEqual(BruteForceZO(self.p, self.w, self.m), ('0111', 15))

    def test_BruteForceF(self):
        self.assertEqual(BruteForceF(self.p, self.w, self.m), ('11f0', 'f = (2/3)', 15.666))

    def test_Dynamic(self):
        self.assertEqual(Dynamic(self.p, self.w, self.m), ('0111', 15))


if __name__ == "__main__":
    unittest.main()
    