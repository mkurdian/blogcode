'''
Enhanced source code demonstrating the iterator pattern.
'''

import unittest
import itertools

# Class Implementations
class Bag:
    '''
    A simple data structure to store items in no particular order.
    This class implements __iter__ and is therefore iterable.
    '''
    def __init__(self):
        '''
        Create an empty Bag
        '''
        self.contents = []

    def add(self, item):
        '''
        Add an item
        '''
        self.contents.append(item)

    def is_empty(self):
        '''
        Check if the bag is empty
        '''
        return len(self.contents) == 0

    def size(self):
        '''
        Number of items in the bag
        '''
        return len(self.contents)

    def __repr__(self):
        '''
        Unambiguous representation of the Bag
        '''
        return str(self.contents)

    def __iter__(self):
        '''
        Return an iterator object
        '''
        return ArrayForwardIterator(self.contents)


class ArrayForwardIterator:
    '''
    An iterator class to be used with the Bag class
    '''
    def __init__(self, arr):
        '''
        Create an iterator object to start iteration from zero index
        '''
        self.arr = arr
        self.index = 0

    def __iter__(self):
        '''
        Returns itself
        '''
        return self

    def __next__(self):
        '''
        Returns the following item when next() is called
        '''
        if self.index == len(self.arr):
            raise StopIteration()

        item = self.arr[self.index]
        self.index += 1
        
        return item

# Testcases
class TestBag(unittest.TestCase):

    def setUp(self):
        self.bag = Bag()
    
    def test_constructor(self):
        bag = self.bag
        self.assertTrue(bag.is_empty())
        self.assertEqual(bag.size(), 0)

    def test_add(self):
        bag = self.bag
        bag.add('a')
        self.assertIn('a', bag.contents)
        bag.add('b')
        self.assertIn('b', bag.contents)

    def test_is_empty(self):
        bag = self.bag
        self.assertTrue(bag.is_empty())
        bag.add('a')
        self.assertFalse(bag.is_empty())

    def test_size(self):
        bag = self.bag
        self.assertEqual(bag.size(), 0)
        bag.add('a')
        self.assertEqual(bag.size(), 1)
        bag.add('b')
        self.assertEqual(bag.size(), 2)


class TestArrayForwardIterator(unittest.TestCase):

    def setUp(self):
        self.it = ArrayForwardIterator(['a', 'b', 'c'])

    def test_iterator_is_sliceable(self):
        slc = itertools.islice(self.it, 1, 3)
        self.assertEqual(list(slc), ['b','c'])

# Main
def main():

    # Construct a bag
    myBag = Bag()

    # Populate
    myBag.add('a')
    myBag.add('b')
    myBag.add('c')

    # Print to console
    for item in myBag:
        print(item)


if __name__ == '__main__':
    main()
