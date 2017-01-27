from PriorityQueue import PriorityQueue
import math


def Dijkstra(G, w, start_vertex):
    '''
    Implementation of dijkstra algorithms
    for computing shortest paths on directed graphs with positive weights.
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
    p_queue = PriorityQueue()
    spt_predecessor = {vertex: None for vertex in G.vertices()}

    p_queue.add(start_vertex, distance_est[start_vertex])

    while True:
        try:
            source = p_queue.pop()
        except KeyError:
            # when the queue is empty either we have examined all
            # vertices or there are no others reachable from start_vertex
            break

        for edge in G.incident_edges(source, outgoing=True):
            destination = edge.opposite(source)
            if distance_est[destination] > distance_est[source] + w[edge]:
                # relaxation step
                distance_est[destination] = distance_est[source] + w[edge]
                # if vertex already in queue then priority is updated
                p_queue.add(destination, distance_est[destination])
                # update the predecessor also
                spt_predecessor[destination] = source

    return distance_est, spt_predecessor
