import math
from depth_first_search import depth_first_search


def dag_shortest_paths(G, w, start_vertex):

    traversal = depth_first_search(G)
    ordering = traversal.get_topological_order(G, start_vertex)

    distance_est = {vertex: math.inf for vertex in G.vertices()}
    distance_est[start_vertex] = 0
    spt_predecessor = {vertex: None for vertex in G.vertices()}
    n = len(ordering)

    for i in range(n):
        source = ordering[i]
        for edge in G.incident_edges(source):
            destination = edge.opposite(source)
            if distance_est[destination] > distance_est[source] + w[edge]:
                distance_est[destination] = distance_est[source] + w[edge]
                spt_predecessor[destination] = source

    return distance_est, spt_predecessor


if __name__ == '__main__':
    import graph

    E = [('a', 'b', 4), ('b', 'd', 10),
         ('d', 'f', 11), ('b', 'c', 5),
         ('a', 'c', 2), ('c', 'e', 3),
         ('e', 'd', 4)]
    print('Shortest paths from a for graph')
    print(E)
    G, weight_mapping = graph.create_graph(E, is_directed=True)
    start_vertex = G.get_vertex('a')
    d, p = dag_shortest_paths(G, weight_mapping, start_vertex)
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
