import unittest
import itertools

from graph import UndirectedGraph, AdjacencyListGraphIterator

class TestUndirectedGraph(unittest.TestCase):
    def test_create_exceptions(self):
        with self.assertRaises(TypeError):
            graph = UndirectedGraph(None, [(0, 1), (2, 3), (0, 4)])

        with self.assertRaises(TypeError):
            graph = UndirectedGraph(4, None)

    def test_adj(self):
        graph = UndirectedGraph(5, [(0, 1), (2, 3), (0, 4)])
        self.assertEqual(graph.adj(0), [1, 4])
        self.assertEqual(graph.adj(1), [0])
        self.assertEqual(graph.adj(2), [3])
        self.assertEqual(graph.adj(3), [2])
        self.assertEqual(graph.adj(4), [0])

class TestIterator(unittest.TestCase):

    def setUp(self):
        self.it = AdjacencyListGraphIterator(10)

    def test_iterator_is_sliceable(self):
        slc = itertools.islice(self.it, 1, 4)
        self.assertEqual(list(slc), [1, 2, 3])