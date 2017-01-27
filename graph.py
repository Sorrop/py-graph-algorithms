class Graph:
    '''
    Representation of a simple graph using an adjacency map.
    There exist nested Classes for Vertex and Edge objects and
    useful methods for vertex and edge, edge incidence and
    vertex degree retrieval plus edge and vertex insertion
    '''

# ------------------------- nested Vertex class -------------------------

    class Vertex:
        '''
        Class for representing vertex structure for a graph.
        '''
        __slots__ = '_element'

        def __init__(self, x):
            '''
            Do not call constructor directly. Use Graph's insert_vertex(x).
            '''
            self._element = x

        def element(self):
            '''
            Return element associated with this vertex.
            '''
            return self._element

        def __hash__(self):
            '''
            will allow vertex to be a map/set key
            '''
            return hash(id(self))

# ------------------------- nested Edge class ---------------------------

    class Edge:
        '''
        Class for representing edge structure for a graph.
        '''
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            '''
            Do not call constructor directly. Use Graph's insert_edge(x).
            '''
            self._origin = u
            self._destination = v
            self._element = x

        def endPoints(self):
            '''
            Return (u,v) tuple for vertices u and v.
            '''
            return (self._origin, self._destination)

        def opposite(self, v):
            '''
            Return the vertex that is opposite v on this edge.
            '''
            return self._destination if self._origin == v else self._origin

        def element(self):
            '''
            Return element associated with this edge.
            '''
            return self._element

        def __hash__(self):
            '''
            will allow edge to be a map/set key
            '''
            return hash(id(self))

# ------------------------- Graph Methods -------------------------------
    def __init__(self, directed=False):
        '''
        Create an empty graph (undirected, by default).
        Graph is directed if optional paramter is set to True.
        '''

        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        '''
        Return True if graph is directed
        '''

        return self._outgoing is not self._incoming

    def vertex_count(self):
        '''
        Return the vertices count
        '''
        return len(self._outgoing)

    def vertices(self):
        '''
        Return an iterator over the graph's vertices
        '''

        return self._outgoing.keys()

    def get_vertex(self, el):
        '''
        Return the graph's vertex with corresponding element
        equal to el. Return None on failure
        '''
        for vertex in self.vertices():
            if vertex.element() == el:
                return vertex

        return None

    def edges_count(self):
        '''
        Return the edges count
        '''

        edges = set()
        for secondary_map in self._outgoing.values():
            edges.update(secondary_map.values())
        return len(edges)

    def edges(self):
        '''
        Return a set of graph's edges
        '''
        edges = set()
        for secondary_map in self._outgoing.values():
            edges.update(secondary_map.values())
        return edges

    def get_edge(self, u, v):
        '''
        Return the edge from u to v
        '''
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        '''
        Return the number of incident vertices to v
        If graph is directed then handle the case of indegree
        '''

        inc = self._outgoing if outgoing else self._incoming
        return len(inc[v])

    def incident_edges(self, v, outgoing=True):
        '''
        Return all incident edges to node v.
        If graph is directed, handle the case of incoming edges
        '''
        inc = self._outgoing if outgoing else self._incoming
        if v not in inc:
            return None
        for edge in inc[v].values():
            yield edge

    def adjacent_vertices(self, v, outgoing=True):
        '''
        Return adjacent vertices to a given vertex
        '''
        if outgoing:
            if v in self._outgoing:
                return self._outgoing[v].keys()
            else:
                return None
        else:
            if v in self._incoming:
                return self._incoming[v].keys()
            else:
                return None

    def insert_vertex(self, x=None):
        '''
        Insert and return a new Vertex with element x
        '''
        for vertex in self.vertices():
            if (vertex.element() == x):
                # raise exception if vertice exists in graph
                # exception can be handled from the class user
                raise Exception('Vertice already exists')
                return None

        v = self.Vertex(x)

        self._outgoing[v] = {}
        if self.is_directed:
            self._incoming[v] = {}

        return v

    def insert_edge(self, u, v, x=None):
        '''
        Insert and return a new Edge from u to v with auxiliary element x.
        '''
        if (v not in self._outgoing) or (v not in self._outgoing):
            # raise exception if one of vertices does not exist
            # exception can be handled from the class user
            raise Exception('One of the vertices does not exist')
            return None

        if self.get_edge(u, v):
            # no multiple edges
            # exception can be handled from the class user
            raise Exception('Edge already exists.')
            return None

        e = self.Edge(u, v, x)

        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def delete_edge(self, u, v):
        if not self.get_edge(u, v):
            # exception for trying to delete non-existent edge
            # can be handled from class user
            raise Exception('Edge is already non-existent.')
            return None

        u_neighbours = self._outgoing[u]
        del u_neighbours[v]
        v_neighbours = self._incoming[v]
        del v_neighbours[u]

        return None

    def delete_vertex(self, x):
        '''
        Delete vertex and all its adjacent edges from graph
        '''

        if (x not in self._outgoing) and (x not in self._incoming):
            raise Exception('Vertex already non-existent')
            return None

        secondary_map = self._outgoing[x]
        for vertex in secondary_map:
            # delete reference to incident edges
            if self.is_directed():
                del self._incoming[vertex][x]
            else:
                del self._outgoing[vertex][x]
        # delete reference to the vertex itself
        del self._outgoing[x]
        return None


