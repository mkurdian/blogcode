from graph import UndirectedGraph

def subset_size(graph, vertex):
    '''
    An iterative implementation of DFS to count the number of elements in the disjoint subset which 'vertex' belongs to.
    '''
    stack = [vertex]
    counter = 0

    while len(stack) != 0:
        current_vertex = stack.pop()
        if not graph.marked[current_vertex]:
            graph.marked[current_vertex] = True
            counter += 1
            for adjacent_vertex in graph.adj(current_vertex):
                stack.append(adjacent_vertex)

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
    An iterative implementation to calculate the number of pairs.
    '''
    if type(subset_counts) is not list:
        raise TypeError("subset_counts must be a list of integers")

    if len(subset_counts) == 0:
        return 0

    result = 0
    summation_so_far = subset_counts[0]

    for count in subset_counts[1:]:
        result += summation_so_far * count
        summation_so_far += count

    return result


def journeyToMoon(n, astronaut):
    '''
    Function signature supplied by Hackerrank,
    and my implementation using supplied arguments: n, astronaut.
    '''
    graph = UndirectedGraph(n, astronaut)
    subset_sizes = disjoint_subset_sizes(graph)

    return calculate_number_of_pairs(subset_sizes)
