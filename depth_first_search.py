class depth_first_search:
    '''
    Callable class that is instantiated on a graph.
    Performs the classic depth first traversal.
    '''

    def __init__(self, G):
        '''
        Constructor of the class
        [time]: counter to record [arrival] and
                [departure] times of the algorithm in each node.
        [state]: mapping from vertices to a state that can be 'unexplored',
                 'exploring' and 'explored'.
        [has_cycle]: boolean to indicate if the algorithm discovered that
                     the graph has a cycle
        [depth_traversal]: a list that we manipulate as a stack
                           that holds the edges of the resulting
                           depth first traversal (DFS tree)
        [top_ordering]: list with vertices of G sorted topologicaly
                        If has_cycle == true it is deemed meaningless
        '''
        self.time = 0
        self.state = {vertex: 'unexplored' for vertex in G.vertices()}
        self.depth_traversal = []

        self.arrival = {vertex: None for vertex in G.vertices()}
        self.departure = {vertex: None for vertex in G.vertices()}

        # edge_added is consulted in order to
        # avoid identifying false back edges
        self.edge_added = {edge: False for edge in G.edges()}

        self.has_cycle = False
        if G.is_directed:
            self._top_ordering = []
        else:
            self._top_ordering = None

    def dfs_compute(self, G, start):
        '''
        Put the unexplored neighbors of start vertex in a list
        and recursively do the same for each one of them.
        '''
        self.state[start] = 'exploring'
        self.time = self.time + 1
        self.arrival[start] = self.time
        for edge in G.incident_edges(start, outgoing=True):
            neighbor = edge.opposite(start)
            if self.state[neighbor] == 'unexplored':
                self.depth_traversal.append(edge)
                self.edge_added[edge] = True
                self.dfs_compute(G, neighbor)
            else:
                if self.edge_added[edge]:
                    continue
                if self.state[neighbor] == 'exploring':
                    self.has_cycle = True
        self.time = self.time + 1
        self.departure[start] = self.time
        self.state[start] = 'explored'
        self._top_ordering.insert(0, start)

    def get_topological_order(self, G, start):
        if not G.is_directed:
            raise Exception('G is undirected')

        self.dfs_compute(G, start)
        if self.has_cycle:
            return None
        else:
            return self._top_ordering
