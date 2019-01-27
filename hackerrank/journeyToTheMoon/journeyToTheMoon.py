from graph import UndirectedGraph

def subset_size(graph, vertex, counter = 0):
    '''
    A recursive implementation of DFS to count the number of elements in the disjoint subset which 'vertex' belongs to.
    '''
    if not graph.marked[vertex]:
        graph.marked[vertex] = True
        counter += 1
        for adjacent_vertex in graph.adj(vertex):
            counter = subset_size(graph, adjacent_vertex, counter)
    return counter

def disjoint_subset_sizes(graph):
    '''
    A function to obtain the disjoint subset sizes from a graph.
    '''
    result = []
    for vertex in graph:
        if not graph.marked[vertex]:
            subset_counter = subset_size(graph, vertex)
            if subset_counter > 0:
                result.append(subset_counter)

    return result


def calculate_number_of_pairs(subset_counts):
    '''
    A recursive implementation to calculate the number of pairs.
    '''
    if type(subset_counts) is not list:
        raise TypeError("subset_counts must be a list of integers")

    if len(subset_counts) <= 1:
        return 0

    first_element = subset_counts[0]
    remaining_elements = subset_counts[1:]
    return first_element*sum(remaining_elements) + calculate_number_of_pairs(remaining_elements)


def journeyToMoon(n, astronaut):
    '''
    Function signature supplied by Hackerrank,
    and my implementation using supplied arguments: n, astronaut.
    '''
    graph = UndirectedGraph(n, astronaut)
    subset_sizes = disjoint_subset_sizes(graph)

    return calculate_number_of_pairs(subset_sizes)
