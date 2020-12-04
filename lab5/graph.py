import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations


def AVGdegree(G, v):
    totalDegree = 0
    for node in nx.nodes(G):
        count = 0
        for neighbor in nx.neighbors(G, node):
            count += 1
        totalDegree += count

    avgDegree = totalDegree/v
    print("Average Degree is: ", int(avgDegree))
    return(int(avgDegree))


def Density(G, v, e):
    if v > 1:
        print("Density is: ", round((2*e)/(v*(v - 1)), 5))
        return(round((2*e)/(v*(v - 1)), 5))
    else:
        print("Density is: 0")
        return(0)


def Diameter(G, v):
    sum = []
    for v1, v2 in combinations(G.nodes, 2):
        if nx.has_path(G, v1, v2):
            sum.append(nx.shortest_path_length(G, v1, v2, method = "dijkstra"))
        else:
            print("The graph is not connected. Diameter is: infinite")
            return("infinite")

    print("Diameter is: ", max(sum))
    return(max(sum))


def ClusteringCoefficient(G, v):
    clusterCoeff = 0
    for node in nx.nodes(G):
        Ki, Ei = 0, 0
        for i in G.neighbors(node):
            Ki += 1

        for v1, v2 in combinations(G.neighbors(node), 2):
            if G.has_edge(v1, v2):
                Ei += 1
        
        if Ki > 1:
            clusterCoeff += (2*Ei)/(Ki*(Ki - 1))
    
    print("Clustering Coefficient is: ", round(clusterCoeff/v, 5))
    return(round(clusterCoeff/v, 5))


def DegreeDistribution(G, v):
    frequencyList = nx.degree_histogram(G)
    probDegreeList = [x/v for x in frequencyList]
    degreeList = [*range(0, len(frequencyList))]
    plt.plot(degreeList, probDegreeList, "g")
    plt.show()


if __name__ == "__main__":
    header_list = ["a", "b"]
    E = pd.read_csv('data/ENZYMES_g196.edges', sep = " ", header = None, names = header_list)
    G = nx.from_pandas_edgelist(E, "a", "b")

    num_nodes = nx.number_of_nodes(G)
    num_edges = nx.number_of_edges(G)
    print("Number of nodes: ", num_nodes)
    print("Number of edges: ", num_edges)

    nx.draw(G)
    plt.show()
    
    AVGdegree(G, num_nodes)
    Density(G, num_nodes, num_edges)
    Diameter(G, num_nodes)
    ClusteringCoefficient(G, num_nodes)

    DegreeDistribution(G, num_nodes)
