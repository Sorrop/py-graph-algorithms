import math
import graph


def Bellman_Ford(G, w, start_vertex):
    '''
    Function for computing shortest paths on directed graphs.
    Reports detection of negative cycle if one exists.

    Inputs:
    [G]: graph.Graph object of graph representation
    [w]: weight mapping of edges
    [start_vertex]: the source to which shortest paths will be computed
                    its a graph.Vertex instance of G.

    Outputs:
    [distance_est]: mapping of vertices to the length of the shortes path
                    with start_vertex as source i.e. = d(start_vertex, v)
    [spt_predecessor]: mapping of vertice to their predecessor
                       in the shortest path tree with root start_vertex
    '''
    distance_est = {vertex: math.inf for vertex in G.vertices()}
    distance_est[start_vertex] = 0
    spt_predecessor = {vertex: None for vertex in G.vertices()}
    n = G.vertex_count()

    for i in range(1, n):
        for edge in G.edges():
            source, destination = edge.endPoints()
            # edge relaxation
            if distance_est[destination] > distance_est[source] + w[edge]:
                distance_est[destination] = distance_est[source] + w[edge]
                spt_predecessor[destination] = source

    for edge in G.edges():
        source, destination = edge.endPoints()
        if distance_est[destination] > distance_est[source] + w[edge]:
            return None, None

    return distance_est, spt_predecessor


if __name__ == '__main__':

    def print_results(d, p):
        '''
        Helper to print the results
        '''
        for key in p:
            if p[key] is None:
                print(key.element() + ' is the start vertex')
            else:
                path = [key]
                vertex = p[key]
                while not (vertex is None):
                    path.insert(0, vertex)
                    vertex = p[vertex]
                elements = [vertex.element() for vertex in path]
                print('Shortest path to ' + key.element() + ' with value: ' + str(d[key]))
                x = '->'.join(elements)
                print(x)

    E = [('s', 'b', 8), ('s', 'a', 6), ('b', 'a', 7), ('b', 'c', 2),
         ('a', 'c', -5), ('e', 'b', 1), ('a', 'd', 4), ('c', 'e', 3),
         ('c', 'd', -4), ('d', 'e', 2), ('e', 'f', 2), ('d', 'f', 5)]
    print('Big Example:')
    print(E)
    G, weight_mapping = graph.create_graph(E)
    start_vertex = G.get_vertex('s')
    d, p = Bellman_Ford(G, weight_mapping, start_vertex)
    print_results(d, p)

    E = [('a', 'b', 4), ('b', 'd', 10),
         ('d', 'f', 11), ('b', 'c', 5),
         ('a', 'c', 2), ('c', 'e', 3),
         ('e', 'd', 4)]
    G, weight_mapping = graph.create_graph(E)
    start_vertex = G.get_vertex('a')
    d, p = Bellman_Ford(G, weight_mapping, start_vertex)
    print('====================')
    print('Smaller Example:')
    print(E)
    print_results(d, p)
