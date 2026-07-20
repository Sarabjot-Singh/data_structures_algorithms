import numpy as np

class Node:
    pass

class Graph:

    def __init__(self, type, edges, n):
        self.edges = edges
        self.type = type
        self.n = n

    
    def build_adjancency_matrix(self):
        graph = np.zeros((self.n, self.n))
        
        for edge in self.edges:
            source = edge[0]
            destination = edge[1]

            graph[source][destination] = 1
            if self.type == 'undirected':
                graph[destination][source] = 1

        return graph

    def build_adjancency_list(self):
        graph = [[] for _ in range(n)]
        
        for edge in self.edges:
            source = edge[0]
            destination = edge[1]
            graph[source].append(destination)
            if self.type == 'undirected':
                graph[destination].append(source)

        return graph
    
    def weighted_graph(self):
        pass
    