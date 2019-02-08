'''
A module that implements a class to represent an undirected graph.
'''

class UndirectedGraph:
    '''
    A class representing an undirected graph.
    Each vertex is represented by an integer from zero to the number of vertices minus one.
    '''
    def __init__(self, num_vertices, edges):

        if num_vertices is None:
            raise TypeError("Number of vertices cannot be None")

        if edges is None:
            raise TypeError("List of edges cannot be None")

        self.num_vertices = num_vertices
        self._graph = [[] for _ in range(self.num_vertices)]
        self.marked = [False] * self.num_vertices

        try:
            for edge in edges:
                self.__add_undirected_edge(edge)
        except Exception as e:
            print(e)

    def __iter__(self):
        return AdjacencyListGraphIterator(self.num_vertices)

    def __add_undirected_edge(self, edge):
        
        if edge is None:
            raise TypeError("Added edge cannot be None")

        v, w = edge

        if v is None or w is None:
            raise TypeError("Added vertex cannot be None")

        if w not in self._graph[v]:
            self._graph[v].append(w)
        if v not in self._graph[w]:
            self._graph[w].append(v)

    def adj(self, vertex):
        '''
        Return the list of adjacent vertices to the given vertex.
        '''
        return self._graph[vertex]


class AdjacencyListGraphIterator:
    '''
    A class to represent an iterator object for a graph with the adjacency list implementation.
    '''
    def __init__(self, num_vertices):
        self.index = 0
        self.num_vertices = num_vertices

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.num_vertices:
            raise StopIteration()

        vertex = self.index
        self.index += 1
        return vertex