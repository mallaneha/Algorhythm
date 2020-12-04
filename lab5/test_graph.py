import unittest
import pandas as pd
import networkx as nx
from graph import AVGdegree, Density, Diameter, ClusteringCoefficient


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.header_list = ["a", "b", "w"]
        self.E = pd.read_csv('data/ENZYMES_g196.edges', sep = " ", header = None, names = self.header_list)
        self.G = nx.from_pandas_edgelist(self.E, "a", "b", ["w"])

        self.num_nodes = nx.number_of_nodes(self.G)
        self.num_edges = nx.number_of_edges(self.G)
        print("Number of nodes: ", self.num_nodes)
        print("Number of edges: ", self.num_edges)

    def test_AVGdegree(self):
        degree = 0
        for node in nx.nodes(self.G):
            degree += self.G.degree(node)
        avg = degree/self.num_nodes

        self.assertEqual(AVGdegree(self.G, self.num_nodes), int(avg))

    def test_Density(self):
        self.assertEqual(Density(self.G, self.num_nodes, self.num_edges), round(nx.density(self.G), 5))

    def test_Diameter(self):
        self.assertEqual(Diameter(self.G, self.num_nodes), nx.diameter(self.G))
    
    def test_ClusteringCoefficient(self):
        self.assertEqual(ClusteringCoefficient(self.G, self.num_nodes), round(nx.average_clustering(self.G), 5))


if __name__ == "__main__":
    unittest.main()
    