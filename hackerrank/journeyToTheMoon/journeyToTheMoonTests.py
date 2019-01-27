import unittest
from io import StringIO
import numpy as np

from journeyToTheMoon import journeyToMoon, calculate_number_of_pairs, disjoint_subset_sizes
from graph import UndirectedGraph

class TestJourneyToMoon(unittest.TestCase):

    def get_big_test_data(self):
        
        with open("journeyToTheMoonData.txt", 'r') as file:
            data = file.read()

        self.big_num_vertices, self.num_edges = np.array(StringIO(data).readline().split(), dtype=int)
        self.big_astronaut = np.genfromtxt(StringIO(data), skip_header=1, dtype=int)

    def test_01(self):
        self.assertEqual(journeyToMoon(5, [(0, 1), (2, 3), (0, 4)]), 6)

    def test_02(self):
        self.assertEqual(journeyToMoon(4, [(0, 2)]), 5)

    def test_03(self):
        self.assertEqual(journeyToMoon(1000, [(1, 2)]), 499499)

    def test_big_input(self):
        self.get_big_test_data()
        self.assertEqual(journeyToMoon(self.big_num_vertices, self.big_astronaut), 4527147)

class TestCalculateNumberOfPairs(unittest.TestCase):
    def test_calculation(self):
        self.assertEqual(calculate_number_of_pairs([3, 2]), 6)
        self.assertEqual(calculate_number_of_pairs([3, 2, 3]), 21)
        self.assertEqual(calculate_number_of_pairs([3]), 0)
        self.assertEqual(calculate_number_of_pairs([]), 0)

    def test_exception(self):
        with self.assertRaises(TypeError):
            result = calculate_number_of_pairs(None)
            
class TestGetSubsetCounts(unittest.TestCase):
    def test_calculation(self):
        graph = UndirectedGraph(5, [(0, 1), (2, 3), (0, 4)])
        self.assertEqual(disjoint_subset_sizes(graph), [3, 2])