def create_graph(sequence, is_directed=False):

    G = Graph(directed=is_directed)
    weight_mapping = {}

    if len(sequence[0]) == 3:
        weighted = True
    else:
        weighted = False

    for edge in sequence:
        source, destination = edge[0:2]
        try:
            source_vertex = G.insert_vertex(source)
        except Exception:
            source_vertex = G.get_vertex(source)

        try:
            destination_vertex = G.insert_vertex(destination)
        except Exception:
            destination_vertex = G.get_vertex(destination)

        new_edge = G.insert_edge(source_vertex,
                                 destination_vertex,
                                 str(source) + str(destination))
        if weighted:
            weight_mapping[new_edge] = edge[2]
        else:
            weight_mapping[new_edge] = 1

    return G, weight_mapping


if __name__ == '__main__':

    # undirected example
    E = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = create_graph(E)
    print('Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.')
    print('Is the graph directed?: ' + str(G.is_directed()))
    a = G.get_vertex('a')
    print('Incident edges to: ' + a.element())
    for edge in G.incident_edges(a):
        print(edge.element())
    print('Adjacent vertices to: ' + a.element())
    x = G.adjacent_vertices(a, outgoing=True)
    for vertex in x:
        print(vertex.element())
    print('Deleting vertex a.')
    G.delete_vertex(a)
    print('Vertices count of G: ' + str(G.vertex_count()))
    for vertex in G.vertices():
        print(vertex.element())
    print('Edges count of G: ' + str(G.edges_count()))
    for edge in G.edges():
        print(edge.element())
    # =========================================================================
    # =========================================================================
    # =========================================================================
    # directed example
    E = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    G, _ = create_graph(E)
    print('Undirected G=(V,E) with V=(a,b,c) and E={(a,b),(b,c),(a,c)}.')
    print('Is the graph directed?: ' + str(G.is_directed()))
    a = G.get_vertex('a')
    print('Is the graph directed?: ' + str(G.is_directed()))
    print('Incident edges to: ' + a.element())
    for edge in G.incident_edges(a):
        print(edge.element())
    print('Adjacent vertices to: ' + a.element())
    x = G.adjacent_vertices(a, outgoing=True)
    for vertex in x:
        print(vertex.element())
    print('Deleting vertex a.')
    G.delete_vertex(a)
    print('Vertices count of G: ' + str(G.vertex_count()))
    for vertex in G.vertices():
        print(vertex.element())
    print('Edges count of G: ' + str(G.edges_count()))
    for edge in G.edges():
        print(edge.element())
