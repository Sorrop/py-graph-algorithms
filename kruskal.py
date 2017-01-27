import graph
from depth_first_search import depth_first_search


def Kruskal(G, w):
    '''
    Implementation of Kruskal's algorithm for obtaining the minimum
    spanning tree of a weighted undirected graph.
    [G]: graph.Graph instance. undirected and connected.
         If not connected we get a forest instead
    [w]: mapping from G's edges to corresponding weights

    Returns a list of the minimum spanning tree's edges
    '''

    # tiny function to use as key for sorting the edges of G
    def get_weight(e):
        return w[e]

    n = G.vertex_count()
    # sort the edges in non decreasing weight
    sorted_edges = sorted(list(G.edges()), key=get_weight)
    # instantiate the tree
    T = graph.Graph()

    # minimum edge will always belong to MST
    edge = sorted_edges.pop(0)
    endpoints = edge.endPoints()
    source = endpoints[0].element()
    destination = endpoints[1].element()

    # create vertices
    source_vertex = T.insert_vertex(source)
    destination_vertex = T.insert_vertex(destination)

    # for faster membership testing
    tree_vertices = {source, destination}

    # create first added edge
    tree_edges = []
    tree_edges.append(T.insert_edge(source_vertex,
                                    destination_vertex,
                                    source + destination))
    # var to hold the start of dfs (to discover cycle)
    tree_root = source_vertex

    while (T.vertex_count() < n):
        new_edge = sorted_edges.pop(0)
        endpoints = new_edge.endPoints()
        source = endpoints[0].element()
        destination = endpoints[1].element()

        # handle cases when a vertex is already inserted
        # into MST
        if source in tree_vertices:
            source_vertex = T.get_vertex(source)
        else:
            source_vertex = T.insert_vertex(source)
            tree_vertices.update(source)

        if destination in tree_vertices:
            destination_vertex = T.get_vertex(destination)
        else:
            destination_vertex = T.insert_vertex(destination)
            tree_vertices.update(destination)

        # insert new edge
        tree_edges.append(T.insert_edge(source_vertex,
                                        destination_vertex,
                                        source + destination))
        # if this edge introduces a cycle in the MST
        depth = depth_first_search(T)
        depth(T, tree_root)
        if depth.has_cycle:
            # get rid of it
            bad_edge = tree_edges.pop(-1)
            u, v = bad_edge.endPoints()
            # vertices are not deleted from the tree.
            # so in case that G is disconnected we will
            # get a forest instead.
            T.delete_edge(u, v)

    return T


if __name__ == '__main__':
    '''
    Example run of the algorithm
    '''

    example = [('a', 'b', 2), ('a', 'c', 3),
               ('b', 'c', 1), ('b', 'e', 4),
               ('b', 'd', 2), ('c', 'd', 1),
               ('c', 'e', 6), ('d', 'e', 7),
               ('d', 'f', 100), ('e', 'f', 5)]
    G, weight_mapping = graph.create_graph(example)

    T = Kruskal(G, weight_mapping)
    print('Example run on graph G with edges')
    print(example)
    for edge in T.edges():
        print(edge.element())
